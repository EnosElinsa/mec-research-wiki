# IEEE/CARSI flow reference

Last live end-to-end verification: 2026-07-21. Generic profile and CARSI-portal recovery regression suite verified: 2026-07-22.

Live diagnostic verification on 2026-07-22 with IEEE document `8263143` reached the configured Guangxi University IdP and classified its current single `_eventId_proceed` page as `attribute-release-required` without clicking it. The hidden CARSI `entityID` was written and verified before the IdP redirect. Full PDF completion still requires either visible user completion within `-BrowserTimeoutSeconds` or explicit `-AcceptAttributeRelease` authorization.

End-to-end smoke: IEEE document `11588261`, DOI `10.1109/ICC59461.2026.11588261`; explicit `-AcceptAttributeRelease` authorization, automatic CARSI/IEEE return, PDF retrieval, MinerU precision conversion through the exact OSS/CDN proxy bypass, signed-URL log redaction, and `raw/tmp` staging completed.

Flow drift repaired 2026-07-22: institutional login or a resource-gateway visit can return to the CARSI application portal without establishing an IEEE session. The workflow now re-enters the configured IEEE gateway within a three-visit bound, without clicking a portal card, and records a sanitized transition trace if CARSI never returns to IEEE. CARSI institution discovery also verifies the configured hidden IdP entity ID before submitting, instead of trusting the visible typeahead selection alone.

This reference covers selector repair and exceptional recovery. The normal workflow belongs in `../SKILL.md`; the one-command script owns browser setup, credential gating, download, conversion, and staging.

## Configured authorized route

```text
selected IEEE URL, DOI, or exact title
  -> IEEE paper metadata
  -> repository duplicate preflight
  -> existing bundle: return its path and stop
  -> PDF unavailable without entitlement
  -> configured ResourceAccessUrl on ds.carsi.edu.cn (preserves the IEEE SAML return target)
  -> CARSI redirects to https://ds.carsi.edu.cn/login/index.html when institution selection is needed
  -> configured CARSI institution-search placeholder and search text
  -> exact configured institution option
  -> write and verify the configured CARSI IdP entity ID
  -> exact configured CARSI login button
  -> exact configured CredentialHost
  -> configured username field / password field / login button
  -> CARSI application resource session
  -> if CARSI portal returns: navigate to the same ResourceAccessUrl again; never click a portal card
  -> if the configured attribute-release controls appear: user acts by default; with explicit authorization, -AcceptAttributeRelease selects only the configured accept control
  -> SAML return to ieeexplore.ieee.org
  -> return to the selected IEEE paper
  -> unique link href containing /stamp/stamp.jsp
  -> iframe src containing /stampPDF/getPDF.jsp
  -> BrowserContext.request using the same authorized cookie jar
  -> validated local PDF path
```

The legacy schema-v1 profile maps to Guangxi University, entity ID `https://idp.gxu.edu.cn/idp/shibboleth`, credential host `idp.gxu.edu.cn`, and `https://ds.carsi.edu.cn/resource/gotoResource.php?id=resource:6`. New or changed institutions must be supplied through interactive setup rather than added to the MJS source.

IEEE's `Institutional Sign In` dialog and `Access Through Your Institution` action are a secondary discovery surface. During the last verification, SeamlessAccess did not return Guangxi University, so the direct CARSI route remains primary. Never fall back to IEEE personal-account credentials for this workflow.

## Pinned contracts

