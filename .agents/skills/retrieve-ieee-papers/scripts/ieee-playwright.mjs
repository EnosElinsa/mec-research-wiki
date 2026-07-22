import { execFile } from "node:child_process";
import { createRequire } from "node:module";
import { mkdir, open, rename, rm, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { promisify } from "node:util";

const execFileAsync = promisify(execFile);
const MODULE_DIR = path.dirname(fileURLToPath(import.meta.url));
const IEEE_HOST = "ieeexplore.ieee.org";
const CARSI_HOST = "ds.carsi.edu.cn";
const DNS_HOST = /^(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$/i;
const CONTROL_NAME = /^[A-Za-z0-9_-]+$/;
const MAX_RESOURCE_GATEWAY_VISITS = 3;

export const SELECTORS = Object.freeze({
  pdfHref: 'a[href*="/stamp/stamp.jsp"]',
  pdfPrimaryHref: 'a.xpl-btn-pdf[href*="/stamp/stamp.jsp"]',
  pdfFrame: 'iframe[src*="/stampPDF/getPDF.jsp"]',
});

export class IeeeFlowError extends Error {
  constructor(phase, message, details = {}) {
    super(message);
    this.name = "IeeeFlowError";
    this.phase = phase;
    this.details = details;
  }
}

export function classifyPaperReference(reference) {
  const value = String(reference ?? "").trim();
  if (!value) throw new TypeError("paper reference is required");
  if (/^https:\/\/ieeexplore\.ieee\.org\//i.test(value)) return { kind: "url", value };
  if (/^10\.\d{4,9}\/[\w.()/:;-]+$/i.test(value)) return { kind: "doi", value };
  return { kind: "title", value };
}

export function normalizeInstitutionProfile(payload = {}) {
  const required = [
    "organization",
    "carsiSchoolPlaceholder",
    "carsiSearchText",
    "carsiInstitution",
    "carsiLoginButtonName",
    "carsiEntityId",
    "credentialHost",
    "usernameLabel",
    "passwordLabel",
    "loginButtonName",
    "resourceAccessUrl",
  ];
  const profile = {};
  for (const name of required) {
    const value = String(payload[name] ?? "").trim();
    if (!value) throw new IeeeFlowError("credential-read", `Institution profile field is missing: ${name}.`);
    profile[name] = value;
  }
  profile.credentialHost = profile.credentialHost.toLowerCase();
  if (profile.credentialHost.endsWith(".") || !DNS_HOST.test(profile.credentialHost)) {
    throw new IeeeFlowError("credential-read", "Institution credential host must be one exact DNS hostname.");
  }
  let carsiEntity;
  try {
    carsiEntity = new URL(profile.carsiEntityId);
  } catch {
    throw new IeeeFlowError("credential-read", "CARSI entity ID must be a valid HTTPS URL.");
  }
  if (
    carsiEntity.protocol !== "https:"
    || carsiEntity.port
    || carsiEntity.username
    || carsiEntity.password
    || carsiEntity.hash
  ) {
    throw new IeeeFlowError(
      "credential-read",
      "CARSI entity ID must be an HTTPS URL without credentials, a custom port, or a fragment.",
    );
  }
  profile.carsiEntityId = carsiEntity.href;
  let resourceAccess;
  try {
    resourceAccess = new URL(profile.resourceAccessUrl);
  } catch {
    throw new IeeeFlowError("credential-read", "Institution resource access URL must be a valid HTTPS URL.");
  }
  if (
    resourceAccess.protocol !== "https:"
    || resourceAccess.hostname.toLowerCase() !== CARSI_HOST
    || resourceAccess.port
    || resourceAccess.username
    || resourceAccess.password
    || resourceAccess.hash
  ) {
    throw new IeeeFlowError(
      "credential-read",
      `Institution resource access URL must use the exact ${CARSI_HOST} HTTPS host without credentials, a custom port, or a fragment.`,
    );
  }
  profile.resourceAccessUrl = resourceAccess.href;
  profile.attributeReleaseTitle = String(payload.attributeReleaseTitle ?? "").trim();
  profile.attributeReleaseAcceptControlName = String(
    payload.attributeReleaseAcceptControlName ?? "",
  ).trim();
  profile.attributeReleaseRejectControlName = String(
    payload.attributeReleaseRejectControlName ?? "",
  ).trim();
  const controls = [profile.attributeReleaseAcceptControlName, profile.attributeReleaseRejectControlName];
  if (profile.attributeReleaseRejectControlName && !profile.attributeReleaseAcceptControlName) {
    throw new IeeeFlowError(
      "credential-read",
      "Institution attribute-release reject control requires an accept or continue control.",
    );
  }
  for (const controlName of controls) {
    if (controlName && !CONTROL_NAME.test(controlName)) {
      throw new IeeeFlowError(
        "credential-read",
        "Institution attribute-release control names may contain only letters, digits, underscores, and hyphens.",
      );
    }
  }
  return profile;
}

export function isApprovedCredentialHost(hostname, institutionProfile) {
  const value = String(hostname ?? "").trim().toLowerCase();
  if (!value || value.endsWith(".")) return false;
  return value === normalizeInstitutionProfile(institutionProfile).credentialHost;
}

function samePath(left, right) {
  const normalize = (value) => path.resolve(String(value)).replace(/[\\/]+$/, "").toLowerCase();
  return normalize(left) === normalize(right);
}

function isPathInside(child, parent) {
  const relative = path.relative(path.resolve(parent), path.resolve(child));
  return relative === "" || (!relative.startsWith("..") && !path.isAbsolute(relative));
}

export function assertAutomationPathBoundaries({
  repoRoot,
  workDir,
  profileDir,
  dependencyRoot,
  localAppData = process.env.LOCALAPPDATA,
  testMode = false,
}) {
  if (testMode === true) return;
  for (const [name, value] of Object.entries({ repoRoot, workDir, profileDir, dependencyRoot, localAppData })) {
    if (!String(value ?? "").trim()) {
      throw new IeeeFlowError("path-boundary", `${name} is required for production automation.`);
    }
  }

  const expectedWorkRoot = path.join(path.resolve(repoRoot), "raw", "tmp", ".work");
  const expectedProfileDir = path.join(path.resolve(localAppData), "Codex", "browser-profiles", "retrieve-ieee-papers");
  const expectedDependencyRoot = path.join(path.resolve(localAppData), "Codex", "deps", "retrieve-ieee-papers");
  if (!isPathInside(workDir, expectedWorkRoot)) {
    throw new IeeeFlowError("path-boundary", "The browser work directory must remain under raw/tmp/.work.");
  }
  if (!samePath(profileDir, expectedProfileDir)) {
    throw new IeeeFlowError("path-boundary", "A dedicated retrieve-ieee-papers Chrome profile is required.");
  }
  if (!samePath(dependencyRoot, expectedDependencyRoot)) {
    throw new IeeeFlowError("path-boundary", "Playwright dependencies must remain in the dedicated LocalAppData directory.");
  }
}

function hostnameOf(value, phase) {
  try {
    return new URL(value).hostname.toLowerCase();
  } catch {
    throw new IeeeFlowError(phase, "The browser returned an invalid URL.");
  }
}

export function sanitizeTransitionUrl(value) {
  let url;
  try {
    url = new URL(value);
  } catch {
    throw new IeeeFlowError("transition-log", "The browser returned an invalid transition URL.");
  }
  const keys = [...new Set(url.searchParams.keys())];
  const query = keys.length
    ? `?${keys.map((key) => `${encodeURIComponent(key)}=[redacted]`).join("&")}`
    : "";
  return `${url.origin}${url.pathname}${query}`;
}

async function uniqueLocator(locator, phase, description) {
  const count = await locator.count();
  if (count !== 1) {
    throw new IeeeFlowError(
      phase,
      `${description} must resolve to exactly one element; found ${count}.`,
      { count },
    );
  }
  return locator;
}

async function waitForDocument(page, timeoutMs) {
  try {
    await page.waitForLoadState("domcontentloaded", { timeout: timeoutMs });
  } catch {
    // URL, hostname, and selector checks below remain authoritative.
  }
}

function isTransientChromeNavigation(error, page) {
  const message = String(error?.message ?? error);
  const currentUrl = String(page.url?.() ?? "");
  return currentUrl.startsWith("chrome-error://chromewebdata/")
    || /net::ERR_(?:ABORTED|FAILED|CONNECTION_RESET)/i.test(message);
}

async function navigateWithTransientRetry(page, targetUrl, timeoutMs, phase) {
  for (let attempt = 1; attempt <= 2; attempt += 1) {
    try {
      await page.goto(targetUrl, { waitUntil: "domcontentloaded", timeout: timeoutMs });
      return;
    } catch (error) {
      if (attempt === 1 && isTransientChromeNavigation(error, page)) continue;
      throw new IeeeFlowError(
        phase,
        `Browser navigation did not reach the requested page after ${attempt} attempt(s).`,
        { targetUrl, attempts: attempt },
      );
    }
  }
}

async function readPaperMetadata(page, timeoutMs) {
  const extract = () => {
    const content = (name) => document.querySelector(`meta[name="${name}"]`)?.getAttribute("content")?.trim() || "";
    const title = content("citation_title") || document.querySelector("h1")?.textContent?.trim() || "";
    const doiLabel = Array.from(document.querySelectorAll("main strong"))
      .slice(0, 64)
      .find((element) => element.textContent?.trim() === "DOI:");
    const doiHref = doiLabel?.nextElementSibling?.getAttribute?.("href") || "";
    const doi = content("citation_doi") || content("DC.Identifier") || doiHref.replace(/^https:\/\/doi\.org\//i, "");
    const canonicalUrl = document.querySelector('link[rel="canonical"]')?.getAttribute("href") || location.href;
    return { title, doi, canonicalUrl, userAgent: navigator.userAgent };
  };

  let metadata = null;
  for (let attempt = 0; attempt < 10; attempt += 1) {
    try {
      metadata = await page.evaluate(extract);
      if (String(metadata?.title ?? "").trim()) break;
    } catch {
      metadata = null;
    }
    if (attempt === 9) break;
    if (hostnameOf(page.url(), "paper-metadata") !== IEEE_HOST) {
      throw new IeeeFlowError("paper-metadata", "IEEE metadata navigation left the expected host.");
    }
    await waitForDocument(page, timeoutMs);
    if (typeof page.waitForTimeout === "function") {
      await page.waitForTimeout(Math.min(500, timeoutMs));
    }
  }
  if (!String(metadata?.title ?? "").trim()) {
    let visibleTitle = "";
    try { visibleTitle = String(await page.title()).trim(); } catch {}
    const current = new URL(page.url());
    throw new IeeeFlowError(
      "paper-metadata",
      `IEEE paper title metadata is missing at ${current.pathname}${current.search}; page title: ${visibleTitle || "(empty)"}.`,
    );
  }

  const currentUrl = page.url();
  const canonicalCandidate = String(metadata.canonicalUrl ?? "").trim();
  const canonicalUrl = canonicalCandidate && hostnameOf(canonicalCandidate, "paper-metadata") === IEEE_HOST
    ? canonicalCandidate
    : currentUrl;
  return {
    title: String(metadata.title).trim(),
    doi: String(metadata.doi ?? "").trim(),
    url: canonicalUrl,
    userAgent: String(metadata.userAgent ?? "").trim(),
  };
}

async function resolvePaper(page, reference, timeoutMs) {
  if (reference.kind === "url") {
    await navigateWithTransientRetry(page, reference.value, timeoutMs, "paper-navigation");
  } else if (reference.kind === "doi") {
    await navigateWithTransientRetry(
      page,
      `https://doi.org/${reference.value}`,
      timeoutMs,
      "paper-navigation",
    );
  } else {
    const searchUrl = `https://${IEEE_HOST}/search/searchresult.jsp?queryText=${encodeURIComponent(reference.value)}`;
    await navigateWithTransientRetry(page, searchUrl, timeoutMs, "paper-navigation");
    const result = await uniqueLocator(
      page.getByRole("link", { name: reference.value, exact: true }),
      "title-search-result",
      "Exact IEEE title result",
    );
    const href = await result.getAttribute("href");
    if (!href) throw new IeeeFlowError("title-search-result", "The exact title result has no target URL.");
    const target = new URL(href, searchUrl);
    if (target.hostname.toLowerCase() !== IEEE_HOST) {
      throw new IeeeFlowError("title-search-result", "The exact title result points outside IEEE Xplore.");
    }
    await navigateWithTransientRetry(page, target.href, timeoutMs, "paper-navigation");
  }

  await waitForDocument(page, timeoutMs);
  const hostname = hostnameOf(page.url(), "resolve-paper");
  if (hostname !== IEEE_HOST) {
    throw new IeeeFlowError("resolve-paper", `Expected an IEEE Xplore page, received host ${hostname}.`, { hostname });
  }
  return readPaperMetadata(page, timeoutMs);
}

async function resolvePdfUrls(page, paperUrl, timeoutMs) {
  let pdfLink = page.locator(SELECTORS.pdfHref);
  const count = await pdfLink.count();
  if (count === 0) return null;
  if (count > 1) {
    const primary = page.locator(SELECTORS.pdfPrimaryHref);
    const primaryCount = await primary.count();
    if (primaryCount !== 1) {
      throw new IeeeFlowError(
        "pdf-link",
        `IEEE PDF action is ambiguous; found ${count} candidates and ${primaryCount} primary candidates.`,
        { count, primaryCount },
      );
    }
    pdfLink = primary;
  }

  const href = await pdfLink.getAttribute("href");
  if (!href) throw new IeeeFlowError("pdf-link", "The IEEE PDF action has no target URL.");
  const stampUrl = new URL(href, paperUrl);
  if (stampUrl.hostname.toLowerCase() !== IEEE_HOST) {
    throw new IeeeFlowError("pdf-link", "The IEEE PDF action points outside IEEE Xplore.");
  }

  await page.goto(stampUrl.href, { waitUntil: "domcontentloaded", timeout: timeoutMs });
  await waitForDocument(page, timeoutMs);
  const landedUrl = new URL(page.url());
  if (landedUrl.hostname.toLowerCase() !== IEEE_HOST) {
    throw new IeeeFlowError("pdf-frame", `IEEE PDF navigation left the expected host for ${landedUrl.hostname}.`);
  }
  if (!landedUrl.pathname.startsWith("/stamp/") || landedUrl.searchParams.has("denied")) {
    return null;
  }
  const frame = page.locator(SELECTORS.pdfFrame);
  if (typeof frame.waitFor === "function") {
    try {
      await frame.waitFor({ state: "attached", timeout: Math.min(timeoutMs, 10_000) });
    } catch {
      return null;
    }
  }
  const frameCount = await frame.count();
  if (frameCount === 0) return null;
  if (frameCount !== 1) {
    throw new IeeeFlowError(
      "pdf-frame",
      `IEEE PDF frame must resolve to exactly one element; found ${frameCount}.`,
      { count: frameCount },
    );
  }
  const src = await frame.getAttribute("src");
  if (!src) throw new IeeeFlowError("pdf-frame", "The IEEE PDF frame has no source URL.");
  const pdfUrl = new URL(src, stampUrl.href);
  if (pdfUrl.hostname.toLowerCase() !== IEEE_HOST) {
    throw new IeeeFlowError("pdf-frame", "The IEEE PDF frame points outside IEEE Xplore.");
  }
  return { stampUrl: stampUrl.href, pdfUrl: pdfUrl.href };
}

async function assertPdfFile(pdfPath) {
  let handle;
  try {
    handle = await open(pdfPath, "r");
    const header = Buffer.alloc(5);
    const { bytesRead } = await handle.read(header, 0, header.length, 0);
    if (bytesRead !== 5 || header.toString("ascii") !== "%PDF-") {
      throw new IeeeFlowError("download-validation", "The downloaded file is not a PDF.");
    }
  } catch (error) {
    if (error instanceof IeeeFlowError) throw error;
    throw new IeeeFlowError("download-validation", "The downloaded PDF could not be read.");
  } finally {
    await handle?.close();
  }
}

async function tryFetchPdf({ page, browserContext, paper, workDir, timeoutMs }) {
  await navigateWithTransientRetry(page, paper.url, timeoutMs, "paper-navigation");
  await waitForDocument(page, timeoutMs);
  const urls = await resolvePdfUrls(page, paper.url, timeoutMs);
  if (!urls) return null;

  const response = await browserContext.request.get(urls.pdfUrl, {
    failOnStatusCode: false,
    maxRedirects: 0,
    timeout: timeoutMs,
    headers: {
      accept: "application/pdf,application/octet-stream;q=0.9,*/*;q=0.8",
      referer: urls.stampUrl,
      ...(paper.userAgent ? { "user-agent": paper.userAgent } : {}),
    },
  });
  const bytes = await response.body();
  const isPdf = response.ok()
    && bytes.length >= 5
    && bytes.subarray(0, 5).toString("ascii") === "%PDF-";
  if (!isPdf) {
    return null;
  }

  await mkdir(workDir, { recursive: true });
  const finalPath = path.join(workDir, "paper.pdf");
  const partialPath = `${finalPath}.partial`;
  try {
    await writeFile(partialPath, bytes, { flag: "wx" });
    await assertPdfFile(partialPath);
    await rename(partialPath, finalPath);
  } catch (error) {
    await rm(partialPath, { force: true });
    throw error;
  }
  return finalPath;
}

export async function readInstitutionProfile({ secretPath = "" } = {}) {
  const bridge = path.join(MODULE_DIR, "read-institution-profile.ps1");
  const args = ["-NoProfile", "-ExecutionPolicy", "Bypass", "-File", bridge];
  if (secretPath) args.push("-SecretPath", secretPath);

  let stdout;
  try {
    ({ stdout } = await execFileAsync("powershell", args, {
      encoding: "utf8",
      windowsHide: true,
      maxBuffer: 64 * 1024,
    }));
  } catch {
    throw new IeeeFlowError("credential-read", "The encrypted institution profile could not be loaded.");
  }
  try {
    return normalizeInstitutionProfile(JSON.parse(stdout));
  } catch (error) {
    if (error instanceof IeeeFlowError) throw error;
    throw new IeeeFlowError("credential-read", "The institution profile bridge returned an invalid response.");
  }
}

export async function readCredentialForHost(
  hostname,
  { secretPath = "", institutionProfile } = {},
) {
  if (!isApprovedCredentialHost(hostname, institutionProfile)) {
    throw new IeeeFlowError("unexpected-auth-host", "Credential release denied for an unapproved hostname.", { hostname });
  }
  const bridge = path.join(MODULE_DIR, "read-browser-credential.ps1");
  const args = ["-NoProfile", "-ExecutionPolicy", "Bypass", "-File", bridge, "-ExpectedHost", hostname];
  if (secretPath) args.push("-SecretPath", secretPath);

  let stdout;
  try {
    ({ stdout } = await execFileAsync("powershell", args, {
      encoding: "utf8",
      windowsHide: true,
      maxBuffer: 64 * 1024,
    }));
  } catch {
    throw new IeeeFlowError("credential-read", "The encrypted institutional credential could not be loaded.");
  }
  try {
    const credential = JSON.parse(stdout);
    if (!String(credential.username ?? "") || !String(credential.password ?? "")) throw new Error("missing fields");
    return { username: String(credential.username), password: String(credential.password) };
  } catch {
    throw new IeeeFlowError("credential-read", "The credential bridge returned an invalid response.");
  }
}

export async function checkRepositoryDuplicate({ title, doi = "", repoRoot }) {
  const checker = path.join(MODULE_DIR, "check-paper-duplicate.ps1");
  const args = [
    "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", checker,
    "-Title", title, "-Doi", doi, "-RepoRoot", repoRoot,
  ];
  let stdout;
  try {
    ({ stdout } = await execFileAsync("powershell", args, {
      encoding: "utf8",
      windowsHide: true,
      maxBuffer: 64 * 1024,
    }));
  } catch {
    throw new IeeeFlowError("duplicate-check", "The repository duplicate check failed.");
  }
  try {
    const result = JSON.parse(stdout);
    if (!result || !["existing", "missing"].includes(result.status)) throw new Error("invalid status");
    return result;
  } catch {
    throw new IeeeFlowError("duplicate-check", "The repository duplicate check returned an invalid response.");
  }
}

async function authenticateThroughCarsi({
  page,
  credentialReader,
  institutionProfile,
  secretPath,
  timeoutMs,
  acceptAttributeRelease,
}) {
  let authHost = hostnameOf(page.url(), "unexpected-auth-host");
  if (authHost === IEEE_HOST) return;
  if (authHost === CARSI_HOST) {
    const schoolCandidate = page.getByPlaceholder(
      institutionProfile.carsiSchoolPlaceholder,
      { exact: true },
    );
    if (await schoolCandidate.count() === 0) return;
    const school = await uniqueLocator(
      schoolCandidate,
      "carsi-school",
      "CARSI institution search",
    );
    await school.fill(institutionProfile.carsiSearchText);
    const institutionCandidate = page.getByRole("option", {
      name: institutionProfile.carsiInstitution,
      exact: true,
    });
    if (typeof institutionCandidate.waitFor === "function") {
      await institutionCandidate.waitFor({ state: "visible", timeout: timeoutMs });
    }
    const institution = await uniqueLocator(
      institutionCandidate,
      "carsi-institution",
      `${institutionProfile.organization} CARSI option`,
    );
    await institution.click();
    const entityId = await uniqueLocator(
      page.locator('input[name="entityID"]'),
      "carsi-entity-id",
      "CARSI institution entity ID field",
    );
    if (typeof entityId.evaluate !== "function" || typeof entityId.inputValue !== "function") {
      throw new IeeeFlowError("carsi-entity-id", "CARSI entity ID field cannot be verified.");
    }
    await entityId.evaluate((element, value) => {
      element.value = value;
      element.dispatchEvent(new Event("input", { bubbles: true }));
      element.dispatchEvent(new Event("change", { bubbles: true }));
    }, institutionProfile.carsiEntityId);
    if (await entityId.inputValue() !== institutionProfile.carsiEntityId) {
      throw new IeeeFlowError("carsi-entity-id", "CARSI institution entity ID was not applied.");
    }
    const carsiLogin = await uniqueLocator(
      page.getByRole("button", { name: institutionProfile.carsiLoginButtonName, exact: true }),
      "carsi-login",
      "CARSI login button",
    );
    await carsiLogin.click();
    if (typeof page.waitForURL === "function") {
      try {
        await page.waitForURL(
          (url) => url.hostname.toLowerCase() !== CARSI_HOST,
          { timeout: Math.min(timeoutMs, 30_000) },
        );
      } catch {
        // A retained CARSI page may represent an existing session; the resource is re-entered once.
      }
    }
    await waitForDocument(page, timeoutMs);
    authHost = hostnameOf(page.url(), "unexpected-auth-host");
  }
  if (authHost === CARSI_HOST) return;
  if (!isApprovedCredentialHost(authHost, institutionProfile)) {
    throw new IeeeFlowError(
      "unexpected-auth-host",
      `CARSI redirected to unapproved authentication host ${authHost}.`,
      { hostname: authHost },
    );
  }

  const usernameCandidate = page.getByLabel(institutionProfile.usernameLabel, { exact: true });
  if (await usernameCandidate.count() === 0 && typeof page.waitForURL === "function") {
    try {
      await page.waitForURL(
        (url) => url.hostname.toLowerCase() !== institutionProfile.credentialHost,
        { timeout: timeoutMs },
      );
      await waitForDocument(page, timeoutMs);
    } catch {
      // The selector check below reports page drift if the IdP does not reuse its live session.
    }
    if (!isApprovedCredentialHost(hostnameOf(page.url(), "authentication-result"), institutionProfile)) return;
    if (await usernameCandidate.count() === 0) {
      const handledRelease = await handleConfiguredAttributeRelease({
        page,
        institutionProfile,
        acceptAttributeRelease,
        timeoutMs,
      });
      if (
        handledRelease
        && !isApprovedCredentialHost(
          hostnameOf(page.url(), "authentication-result"),
          institutionProfile,
        )
      ) return;
      throw new IeeeFlowError(
        "authentication-not-complete",
        "The institutional page exposed neither the configured login form nor a completed session return.",
        { requiresUserAction: true },
      );
    }
  }

  const credential = await credentialReader(authHost, { secretPath, institutionProfile });
  try {
    const username = await uniqueLocator(
      usernameCandidate,
      "institution-username",
      `${institutionProfile.organization} username field`,
    );
    const password = await uniqueLocator(
      page.getByLabel(institutionProfile.passwordLabel, { exact: true }),
      "institution-password",
      `${institutionProfile.organization} password field`,
    );
    const login = await uniqueLocator(
      page.getByRole("button", { name: institutionProfile.loginButtonName, exact: true }),
      "institution-login",
      `${institutionProfile.organization} login button`,
    );
    await username.fill(credential.username);
    await password.fill(credential.password);
    await login.click();
    if (typeof page.waitForURL === "function") {
      try {
        await page.waitForURL(
          (url) => url.hostname.toLowerCase() !== institutionProfile.credentialHost,
          { timeout: timeoutMs },
        );
      } catch {
        // The explicit hostname check below reports the bounded authentication stop.
      }
    }
    await waitForDocument(page, timeoutMs);
  } finally {
    credential.username = null;
    credential.password = null;
  }

  if (isApprovedCredentialHost(hostnameOf(page.url(), "authentication-result"), institutionProfile)) {
    const handledRelease = await handleConfiguredAttributeRelease({
      page,
      institutionProfile,
      acceptAttributeRelease,
      timeoutMs,
    });
    if (
      handledRelease
      && !isApprovedCredentialHost(
        hostnameOf(page.url(), "authentication-result"),
        institutionProfile,
      )
    ) return;
    throw new IeeeFlowError(
      "authentication-not-complete",
      "Institutional login did not complete; the visible page may require CAPTCHA or OTP, or the credential may be invalid.",
      { requiresUserAction: true },
    );
  }
}

async function handleConfiguredAttributeRelease({
  page,
  institutionProfile,
  acceptAttributeRelease,
  timeoutMs,
}) {
  if (!institutionProfile.attributeReleaseAcceptControlName) return false;
  if (!isApprovedCredentialHost(hostnameOf(page.url(), "attribute-release"), institutionProfile)) {
    return false;
  }
  if (institutionProfile.attributeReleaseTitle && typeof page.title === "function") {
    const title = await page.title();
    if (title !== institutionProfile.attributeReleaseTitle) return false;
  }

  const proceed = page.locator(
    `button[name="${institutionProfile.attributeReleaseAcceptControlName}"]`,
  );
  const reject = institutionProfile.attributeReleaseRejectControlName
    ? page.locator(`button[name="${institutionProfile.attributeReleaseRejectControlName}"]`)
    : null;
  let [proceedCount, rejectCount] = await Promise.all([
    proceed.count(),
    reject ? reject.count() : Promise.resolve(0),
  ]);
  if (proceedCount === 0 && rejectCount === 0 && typeof proceed.waitFor === "function") {
    try {
      await proceed.waitFor({ state: "visible", timeout: Math.min(timeoutMs, 10_000) });
    } catch {
      // The IdP may auto-return without rendering an attribute-release control.
    }
    [proceedCount, rejectCount] = await Promise.all([
      proceed.count(),
      reject ? reject.count() : Promise.resolve(0),
    ]);
  }
  if (proceedCount === 0 && rejectCount === 0) {
    if (typeof page.waitForURL === "function") {
      try {
        await page.waitForURL(
          (url) => url.hostname.toLowerCase() !== institutionProfile.credentialHost,
          { timeout: Math.min(timeoutMs, 30_000) },
        );
      } catch {
        // The caller reports the still-visible, unclassified institutional page.
      }
    }
    await waitForDocument(page, timeoutMs);
    return !isApprovedCredentialHost(
      hostnameOf(page.url(), "attribute-release"),
      institutionProfile,
    );
  }
  if (proceedCount !== 1 || rejectCount > 1) {
    throw new IeeeFlowError(
      "attribute-release-controls",
      "The configured institutional continuation page did not expose exactly one accept/continue control and at most one reject control.",
      { requiresUserAction: true },
    );
  }
  if (acceptAttributeRelease) await proceed.click();
  if (typeof page.waitForURL === "function") {
    try {
      await page.waitForURL(
        (url) => url.hostname.toLowerCase() !== institutionProfile.credentialHost,
        { timeout: timeoutMs },
      );
    } catch {
      // The exact host check below distinguishes a completed visible action from a bounded pause.
    }
  }
  await waitForDocument(page, timeoutMs);
  if (isApprovedCredentialHost(hostnameOf(page.url(), "attribute-release"), institutionProfile)) {
    throw new IeeeFlowError(
      "attribute-release-required",
      "Institutional attribute release requires visible user action or explicit authorization.",
      { requiresUserAction: true },
    );
  }
  return true;
}

async function authorizeIeeeThroughCarsi({
  page,
  institutionProfile,
  timeoutMs,
  acceptAttributeRelease = false,
  maxVisits = MAX_RESOURCE_GATEWAY_VISITS,
  startingVisit = 0,
  initialTransitions = [],
}) {
  const transitions = [...initialTransitions];
  for (let attempt = 1; attempt <= maxVisits; attempt += 1) {
    const visit = startingVisit + attempt;
    await page.goto(institutionProfile.resourceAccessUrl, {
      waitUntil: "domcontentloaded",
      timeout: timeoutMs,
    });
    await waitForDocument(page, timeoutMs);

    let currentHost = hostnameOf(page.url(), "carsi-ieee-resource");
    transitions.push({ visit, host: currentHost, url: sanitizeTransitionUrl(page.url()) });
    if (currentHost === IEEE_HOST) return;

    if (isApprovedCredentialHost(currentHost, institutionProfile)) {
      const handledRelease = await handleConfiguredAttributeRelease({
        page,
        institutionProfile,
        acceptAttributeRelease,
        timeoutMs,
      });
      if (!handledRelease) {
        throw new IeeeFlowError(
          "authentication-not-complete",
          "The institutional page exposed neither the configured attribute-release state nor a completed return.",
          { hostname: currentHost, requiresUserAction: true, transitions },
        );
      }
      currentHost = hostnameOf(page.url(), "institutional-return");
      transitions.push({
        visit,
        host: currentHost,
        url: sanitizeTransitionUrl(page.url()),
        after: "attribute-release",
      });
      if (currentHost === IEEE_HOST) return;
    }

    if (currentHost === CARSI_HOST && attempt < maxVisits) {
      continue;
    }
    if (currentHost !== CARSI_HOST) {
      throw new IeeeFlowError(
        "unexpected-auth-host",
        `The institutional return reached unexpected host ${currentHost}.`,
        { hostname: currentHost, transitions },
      );
    }
  }

  const currentHost = hostnameOf(page.url(), "institutional-return");
  throw new IeeeFlowError(
    "institutional-return",
    `CARSI did not return to IEEE Xplore after ${startingVisit + maxVisits} configured resource visits; received host ${currentHost}.`,
    { hostname: currentHost, resourceVisits: startingVisit + maxVisits, transitions },
  );
}

export async function retrieveIeeePaper(options) {
  if (!options?.page || !options?.browserContext?.request) {
    throw new TypeError("page and browserContext are required");
  }
  const workDir = path.resolve(String(options.workDir ?? ""));
  if (!String(options.workDir ?? "").trim()) throw new TypeError("workDir is required");
  const timeoutMs = Number(options.timeoutMs ?? 45_000);
  const credentialReader = options.credentialReader ?? readCredentialForHost;
  const profileReader = options.profileReader ?? readInstitutionProfile;
  const duplicateChecker = options.duplicateChecker ?? checkRepositoryDuplicate;
  const repoRoot = options.repoRoot ? path.resolve(String(options.repoRoot)) : "";
  const secretPath = options.secretPath ? path.resolve(String(options.secretPath)) : "";
  await mkdir(workDir, { recursive: true });

  const paper = await resolvePaper(options.page, classifyPaperReference(options.reference), timeoutMs);
  if (repoRoot) {
    const duplicate = await duplicateChecker({ title: paper.title, doi: paper.doi, repoRoot });
    if (duplicate.status === "existing") {
      return {
        status: "existing",
        title: paper.title,
        doi: paper.doi,
        url: paper.url,
        sourceRoot: duplicate.sourceRoot,
        path: duplicate.path,
      };
    }
  }

  const firstPdf = await tryFetchPdf({
    page: options.page,
    browserContext: options.browserContext,
    paper,
    workDir,
    timeoutMs,
  });
  if (firstPdf) {
    return { status: "downloaded", title: paper.title, doi: paper.doi, url: paper.url, pdfPath: firstPdf };
  }

  const institutionProfile = options.institutionProfile
    ? normalizeInstitutionProfile(options.institutionProfile)
    : await profileReader({ secretPath });

  const acceptAttributeRelease = options.acceptAttributeRelease === true
    || String(options.acceptAttributeRelease ?? "").toLowerCase() === "true";
  await navigateWithTransientRetry(
    options.page,
    institutionProfile.resourceAccessUrl,
    timeoutMs,
    "carsi-ieee-resource",
  );
  await waitForDocument(options.page, timeoutMs);
  const initialHost = hostnameOf(options.page.url(), "carsi-ieee-resource");
  const transitions = [{
    visit: 1,
    host: initialHost,
    url: sanitizeTransitionUrl(options.page.url()),
  }];
  if (initialHost !== IEEE_HOST) {
    await authenticateThroughCarsi({
      page: options.page,
      credentialReader,
      institutionProfile,
      secretPath,
      timeoutMs,
      acceptAttributeRelease,
    });
    const authenticatedHost = hostnameOf(options.page.url(), "authentication-result");
    if (authenticatedHost !== IEEE_HOST) {
      await authorizeIeeeThroughCarsi({
        page: options.page,
        institutionProfile,
        timeoutMs,
        acceptAttributeRelease,
        maxVisits: MAX_RESOURCE_GATEWAY_VISITS - 1,
        startingVisit: 1,
        initialTransitions: transitions,
      });
    }
  }
  const secondPdf = await tryFetchPdf({
    page: options.page,
    browserContext: options.browserContext,
    paper,
    workDir,
    timeoutMs,
  });
  if (!secondPdf) {
    throw new IeeeFlowError(
      "download-after-auth",
      "IEEE did not return a PDF after CARSI authentication; the item may not be covered by the subscription.",
    );
  }
  return { status: "downloaded", title: paper.title, doi: paper.doi, url: paper.url, pdfPath: secondPdf };
}

export async function runAutomatedRetrieval(options) {
  if (!options?.chromium || typeof options.chromium.launchPersistentContext !== "function") {
    throw new TypeError("a Playwright chromium implementation is required");
  }
  const profileDir = path.resolve(String(options.profileDir ?? ""));
  const workDir = path.resolve(String(options.workDir ?? ""));
  if (!String(options.profileDir ?? "").trim()) throw new TypeError("profileDir is required");
  if (!String(options.workDir ?? "").trim()) throw new TypeError("workDir is required");
  assertAutomationPathBoundaries({
    repoRoot: options.repoRoot,
    workDir,
    profileDir,
    dependencyRoot: options.dependencyRoot,
    localAppData: options.localAppData,
    testMode: options.testMode === true,
  });
  await mkdir(profileDir, { recursive: true });
  await mkdir(workDir, { recursive: true });

  const browserContext = await options.chromium.launchPersistentContext(profileDir, {
    channel: "chrome",
    headless: options.headless === true,
    acceptDownloads: true,
    downloadsPath: workDir,
  });
  try {
    const page = browserContext.pages()[0] ?? await browserContext.newPage();
    return await retrieveIeeePaper({ ...options, page, browserContext, workDir });
  } finally {
    await browserContext.close();
  }
}

export function loadPlaywrightChromium(dependencyRoot) {
  const require = createRequire(import.meta.url);
  const packagePath = path.join(path.resolve(dependencyRoot), "node_modules", "playwright-core");
  const playwright = require(packagePath);
  if (!playwright?.chromium) throw new Error("playwright-core does not expose chromium");
  return playwright.chromium;
}

function parseArgs(argv) {
  const options = {};
  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (!arg.startsWith("--") || index + 1 >= argv.length) throw new Error(`Invalid argument: ${arg}`);
    options[arg.slice(2).replace(/-([a-z])/g, (_, letter) => letter.toUpperCase())] = argv[index + 1];
    index += 1;
  }
  return options;
}

async function main() {
  const options = parseArgs(process.argv.slice(2));
  for (const required of ["reference", "workDir", "profileDir", "dependencyRoot"]) {
    if (!String(options[required] ?? "").trim()) throw new Error(`Missing --${required.replace(/[A-Z]/g, (c) => `-${c.toLowerCase()}`)}`);
  }
  const chromium = loadPlaywrightChromium(options.dependencyRoot);
  const result = await runAutomatedRetrieval({
    ...options,
    chromium,
    timeoutMs: options.timeoutMs ? Number(options.timeoutMs) : undefined,
  });
  process.stdout.write(`${JSON.stringify(result)}\n`);
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) {
  main().catch((error) => {
    const payload = {
      status: "error",
      phase: error instanceof IeeeFlowError ? error.phase : "automation",
      message: String(error?.message ?? error),
      ...(error instanceof IeeeFlowError && Object.keys(error.details).length
        ? { details: error.details }
        : {}),
    };
    process.stderr.write(`${JSON.stringify(payload)}\n`);
    process.exitCode = 1;
  });
}
