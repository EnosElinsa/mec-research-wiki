import assert from "node:assert/strict";
import { mkdtemp, readFile, rm } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import test from "node:test";

const GENERIC_INSTITUTION_PROFILE = Object.freeze({
  organization: "Example University",
  carsiSchoolPlaceholder: "Institution name",
  carsiSearchText: "Example University",
  carsiInstitution: "Example University (Example)",
  carsiLoginButtonName: "Continue",
  carsiEntityId: "https://login.example.edu/idp/shibboleth",
  credentialHost: "login.example.edu",
  usernameLabel: "Account",
  passwordLabel: "Passcode",
  loginButtonName: "Sign in",
  resourceAccessUrl: "https://ds.carsi.edu.cn/resource/gotoResource.php?id=resource:example-ieee",
  attributeReleaseTitle: "",
  attributeReleaseAcceptControlName: "",
  attributeReleaseRejectControlName: "",
});

const LEGACY_GXU_PROFILE = Object.freeze({
  organization: "Guangxi University",
  carsiSchoolPlaceholder: "请输入高校/机构名称",
  carsiSearchText: "广西大学",
  carsiInstitution: "广西大学（GuangXi University）",
  carsiLoginButtonName: "登录",
  carsiEntityId: "https://idp.gxu.edu.cn/idp/shibboleth",
  credentialHost: "idp.gxu.edu.cn",
  usernameLabel: "用户名",
  passwordLabel: "密码",
  loginButtonName: "登录",
  resourceAccessUrl: "https://ds.carsi.edu.cn/resource/gotoResource.php?id=resource:6",
  attributeReleaseTitle: "",
  attributeReleaseAcceptControlName: "_eventId_proceed",
  attributeReleaseRejectControlName: "_eventId_AttributeReleaseRejected",
});

let subject = {};
try {
  subject = await import("../ieee-playwright.mjs");
  const retrieveIeeePaper = subject.retrieveIeeePaper;
  subject = {
    ...subject,
    retrieveIeeePaper: (options) => retrieveIeeePaper({
      institutionProfile: LEGACY_GXU_PROFILE,
      ...options,
    }),
  };
} catch {
  // RED phase: the assertions below describe the replacement automation API.
}

class FakeResponse {
  constructor(body, { status = 200, contentType = "application/pdf", location = "" } = {}) {
    this.bytes = Buffer.from(body);
    this.statusCode = status;
    this.contentType = contentType;
    this.location = location;
  }

  ok() { return this.statusCode >= 200 && this.statusCode < 300; }
  status() { return this.statusCode; }
  headers() {
    return {
      "content-type": this.contentType,
      ...(this.location ? { location: this.location } : {}),
    };
  }
  async body() { return this.bytes; }
}

class FakeRequestContext {
  constructor(responses) {
    this.responses = [...responses];
    this.calls = [];
  }

  async get(url, options) {
    this.calls.push({ url, options });
    const response = this.responses.shift();
    if (!response) throw new Error("Unexpected PDF request");
    return response;
  }
}

class FakeLocator {
  constructor(page, key) {
    this.page = page;
    this.key = key;
  }

  async count() {
    if (this.key === "pdf") return 2;
    if (this.key === "pdf-primary") return 1;
    if (this.key === "iframe") {
      if (this.page.stampVisits <= this.page.missingPdfFrameVisits) return 0;
      return this.page.currentUrl.includes("/stamp/stamp.jsp") ? 1 : 0;
    }
    if (this.key === "institution") return this.page.institutionReady ? 1 : 0;
    if (this.key === "username" && this.page.idpSessionAutoRedirect) {
      this.page.pendingRedirect = "https://ds.carsi.edu.cn/resource/resource.php";
      return 0;
    }
    if (this.key === "attribute-proceed" || this.key === "attribute-reject") {
      if (this.key === "attribute-reject" && this.page.attributeRejectMissing) return 0;
      return (
        this.page.attributeControlsReady
        && this.page.currentUrl.includes("/idp/profile/SAML2/Redirect/SSO")
      ) ? 1 : 0;
    }
    return 1;
  }

  async waitFor() {
    if (this.key === "institution") this.page.institutionReady = true;
    if (this.key === "attribute-proceed" || this.key === "attribute-reject") {
      this.page.attributeControlsReady = true;
    }
  }

  async getAttribute(name) {
    if (this.key === "pdf-primary" && name === "href") {
      return "/stamp/stamp.jsp?tp=&arnumber=11014597";
    }
    if (this.key === "iframe" && name === "src") {
      return "/stampPDF/getPDF.jsp?tp=&arnumber=11014597&ref=synthetic";
    }
    if (this.key === "title-result" && name === "href") return "/document/11014597";
    return null;
  }

