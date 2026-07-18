# IEEE/CARSI flow reference

Last live verification: 2026-07-18.

End-to-end smoke: IEEE document `11014597`, DOI `10.1109/TAP.2025.3571069`; automatic PDF retrieval, MinerU precision conversion through the exact CDN proxy bypass, and `raw/tmp` staging completed without user interaction.

This reference covers selector repair and exceptional recovery. The normal workflow belongs in `../SKILL.md`; the one-command script owns browser setup, credential gating, download, conversion, and staging.

## Current authorized route

```text
selected IEEE URL, DOI, or exact title
  -> IEEE paper metadata
  -> repository duplicate preflight
  -> existing bundle: return its path and stop
  -> PDF unavailable without entitlement
  -> https://ds.carsi.edu.cn/ds/index.html
  -> textbox 请输入高校/机构名称: type 广西大学 to trigger the live suggestion list
  -> option 广西大学（GuangXi University）
  -> button 登录
  -> exact host https://idp.gxu.edu.cn/
  -> textbox 用户名 / textbox 密码 / button 登录
  -> return to the selected IEEE paper
  -> unique link href containing /stamp/stamp.jsp
  -> iframe src containing /stampPDF/getPDF.jsp
  -> BrowserContext.request using the same authorized cookie jar
  -> validated local PDF path
```

Guangxi University Library currently recommends CARSI pre-authentication and lists IEEE IEL among its subscribed resources: <https://www.lib.gxu.edu.cn/dzzy/xwfw1.htm>.

IEEE's `Institutional Sign In` dialog and `Access Through Your Institution` action are a secondary discovery surface. During the last verification, SeamlessAccess did not return Guangxi University, so the direct CARSI route remains primary. Never fall back to IEEE personal-account credentials for this workflow.

## Pinned contracts

| Phase | Contract |
|---|---|
| IEEE target | Host must be `ieeexplore.ieee.org` |
| CARSI discovery | URL `https://ds.carsi.edu.cn/ds/index.html` |
| Institution | Exact visible option `广西大学（GuangXi University）` |
| Credential release | Host must equal `idp.gxu.edu.cn`, case-insensitively, with no suffix |
| IEEE PDF | Use `a[href*="/stamp/stamp.jsp"]`; if responsive markup yields two actions, narrow to the unique `a.xpl-btn-pdf[href*="/stamp/stamp.jsp"]` |
| PDF response | Open the stamp page, require one iframe on `ieeexplore.ieee.org`, then request its src with `browserContext.request` and `maxRedirects: 0`; require a direct successful response with `%PDF-` bytes before writing |
| Browser profile | Use only `%LOCALAPPDATA%\Codex\browser-profiles\retrieve-ieee-papers`; never use the normal Chrome profile |
| Browser dependency | Use only integrity-pinned `playwright-core@1.61.1` under `%LOCALAPPDATA%\Codex\deps\retrieve-ieee-papers` |
| MinerU CDN | Append exact host `cdn-mineru.openxlab.org.cn` to both `NO_PROXY` and `no_proxy` in the CLI child only |
| MinerU output | Keep precision and flash outputs isolated; stage only the directory reported by the successful mode |
| Repository destination | Only ignored `raw/tmp/<safe-title>/` |

The browser adapter may navigate on IEEE, CARSI discovery, DOI resolution, and the pinned GXU IdP. Only the last host may receive the stored institutional credential.

## Named failures

| Phase/code | Response |
|---|---|
| `title-search-result` | Confirm the exact title and repair only the result locator if the live snapshot supports it. |
| `carsi-school`, `carsi-institution`, `carsi-login` | Inspect a fresh CARSI snapshot and update the corresponding selector plus test fixture. |
| `unexpected-auth-host` | Stop before reading credentials. Show only the hostname and ask the user whether it should be approved. |
| `gxu-username`, `gxu-password`, `gxu-login` | Inspect the current IdP snapshot without reading form values; update one selector and its test. |
| `authentication-not-complete` | Hand the visible page to the user for CAPTCHA/OTP, or report a single failed credential submission. Do not resubmit automatically. |
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
