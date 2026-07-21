import assert from "node:assert/strict";
import { mkdtemp, readFile, rm } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import test from "node:test";

let subject = {};
try {
  subject = await import("../ieee-playwright.mjs");
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
    if (this.key === "iframe") return this.page.currentUrl.includes("/stamp/stamp.jsp") ? 1 : 0;
    if (this.key === "institution") return this.page.institutionReady ? 1 : 0;
    if (this.key === "username" && this.page.idpSessionAutoRedirect) {
      this.page.pendingRedirect = "https://ds.carsi.edu.cn/resource/resource.php";
      return 0;
    }
    if (this.key === "attribute-proceed" || this.key === "attribute-reject") {
      return this.page.currentUrl.includes("/idp/profile/SAML2/Redirect/SSO") ? 1 : 0;
    }
    return 1;
  }

  async waitFor() {
    if (this.key === "institution") this.page.institutionReady = true;
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
      } else if (this.page.deferCarsiRedirect) {
        this.page.pendingRedirect = `https://${this.page.redirectHost}/login`;
      } else {
        this.page.currentUrl = `https://${this.page.redirectHost}/login`;
      }
    } else if (this.key === "gxu-login") {
      this.page.authenticated = true;
      this.page.currentUrl = "https://ds.carsi.edu.cn/ds/index.html";
    }
  }
}

class FakePage {
  constructor({ redirectHost = "idp.gxu.edu.cn", denyFirstStamp = false, institutionInitiallyReady = true, evaluateFailures = 0, deferCarsiRedirect = false, stayOnCarsi = false, requireAttributeRelease = false, attributeReleaseProceeds = false, idpSessionAutoRedirect = false } = {}) {
    this.currentUrl = "about:blank";
    this.redirectHost = redirectHost;
    this.actions = [];
    this.school = "";
    this.username = "";
    this.password = "";
    this.authenticated = false;
    this.denyFirstStamp = denyFirstStamp;
    this.institutionReady = institutionInitiallyReady;
    this.evaluateFailures = evaluateFailures;
    this.deferCarsiRedirect = deferCarsiRedirect;
    this.stayOnCarsi = stayOnCarsi;
    this.requireAttributeRelease = requireAttributeRelease;
    this.attributeReleaseProceeds = attributeReleaseProceeds;
    this.idpSessionAutoRedirect = idpSessionAutoRedirect;
    this.pendingRedirect = "";
    this.navigations = [];
  }

  async goto(url) {
    this.navigations.push(url);
    if (url.includes("/stamp/stamp.jsp") && this.denyFirstStamp && !this.authenticated) {
      this.currentUrl = "https://ieeexplore.ieee.org/document/11014597?denied=";
    } else if (url === "https://ds.carsi.edu.cn/resource/gotoResource.php?id=resource:6") {
      if (this.requireAttributeRelease) {
        this.currentUrl = "https://idp.gxu.edu.cn/idp/profile/SAML2/Redirect/SSO?execution=e2s1";
        if (this.attributeReleaseProceeds) {
          this.pendingRedirect = "https://ieeexplore.ieee.org/Xplore/home.jsp";
        }
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
    if (selector === 'button[name="_eventId_proceed"]') return new FakeLocator(this, "attribute-proceed");
    if (selector === 'button[name="_eventId_AttributeReleaseRejected"]') return new FakeLocator(this, "attribute-reject");
    throw new Error(`Unexpected selector: ${selector}`);
  }

  getByPlaceholder() { return new FakeLocator(this, "school"); }
  getByLabel(name) { return new FakeLocator(this, name === "用户名" ? "username" : "password"); }
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

test("keeps reference classification, selectors, and exact credential host pinned", () => {
  assert.equal(subject.classifyPaperReference("https://ieeexplore.ieee.org/document/11014597").kind, "url");
  assert.equal(subject.classifyPaperReference("10.1109/TAP.2025.3571069").kind, "doi");
  assert.deepEqual(subject.classifyPaperReference("Exact title"), { kind: "title", value: "Exact title" });
  assert.equal(subject.isApprovedCredentialHost("IDP.GXU.EDU.CN"), true);
  assert.equal(subject.isApprovedCredentialHost("idp.gxu.edu.cn.evil.example"), false);
  assert.equal(subject.SELECTORS.carsiInstitution, "广西大学（GuangXi University）");
  assert.equal(subject.SELECTORS.pdfPrimaryHref, 'a.xpl-btn-pdf[href*="/stamp/stamp.jsp"]');
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