  async evaluate(_callback, value) {
    if (this.key !== "carsi-entity-id") throw new Error(`Unexpected evaluate target: ${this.key}`);
    this.page.carsiEntityId = value;
  }

  async inputValue() {
    if (this.key !== "carsi-entity-id") throw new Error(`Unexpected inputValue target: ${this.key}`);
    return this.page.carsiEntityId;
  }

  async fill(value) {
    this.page.actions.push(["fill", this.key]);
    if (this.key === "school") this.page.school = value;
    if (this.key === "username") this.page.username = value;
    if (this.key === "password") this.page.password = value;
  }

  async click() {
    this.page.actions.push(["click", this.key]);
    if (this.key === "carsi-login") {
      if (this.page.stayOnCarsi) {
        this.page.currentUrl = "https://ds.carsi.edu.cn/ds/index.html";
        this.page.authenticated = true;
      } else if (this.page.deferCarsiRedirect) {
        this.page.pendingRedirect = `https://${this.page.redirectHost}/login`;
      } else {
        this.page.currentUrl = `https://${this.page.redirectHost}/login`;
      }
    } else if (this.key === "gxu-login") {
      this.page.authenticated = true;
      if (this.page.attributeReleaseAfterLogin) {
        this.page.currentUrl = `https://${this.page.redirectHost}/idp/profile/SAML2/Redirect/SSO?execution=e2s1`;
        if (this.page.attributeReleaseProceeds) {
          this.page.pendingRedirect = "https://ds.carsi.edu.cn/resource/resource.php";
        }
      } else {
        this.page.currentUrl = "https://ds.carsi.edu.cn/ds/index.html";
      }
    } else if (this.key === "attribute-proceed" && this.page.attributeReleaseAfterLogin) {
      this.page.currentUrl = "https://ds.carsi.edu.cn/resource/resource.php";
    }
  }
}

class FakePage {
  constructor({ redirectHost = "idp.gxu.edu.cn", denyFirstStamp = false, institutionInitiallyReady = true, evaluateFailures = 0, paperNavigationFailures = 0, missingPdfFrameVisits = 0, deferCarsiRedirect = false, stayOnCarsi = false, requireAttributeRelease = false, delayedAttributeReleaseControls = false, attributeReleaseProceeds = false, attributeReleaseAfterLogin = false, attributeRejectMissing = false, idpSessionAutoRedirect = false, resourceGatewayRequiresLogin = true, resourceGatewayPortalVisits = 0, institutionProfile = null } = {}) {
    this.currentUrl = "about:blank";
    this.redirectHost = redirectHost;
    this.actions = [];
    this.school = "";
    this.username = "";
    this.password = "";
    this.carsiEntityId = "";
    this.authenticated = false;
    this.denyFirstStamp = denyFirstStamp;
    this.institutionReady = institutionInitiallyReady;
    this.evaluateFailures = evaluateFailures;
    this.paperNavigationFailures = paperNavigationFailures;
    this.missingPdfFrameVisits = missingPdfFrameVisits;
    this.stampVisits = 0;
    this.deferCarsiRedirect = deferCarsiRedirect;
    this.stayOnCarsi = stayOnCarsi;
    this.requireAttributeRelease = requireAttributeRelease;
    this.attributeControlsReady = !delayedAttributeReleaseControls;
    this.attributeReleaseProceeds = attributeReleaseProceeds;
    this.attributeReleaseAfterLogin = attributeReleaseAfterLogin;
    this.attributeRejectMissing = attributeRejectMissing;
    this.idpSessionAutoRedirect = idpSessionAutoRedirect;
    this.resourceGatewayRequiresLogin = resourceGatewayRequiresLogin;
    this.resourceGatewayPortalVisits = resourceGatewayPortalVisits;
    this.resourceGatewayVisits = 0;
    this.institutionProfile = institutionProfile;
    this.pendingRedirect = "";
    this.navigations = [];
  }