| Phase | Contract |
|---|---|
| IEEE target | Host must be `ieeexplore.ieee.org` |
| CARSI discovery | URL `https://ds.carsi.edu.cn/login/index.html` |
| Institution | Exact option, search text, IdP entity ID, and button names from the encrypted institution profile; verify the hidden `entityID` before submission |
| Credential release | Current host must exactly equal configured `CredentialHost`, case-insensitively, with no suffix or trailing dot |
| IEEE gateway | Enter the exact configured HTTPS `ResourceAccessUrl` before institution selection; allow at most three total visits for initial discovery, post-login authorization, and post-release/post-portal recovery; never click a portal card |
| Institutional continuation | On the exact IdP host, require exactly one configured accept/continue control and at most one configured reject control; support both single-button continuation and accept/reject pages; click only accept/continue and only with explicit `-AcceptAttributeRelease`; never click rejection |
| IEEE PDF | Use `a[href*="/stamp/stamp.jsp"]`; if responsive markup yields two actions, narrow to the unique `a.xpl-btn-pdf[href*="/stamp/stamp.jsp"]` |
| PDF response | Open the stamp page, require one iframe on `ieeexplore.ieee.org`, then request its src with `browserContext.request` and `maxRedirects: 0`; require a direct successful response with `%PDF-` bytes before writing |
| Browser profile | Use only `%LOCALAPPDATA%\Codex\browser-profiles\retrieve-ieee-papers`; never use the normal Chrome profile |
| Browser dependency | Use only integrity-pinned `playwright-core@1.61.1` under `%LOCALAPPDATA%\Codex\deps\retrieve-ieee-papers` |
| MinerU network | Append exact hosts `mineru.oss-cn-shanghai.aliyuncs.com` and `cdn-mineru.openxlab.org.cn` to both `NO_PROXY` and `no_proxy` in the CLI child only |
| MinerU logs | Replace the protected token and every HTTPS signed-URL query with `[REDACTED]` before writing stdout/stderr logs, including flash fallback output |
| MinerU output | Keep precision and flash outputs isolated; stage only the directory reported by the successful mode |
| Repository destination | Only ignored `raw/tmp/<safe-title>/` |

The browser adapter may navigate on IEEE, CARSI discovery, DOI resolution, and the configured IdP. Only the exact configured IdP host may receive the stored institutional credential.

## Named failures

| Phase/code | Response |
|---|---|
| `title-search-result` | Confirm the exact title and repair only the result locator if the live snapshot supports it. |
| `carsi-school`, `carsi-institution`, `carsi-entity-id`, `carsi-login` | Inspect a fresh CARSI snapshot and update the corresponding profile field or selector plus test fixture. |
| `unexpected-auth-host` | Stop before reading credentials. Show only the hostname and ask the user whether it should be approved. |
| `institution-username`, `institution-password`, `institution-login` | Compare the visible IdP labels with the encrypted profile without reading form values. Replace the profile interactively if its contract is stale. |
| `authentication-not-complete` | Hand the visible page to the user for CAPTCHA/OTP, or report a single failed credential submission. Do not resubmit automatically. |
| `attribute-release-required` | Keep the visible page available for the user to accept or reject attribute release when automatic acceptance was not explicitly authorized. |
| `institutional-return` | Report the sanitized transition trace after the bounded gateway visits return to CARSI; do not click a portal card or continue to PDF retrieval. |
| `pdf-link`, `pdf-frame` | Inspect the dedicated Chrome window for the failed run; repair the href or iframe selector only if a stable replacement is visible. |
| `download-after-auth` | Report that entitlement may not cover the item. Do not attempt a bypass. |
| `download-validation` | Treat the file as invalid and stop before MinerU. |
| `duplicate-check` | Repair the local PowerShell/runtime issue before authentication; do not skip the gate. |

## Selector repair procedure

1. Keep the selected paper URL and the last safe page.
2. Run `scripts/retrieve-paper.ps1` once and inspect the named failed phase in its dedicated Chrome window only.
3. Prefer, in order: stable data attribute, stable href, scoped role plus exact accessible name, scoped text, then CSS.
4. Confirm the candidate count is exactly one before interaction.
5. Change only `../scripts/ieee-playwright.mjs` and the matching test in `../scripts/tests/test-ieee-playwright.mjs`.
6. Run `node --test .agents/skills/retrieve-ieee-papers/scripts/tests/test-ieee-playwright.mjs`.
7. Retry from the selected IEEE page or CARSI discovery page, whichever is the last safe state.

Never use selector repair to accept a new authentication hostname, bypass CAPTCHA/OTP, inspect browser state stores, or loop a credential submission.
