---
name: retrieve-ieee-papers
description: Use when researching IEEE literature and a selected IEEE paper needs authorized institutional full-text retrieval through a user-configured CARSI institution, PDF download, MinerU conversion, duplicate-safe repository naming, or local staging under raw/tmp.
---

# Retrieve IEEE Papers

Retrieve only papers already selected for the research task. Run one repository command to use the current user's configured CARSI access, download through an isolated persistent Chrome session, parse with MinerU, and leave the candidate under ignored `raw/tmp/`. Never promote it to `raw/sources/`.

## One-time secret setup

The encrypted store is `%LOCALAPPDATA%\Codex\secrets\retrieve-ieee-papers.clixml`. If it is missing or must be replaced, create the DPAPI payload inside the agent security context, then install only the ciphertext outside the repository:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/setup-secrets.ps1 `
  -Path raw/tmp/.work/retrieve-ieee-papers.provision.clixml -Force
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/install-secret-file.ps1 `
  -SourcePath raw/tmp/.work/retrieve-ieee-papers.provision.clixml -RepoRoot <repo-root> -Force
```

Use an interactive terminal. Supply the institution display name, exact CARSI option and IdP entity ID, form contract, exact institutional IdP hostname, exact post-login IEEE resource URL, institutional credential, and MinerU token. Credential and token values use non-echoing secure prompts. The installer may need OS approval to write LocalAppData; it copies only the already-encrypted payload and removes the ignored temporary copy. Never place a secret value in command arguments, normal output, scripts, logs, environment files, or repository files.

The downloader releases the institutional credential only when the current hostname exactly equals the encrypted profile's `CredentialHost`. Existing schema-v1 Guangxi University payloads are normalized in memory to the same profile contract, so they keep working without exposing or rewriting the credential. The MinerU stage injects its token only into the CLI child process.

## Normal path: one command

Run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/retrieve-paper.ps1 `
  -Reference <IEEE-URL-DOI-or-exact-title> -RepoRoot <repo-root>
```

The command performs the whole pipeline:

1. Resolve IEEE metadata and stop immediately if the paper already exists in `raw/sources/` or `raw/tmp/`.
2. Auto-install `playwright-core@1.61.1` under `%LOCALAPPDATA%\Codex\deps\retrieve-ieee-papers` on first use from the fixed official npm registry and integrity-pinned lockfile, with lifecycle scripts disabled.
3. Open and control a dedicated Chrome window with the isolated session under `%LOCALAPPDATA%\Codex\browser-profiles\retrieve-ieee-papers`; never attach to or inspect the user's normal Chrome profile. Routine login uses only the configured institution selectors, writes and verifies the configured CARSI entity ID before submitting discovery, and submits credentials at most once. By default, a configured SAML attribute-release page remains visible for the full `-BrowserTimeoutSeconds` window; if the user completes it, automation observes the IdP return and continues. Use `-AcceptAttributeRelease` only when the user explicitly authorizes automatic acceptance for the retrieval; the script never selects rejection.
4. Request the PDF through Playwright's browser-context request API, which shares the authorized session cookie jar without exporting cookies. Automatic redirects are disabled so request headers cannot be forwarded to another host. If the first response is not a direct PDF, enter the configured IEEE resource gateway first so its SAML return target survives institution selection and login. Re-enter that same gateway only after CARSI or an accepted attribute-release page returns without IEEE entitlement; never click a portal card. At most three gateway visits are allowed: initial discovery, post-login authorization, and one post-release/post-portal recovery. Require an exact return to `ieeexplore.ieee.org` before retrying the PDF; exhaustion is `institutional-return` with a sanitized transition trace.
5. Run `mineru-open-api` precision extraction with the protected token. The child process adds only the exact upload host `mineru.oss-cn-shanghai.aliyuncs.com` and result host `cdn-mineru.openxlab.org.cn` to `NO_PROXY/no_proxy`; signed URL query parameters are removed from all stored logs. If the precision result download from the exact result host fails with an explicit EOF/TLS error, run one token-free `flash-extract` fallback. Precision and flash write to separate directories, and only the successful directory reaches staging. Then atomically stage same-named PDF, Markdown, and `images/` under `raw/tmp/<safe-title>/`.

The final stdout is one JSON object. Report `directory` when its status is `staged`; report the existing path and stop when its status is `existing`. Exit code `75` means MinerU rate-limited the request; stop without retrying.

## MinerU relationship

`MinerU Document Extractor` is the agent-facing guidance skill. `mineru-open-api` is the authenticated precision CLI. The one-command path deliberately uses the CLI so routine retrieval needs no extra agent operations. Do not manually export `MINERU_TOKEN`.

If an exposed MinerU MCP is explicitly preferred, run the same command with `-DownloadOnly`, parse the returned `pdfPath` through MCP, then call `scripts/stage-paper.ps1`. This is an optional path, not the default.

## Diagnostics

Use `-DownloadOnly` only to isolate download failures or choose MinerU MCP manually. Routine runs remain one-command; do not click the automatically controlled Chrome window. A selector failure is reported by a named phase. A transient pre-authentication `chrome-error` navigation retries once. A stamp page without its PDF iframe waits at most 10 seconds before being treated as an entitlement signal. An `institutional-return` error includes only sanitized host/URL transitions and resource-visit count, making bounded recovery distinguishable from a stalled page.

## Hard stops

- Never echo, inspect, summarize, or log credentials, tokens, filled form values, cookies, local storage, or browser profiles.
- Never release credentials for a hostname other than the exact `CredentialHost` stored in the current encrypted institution profile. Change the profile through interactive setup; never broaden hostname matching in code.
- Submit credentials once. Stop on an invalid credential, CAPTCHA, OTP, safety interstitial, unexpected host, or missing entitlement.
- Never accept SAML attribute release unless the user explicitly authorizes it and the command carries `-AcceptAttributeRelease`. Never reject automatically. Without authorization, wait for the user's choice and stop with `attribute-release-required` after the bounded timeout.
- Never bypass publisher or institutional access controls and never bulk-download speculative search results.
- Never attach Playwright to the normal Chrome profile, enumerate its state, or export cookies. The dedicated profile is an opaque session store.
- Never publish partial MinerU output as a final bundle and never overwrite an existing candidate automatically.
- Never retain MinerU signed upload/download query parameters in stdout or stderr logs.
- Never write under `raw/sources/`; manual promotion belongs to the user.

## Page drift

For a named browser phase failure, read [references/ieee-flow.md](references/ieee-flow.md). Inspect only the failed page in the dedicated Chrome window. If the live page still matches the configured institution but the automation transition is wrong, patch `scripts/ieee-playwright.mjs`, update `scripts/tests/test-ieee-playwright.mjs`, and rerun the tests before retrying. If the institution's visible labels or exact hostname changed, replace the encrypted profile through interactive setup; do not add institution-specific selectors or broaden hostname matching in code.