  async goto(url) {
    this.navigations.push(url);
    if (url.includes("/document/11014597") && this.paperNavigationFailures > 0) {
      this.paperNavigationFailures -= 1;
      this.currentUrl = "chrome-error://chromewebdata/";
      throw new Error("page.goto: net::ERR_ABORTED at chrome-error://chromewebdata/");
    }
    if (url.includes("/stamp/stamp.jsp")) this.stampVisits += 1;
    if (url.includes("/stamp/stamp.jsp") && this.denyFirstStamp && !this.authenticated) {
      this.currentUrl = "https://ieeexplore.ieee.org/document/11014597?denied=";
    } else if (
      url === "https://ds.carsi.edu.cn/resource/gotoResource.php?id=resource:6"
      || url === this.institutionProfile?.resourceAccessUrl
    ) {
      this.resourceGatewayVisits += 1;
      if (this.resourceGatewayRequiresLogin && !this.authenticated) {
        this.currentUrl = "https://ds.carsi.edu.cn/login/index.html";
      } else if (this.requireAttributeRelease) {
        this.currentUrl = "https://idp.gxu.edu.cn/idp/profile/SAML2/Redirect/SSO?execution=e2s1";
        if (this.attributeReleaseProceeds) {
          this.pendingRedirect = "https://ieeexplore.ieee.org/Xplore/home.jsp";
        }
      } else if (this.resourceGatewayVisits <= this.resourceGatewayPortalVisits) {
        this.currentUrl = "https://ds.carsi.edu.cn/resource/resource.php";
      } else {
        this.currentUrl = "https://ieeexplore.ieee.org/Xplore/home.jsp";
      }
    } else {
      this.currentUrl = url;
    }
  }

  url() { return this.currentUrl; }

  async waitForLoadState() {}

  async waitForURL(predicate) {
    if (this.pendingRedirect) {
      this.currentUrl = this.pendingRedirect;
      this.pendingRedirect = "";
      if (this.idpSessionAutoRedirect && this.currentUrl.includes("ds.carsi.edu.cn")) {
        this.authenticated = true;
      }
    }
    if (!predicate(new URL(this.currentUrl))) throw new Error("waitForURL timed out");
  }

  async evaluate() {
    if (this.evaluateFailures > 0) {
      this.evaluateFailures -= 1;
      throw new Error("Execution context was destroyed, most likely because of a navigation");
    }
    return {
      title: "A Synthetic IEEE Paper",
      doi: "10.1109/TEST.2026.1",
      canonicalUrl: "https://ieeexplore.ieee.org/document/11014597",
      userAgent: "Synthetic Chrome",
    };
  }

  locator(selector) {
    if (selector === 'a[href*="/stamp/stamp.jsp"]') return new FakeLocator(this, "pdf");
    if (selector === 'a.xpl-btn-pdf[href*="/stamp/stamp.jsp"]') return new FakeLocator(this, "pdf-primary");
    if (selector === 'iframe[src*="/stampPDF/getPDF.jsp"]') return new FakeLocator(this, "iframe");
    if (selector === 'input[name="entityID"]') return new FakeLocator(this, "carsi-entity-id");
    if (selector === 'button[name="_eventId_proceed"]') return new FakeLocator(this, "attribute-proceed");
    if (selector === 'button[name="_eventId_AttributeReleaseRejected"]') return new FakeLocator(this, "attribute-reject");
    throw new Error(`Unexpected selector: ${selector}`);
  }

  getByPlaceholder(name) {
    if (this.institutionProfile) assert.equal(name, this.institutionProfile.carsiSchoolPlaceholder);
    return new FakeLocator(this, "school");
  }
  getByLabel(name) {
    const usernameLabel = this.institutionProfile?.usernameLabel ?? "用户名";
    return new FakeLocator(this, name === usernameLabel ? "username" : "password");
  }
  getByRole(role) {
    if (role === "option") return new FakeLocator(this, "institution");
    if (role === "link") return new FakeLocator(this, "title-result");
    if (role === "button") {
      return new FakeLocator(this, this.currentUrl.includes(this.redirectHost) ? "gxu-login" : "carsi-login");
    }
    throw new Error(`Unexpected role: ${role}`);
  }
}

function fakeContext(responses) {
  return { request: new FakeRequestContext(responses) };
}

test("keeps reference classification and exact profile-scoped credential gating", () => {
  assert.equal(subject.classifyPaperReference("https://ieeexplore.ieee.org/document/11014597").kind, "url");
  assert.equal(subject.classifyPaperReference("10.1109/TAP.2025.3571069").kind, "doi");
  assert.deepEqual(subject.classifyPaperReference("Exact title"), { kind: "title", value: "Exact title" });
  assert.equal(subject.isApprovedCredentialHost("IDP.GXU.EDU.CN", LEGACY_GXU_PROFILE), true);
  assert.equal(subject.isApprovedCredentialHost("idp.gxu.edu.cn.evil.example", LEGACY_GXU_PROFILE), false);
  assert.equal(Object.hasOwn(subject.SELECTORS, "carsiInstitution"), false);
  assert.equal(subject.SELECTORS.pdfPrimaryHref, 'a.xpl-btn-pdf[href*="/stamp/stamp.jsp"]');
  assert.equal(
    subject.sanitizeTransitionUrl("https://idp.example.edu/SSO?execution=e1s2&token=secret#state"),
    "https://idp.example.edu/SSO?execution=[redacted]&token=[redacted]",
  );
});

test("uses a configured institution profile instead of Guangxi-specific selectors", async () => {
  assert.deepEqual(
    subject.normalizeInstitutionProfile(GENERIC_INSTITUTION_PROFILE),
    GENERIC_INSTITUTION_PROFILE,
  );
  assert.equal(
    subject.isApprovedCredentialHost("LOGIN.EXAMPLE.EDU", GENERIC_INSTITUTION_PROFILE),
    true,
  );
  assert.equal(
    subject.isApprovedCredentialHost("login.example.edu.evil.example", GENERIC_INSTITUTION_PROFILE),
    false,
  );
  assert.throws(
    () => subject.normalizeInstitutionProfile({
      ...GENERIC_INSTITUTION_PROFILE,
      carsiEntityId: "https://login.example.edu:8443/idp/shibboleth",
    }),
    /CARSI entity ID/,
  );

  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-generic-profile-"));
  try {
    const page = new FakePage({
      redirectHost: GENERIC_INSTITUTION_PROFILE.credentialHost,
      institutionProfile: GENERIC_INSTITUTION_PROFILE,
    });
    const result = await subject.retrieveIeeePaper({
      page,
      browserContext: fakeContext([
        new FakeResponse("denied", { status: 403, contentType: "text/html" }),
        new FakeResponse("%PDF-1.7\ngeneric institution\n"),
      ]),
      reference: "https://ieeexplore.ieee.org/document/11014597",
      workDir: root,
      institutionProfile: GENERIC_INSTITUTION_PROFILE,
      credentialReader: async (host) => {
        assert.equal(host, GENERIC_INSTITUTION_PROFILE.credentialHost);
        return { username: "generic-user", password: "generic-password" };
      },
    });
    assert.equal(result.status, "downloaded");
    assert.equal(page.school, GENERIC_INSTITUTION_PROFILE.carsiSearchText);
    assert.equal(page.carsiEntityId, GENERIC_INSTITUTION_PROFILE.carsiEntityId);
    assert.equal(page.username, "generic-user");
    assert.equal(page.password, "generic-password");
    assert.ok(page.navigations.includes(GENERIC_INSTITUTION_PROFILE.resourceAccessUrl));
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("re-enters the exact resource gateway when login returns to the CARSI portal", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-portal-return-"));
  try {
    const page = new FakePage({ resourceGatewayRequiresLogin: false, resourceGatewayPortalVisits: 1 });
    const result = await subject.retrieveIeeePaper({
      page,
      browserContext: fakeContext([
        new FakeResponse("denied", { status: 403, contentType: "text/html" }),
        new FakeResponse("%PDF-1.7\nauthorized after portal return\n"),
      ]),
      reference: "https://ieeexplore.ieee.org/document/11014597",
      workDir: root,
      credentialReader: async () => ({ username: "user", password: "password" }),
    });
    assert.equal(result.status, "downloaded");
    assert.equal(page.resourceGatewayVisits, 2);
    assert.equal(page.actions.some((action) => action[1] === "resource-card"), false);
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("starts with the configured resource gateway so SAML preserves the IEEE return target", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-gateway-first-"));
  let credentialReads = 0;
  try {
    const page = new FakePage({ resourceGatewayRequiresLogin: true });
    const result = await subject.retrieveIeeePaper({
      page,
      browserContext: fakeContext([
        new FakeResponse("denied", { status: 403, contentType: "text/html" }),
        new FakeResponse("%PDF-1.7\ngateway-first\n"),
      ]),
      reference: "https://ieeexplore.ieee.org/document/11014597",
      workDir: root,
      credentialReader: async () => {
        credentialReads += 1;
        return { username: "user", password: "password" };
      },
    });
    assert.equal(result.status, "downloaded");
    assert.equal(credentialReads, 1);
    assert.equal(page.resourceGatewayVisits, 2);
    const gatewayIndex = page.navigations.indexOf(LEGACY_GXU_PROFILE.resourceAccessUrl);
    const genericDiscoveryIndex = page.navigations.indexOf("https://ds.carsi.edu.cn/login/index.html");
    assert.equal(gatewayIndex >= 0, true);
    assert.equal(genericDiscoveryIndex === -1 || gatewayIndex < genericDiscoveryIndex, true);
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("stops after three configured resource visits when CARSI keeps returning the portal", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-bounded-portal-return-"));
  const context = fakeContext([
    new FakeResponse("denied", { status: 403, contentType: "text/html" }),
  ]);
  const page = new FakePage({ resourceGatewayRequiresLogin: false, resourceGatewayPortalVisits: 99 });
  try {
    await assert.rejects(
      subject.retrieveIeeePaper({
        page,
        browserContext: context,
        reference: "https://ieeexplore.ieee.org/document/11014597",
        workDir: root,
        credentialReader: async () => ({ username: "user", password: "password" }),
      }),
      (error) => (
        error?.phase === "institutional-return"
        && error?.details?.resourceVisits === 3
        && error?.details?.transitions?.length === 3
      ),
    );
    assert.equal(page.resourceGatewayVisits, 3);
    assert.equal(context.request.calls.length, 1);
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("returns an existing repository bundle before PDF requests or authentication", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-duplicate-"));
  let credentialReads = 0;
  try {
    const browserContext = fakeContext([]);
    const result = await subject.retrieveIeeePaper({
      page: new FakePage(),
      browserContext,
      reference: "https://ieeexplore.ieee.org/document/11014597",
      workDir: root,
      repoRoot: root,
      duplicateChecker: async ({ title, doi }) => {
        assert.equal(title, "A Synthetic IEEE Paper");
        assert.equal(doi, "10.1109/TEST.2026.1");
        return { status: "existing", sourceRoot: "raw/sources", path: path.join(root, "raw", "sources", "paper") };
      },
      credentialReader: async () => {
        credentialReads += 1;
        return { username: "u", password: "p" };
      },
    });
    assert.equal(result.status, "existing");
    assert.equal(result.sourceRoot, "raw/sources");
    assert.equal(browserContext.request.calls.length, 0);
    assert.equal(credentialReads, 0);
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("downloads PDF bytes through the browser context's shared-cookie request API", async () => {
  assert.equal(typeof subject.retrieveIeeePaper, "function");
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-request-"));
  try {
    const page = new FakePage();
    const browserContext = fakeContext([new FakeResponse("%PDF-1.7\nsynthetic\n")]);
    const result = await subject.retrieveIeeePaper({
      page,
      browserContext,
      reference: "https://ieeexplore.ieee.org/document/11014597",
      workDir: root,
      credentialReader: async () => { throw new Error("credentials must not be read"); },
    });

    assert.equal(result.status, "downloaded");
    assert.equal((await readFile(result.pdfPath)).subarray(0, 5).toString("ascii"), "%PDF-");
    assert.equal(browserContext.request.calls.length, 1);
    assert.match(browserContext.request.calls[0].url, /\/stampPDF\/getPDF\.jsp/);
    assert.equal(browserContext.request.calls[0].options.maxRedirects, 0);
    assert.equal(
      browserContext.request.calls[0].options.headers.referer,
      "https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=11014597",
    );
    assert.equal(browserContext.request.calls[0].options.headers["user-agent"], "Synthetic Chrome");
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("rejects external PDF redirects without forwarding the request automatically", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-redirect-"));
  let credentialReads = 0;
  try {
    const browserContext = fakeContext([
      new FakeResponse("%PDF-redirect-body", {
        status: 302,
        location: "https://attacker.example/capture",
      }),
      new FakeResponse("%PDF-1.7\nauthorized\n"),
    ]);
    const result = await subject.retrieveIeeePaper({
      page: new FakePage(),
      browserContext,
      reference: "https://ieeexplore.ieee.org/document/11014597",
      workDir: root,
      credentialReader: async () => {
        credentialReads += 1;
        return { username: "synthetic-user", password: "synthetic-password" };
      },
    });
    assert.equal(result.status, "downloaded");
    assert.equal(credentialReads, 1);
    assert.equal(browserContext.request.calls.length, 2);
    assert.equal(browserContext.request.calls[0].options.maxRedirects, 0);
    assert.equal(browserContext.request.calls[0].url.startsWith("https://ieeexplore.ieee.org/"), true);
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("retries one transient IEEE navigation that destroys the metadata execution context", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-metadata-navigation-"));
  try {
    const result = await subject.retrieveIeeePaper({
      page: new FakePage({ evaluateFailures: 1 }),
      browserContext: fakeContext([new FakeResponse("%PDF-1.7\nmetadata retry\n")]),
      reference: "https://ieeexplore.ieee.org/document/11014597",
      workDir: root,
      credentialReader: async () => { throw new Error("credentials must not be read"); },
    });
    assert.equal(result.status, "downloaded");
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("retries one transient chrome-error navigation before reading metadata", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-paper-navigation-"));
  try {
    const page = new FakePage({ paperNavigationFailures: 1 });
    const result = await subject.retrieveIeeePaper({
      page,
      browserContext: fakeContext([new FakeResponse("%PDF-1.7\nnavigation retry\n")]),
      reference: "https://ieeexplore.ieee.org/document/11014597",
      workDir: root,
      credentialReader: async () => { throw new Error("credentials must not be read"); },
    });
    assert.equal(result.status, "downloaded");
    assert.equal(
      page.navigations.filter((url) => url.includes("/document/11014597")).length >= 2,
      true,
    );
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("treats a missing pre-auth PDF iframe as an entitlement signal without waiting", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-missing-frame-"));
  let credentialReads = 0;
  try {
    const page = new FakePage({ missingPdfFrameVisits: 1 });
    const result = await subject.retrieveIeeePaper({
      page,
      browserContext: fakeContext([new FakeResponse("%PDF-1.7\nafter missing frame\n")]),
      reference: "https://ieeexplore.ieee.org/document/11014597",
      workDir: root,
      credentialReader: async () => {
        credentialReads += 1;
        return { username: "user", password: "password" };
      },
    });
    assert.equal(result.status, "downloaded");
    assert.equal(credentialReads, 1);
    assert.equal(page.stampVisits, 2);
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("authenticates exactly once and retries the PDF request in the same persistent context", async () => {
  assert.equal(typeof subject.retrieveIeeePaper, "function");
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-auth-"));
  let credentialReads = 0;
  try {
    const page = new FakePage();
    const browserContext = fakeContext([
      new FakeResponse("not a pdf", { status: 418, contentType: "text/html" }),
      new FakeResponse("%PDF-1.7\nauthorized\n"),
    ]);
    const result = await subject.retrieveIeeePaper({
      page,
      browserContext,
      reference: "https://ieeexplore.ieee.org/document/11014597",
      workDir: root,
      credentialReader: async (host) => {
        credentialReads += 1;
        assert.equal(host, "idp.gxu.edu.cn");
        return { username: "synthetic-user", password: "synthetic-password" };
      },
    });

    assert.equal(result.status, "downloaded");
    assert.equal(credentialReads, 1);
    assert.equal(browserContext.request.calls.length, 2);
    assert.equal(page.school, "广西大学");
    assert.equal(page.username, "synthetic-user");
    assert.equal(page.password, "synthetic-password");
    assert.equal(
      page.navigations.includes("https://ds.carsi.edu.cn/resource/gotoResource.php?id=resource:6"),
      true,
    );
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("waits for the user at Guangxi University attribute release without choosing for them", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-attribute-release-"));
  const page = new FakePage({ requireAttributeRelease: true });
  try {
    await assert.rejects(
      subject.retrieveIeeePaper({
        page,
        browserContext: fakeContext([
          new FakeResponse("not a pdf", { status: 418, contentType: "text/html" }),
        ]),
        reference: "https://ieeexplore.ieee.org/document/11014597",
        workDir: root,
        credentialReader: async () => ({
          username: "synthetic-user",
          password: "synthetic-password",
        }),
      }),
      (error) => error?.phase === "attribute-release-required",
    );
    assert.equal(page.actions.some((action) => action[1] === "attribute-proceed"), false);
    assert.equal(page.actions.some((action) => action[1] === "attribute-reject"), false);
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("continues after the user completes Guangxi University attribute release", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-attribute-return-"));
  try {
    const page = new FakePage({ requireAttributeRelease: true, attributeReleaseProceeds: true });
    const result = await subject.retrieveIeeePaper({
      page,
      browserContext: fakeContext([
        new FakeResponse("not a pdf", { status: 418, contentType: "text/html" }),
        new FakeResponse("%PDF-1.7\nauthorized after attribute release\n"),
      ]),
      reference: "https://ieeexplore.ieee.org/document/11014597",
      workDir: root,
      credentialReader: async () => ({
        username: "synthetic-user",
        password: "synthetic-password",
      }),
    });
    assert.equal(result.status, "downloaded");
    assert.equal(
      page.navigations.includes("https://ds.carsi.edu.cn/resource/gotoResource.php?id=resource:6"),
      true,
    );
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("accepts Guangxi University attribute release only when explicitly enabled", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-attribute-accept-"));
  try {
    const page = new FakePage({ requireAttributeRelease: true, attributeReleaseProceeds: true });
    const result = await subject.retrieveIeeePaper({
      page,
      browserContext: fakeContext([
        new FakeResponse("not a pdf", { status: 418, contentType: "text/html" }),
        new FakeResponse("%PDF-1.7\nauthorized after explicit attribute acceptance\n"),
      ]),
      reference: "https://ieeexplore.ieee.org/document/11014597",
      workDir: root,
      acceptAttributeRelease: true,
      credentialReader: async () => ({
        username: "synthetic-user",
        password: "synthetic-password",
      }),
    });
    assert.equal(result.status, "downloaded");
    assert.equal(page.actions.some((action) => action[1] === "attribute-proceed"), true);
    assert.equal(page.actions.some((action) => action[1] === "attribute-reject"), false);
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("supports an IdP continuation page with one configured proceed control", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-single-proceed-"));
  try {
    const page = new FakePage({
      requireAttributeRelease: true,
      attributeReleaseProceeds: true,
      attributeRejectMissing: true,
    });
    const result = await subject.retrieveIeeePaper({
      page,
      browserContext: fakeContext([
        new FakeResponse("denied", { status: 403, contentType: "text/html" }),
        new FakeResponse("%PDF-1.7\nsingle proceed\n"),
      ]),
      reference: "https://ieeexplore.ieee.org/document/11014597",
      workDir: root,
      acceptAttributeRelease: true,
      credentialReader: async () => ({ username: "user", password: "password" }),
    });
    assert.equal(result.status, "downloaded");
    assert.equal(page.actions.some((action) => action[1] === "attribute-proceed"), true);
    assert.equal(page.actions.some((action) => action[1] === "attribute-reject"), false);
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("waits for delayed attribute-release controls before classifying the IdP page", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-delayed-attribute-controls-"));
  try {
    const page = new FakePage({
      requireAttributeRelease: true,
      delayedAttributeReleaseControls: true,
      attributeReleaseProceeds: true,
    });
    const result = await subject.retrieveIeeePaper({
      page,
      browserContext: fakeContext([
        new FakeResponse("denied", { status: 403, contentType: "text/html" }),
        new FakeResponse("%PDF-1.7\ndelayed attribute controls\n"),
      ]),
      reference: "https://ieeexplore.ieee.org/document/11014597",
      workDir: root,
      acceptAttributeRelease: true,
      credentialReader: async () => ({ username: "user", password: "password" }),
    });
    assert.equal(result.status, "downloaded");
    assert.equal(page.actions.some((action) => action[1] === "attribute-proceed"), true);
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("handles attribute release immediately after institutional login", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-login-attribute-release-"));
  try {
    const page = new FakePage({
      attributeReleaseAfterLogin: true,
    });
    const result = await subject.retrieveIeeePaper({
      page,
      browserContext: fakeContext([
        new FakeResponse("denied", { status: 403, contentType: "text/html" }),
        new FakeResponse("%PDF-1.7\nauthorized after login attribute release\n"),
      ]),
      reference: "https://ieeexplore.ieee.org/document/11014597",
      workDir: root,
      acceptAttributeRelease: true,
      credentialReader: async () => ({ username: "user", password: "password" }),
    });
    assert.equal(result.status, "downloaded");
    assert.equal(page.actions.some((action) => action[1] === "attribute-proceed"), true);
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("reuses a live Guangxi University IdP session without reading credentials again", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-idp-session-"));
  let credentialReads = 0;
  try {
    const page = new FakePage({ idpSessionAutoRedirect: true });
    const result = await subject.retrieveIeeePaper({
      page,
      browserContext: fakeContext([
        new FakeResponse("not a pdf", { status: 418, contentType: "text/html" }),
        new FakeResponse("%PDF-1.7\nauthorized with existing IdP session\n"),
      ]),
      reference: "https://ieeexplore.ieee.org/document/11014597",
      workDir: root,
      credentialReader: async () => {
        credentialReads += 1;
        return { username: "synthetic-user", password: "synthetic-password" };
      },
    });
    assert.equal(result.status, "downloaded");
    assert.equal(credentialReads, 0);
    assert.equal(
      page.navigations.includes("https://ds.carsi.edu.cn/resource/gotoResource.php?id=resource:6"),
      true,
    );
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("treats an IEEE denied redirect as the signal to authenticate instead of accepting unrelated iframes", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-denied-"));
  let credentialReads = 0;
  try {
    const browserContext = fakeContext([new FakeResponse("%PDF-1.7\nauthorized after denied\n")]);
    const result = await subject.retrieveIeeePaper({
      page: new FakePage({ denyFirstStamp: true }),
      browserContext,
      reference: "https://ieeexplore.ieee.org/document/11014597",
      workDir: root,
      credentialReader: async () => {
        credentialReads += 1;
        return { username: "synthetic-user", password: "synthetic-password" };
      },
    });
    assert.equal(result.status, "downloaded");
    assert.equal(credentialReads, 1);
    assert.equal(browserContext.request.calls.length, 1);
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("waits for the exact CARSI institution suggestion instead of counting immediately", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-carsi-wait-"));
  try {
    const result = await subject.retrieveIeeePaper({
      page: new FakePage({ institutionInitiallyReady: false }),
      browserContext: fakeContext([
        new FakeResponse("not a pdf", { status: 418, contentType: "text/html" }),
        new FakeResponse("%PDF-1.7\nauthorized\n"),
      ]),
      reference: "https://ieeexplore.ieee.org/document/11014597",
      workDir: root,
      credentialReader: async () => ({ username: "synthetic-user", password: "synthetic-password" }),
    });
    assert.equal(result.status, "downloaded");
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("waits for CARSI discovery to redirect before enforcing the credential host gate", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-carsi-redirect-"));
  try {
    const result = await subject.retrieveIeeePaper({
      page: new FakePage({ deferCarsiRedirect: true }),
      browserContext: fakeContext([
        new FakeResponse("not a pdf", { status: 418, contentType: "text/html" }),
        new FakeResponse("%PDF-1.7\nauthorized\n"),
      ]),
      reference: "https://ieeexplore.ieee.org/document/11014597",
      workDir: root,
      credentialReader: async () => ({ username: "synthetic-user", password: "synthetic-password" }),
    });
    assert.equal(result.status, "downloaded");
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("rechecks IEEE without reading credentials when CARSI discovery keeps an existing session", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-carsi-session-"));
  let credentialReads = 0;
  try {
    const result = await subject.retrieveIeeePaper({
      page: new FakePage({ stayOnCarsi: true }),
      browserContext: fakeContext([
        new FakeResponse("not a pdf", { status: 418, contentType: "text/html" }),
        new FakeResponse("%PDF-1.7\nsession\n"),
      ]),
      reference: "https://ieeexplore.ieee.org/document/11014597",
      workDir: root,
      credentialReader: async () => {
        credentialReads += 1;
        return { username: "u", password: "p" };
      },
    });
    assert.equal(result.status, "downloaded");
    assert.equal(credentialReads, 0);
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("stops before credential release when CARSI redirects to an unexpected host", async () => {
  assert.equal(typeof subject.retrieveIeeePaper, "function");
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-host-"));
  let credentialReads = 0;
  try {
    await assert.rejects(
      subject.retrieveIeeePaper({
        page: new FakePage({ redirectHost: "idp.gxu.edu.cn.evil.example" }),
        browserContext: fakeContext([
          new FakeResponse("not a pdf", { status: 418, contentType: "text/html" }),
        ]),
        reference: "https://ieeexplore.ieee.org/document/11014597",
        workDir: root,
        credentialReader: async () => {
          credentialReads += 1;
          return { username: "u", password: "p" };
        },
      }),
      (error) => error?.phase === "unexpected-auth-host",
    );
    assert.equal(credentialReads, 0);
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("launches a separate persistent Chrome profile and closes it after retrieval", async () => {
  assert.equal(typeof subject.runAutomatedRetrieval, "function");
  const root = await mkdtemp(path.join(os.tmpdir(), "ieee-playwright-profile-"));
  const profileDir = path.join(root, "profile");
  const page = new FakePage();
  const browserContext = {
    ...fakeContext([new FakeResponse("%PDF-1.7\nprofile\n")]),
    pages: () => [page],
    closeCalls: 0,
    async close() { this.closeCalls += 1; },
  };
  const chromium = {
    calls: [],
    async launchPersistentContext(dir, options) {
      this.calls.push({ dir, options });
      return browserContext;
    },
  };

  try {
    const result = await subject.runAutomatedRetrieval({
      chromium,
      reference: "https://ieeexplore.ieee.org/document/11014597",
      workDir: path.join(root, "work"),
      profileDir,
      testMode: true,
      credentialReader: async () => { throw new Error("credentials must not be read"); },
    });
    assert.equal(result.status, "downloaded");
    assert.equal(chromium.calls.length, 1);
    assert.equal(chromium.calls[0].dir, profileDir);
    assert.equal(chromium.calls[0].options.channel, "chrome");
    assert.equal(chromium.calls[0].options.acceptDownloads, true);
    assert.equal(chromium.calls[0].options.headless, false);
    assert.equal(browserContext.closeCalls, 1);
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("enforces dedicated production work, profile, and dependency paths", () => {
  assert.equal(typeof subject.assertAutomationPathBoundaries, "function");
  const localAppData = path.resolve("C:/Users/synthetic/AppData/Local");
  const repoRoot = path.resolve("C:/repo");
  const allowed = {
    repoRoot,
    workDir: path.join(repoRoot, "raw", "tmp", ".work", "run", "download"),
    profileDir: path.join(localAppData, "Codex", "browser-profiles", "retrieve-ieee-papers"),
    dependencyRoot: path.join(localAppData, "Codex", "deps", "retrieve-ieee-papers"),
    localAppData,
  };
  assert.doesNotThrow(() => subject.assertAutomationPathBoundaries(allowed));
  assert.throws(() => subject.assertAutomationPathBoundaries({ ...allowed, workDir: path.join(repoRoot, "raw", "sources") }));
  assert.throws(() => subject.assertAutomationPathBoundaries({ ...allowed, profileDir: path.join(localAppData, "Google", "Chrome", "User Data") }));
  assert.throws(() => subject.assertAutomationPathBoundaries({ ...allowed, dependencyRoot: path.join(repoRoot, "node_modules") }));
});
