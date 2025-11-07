# TESTING

## Table of Contents

- [1) Authentication](#1-authentication)
  - [Sign Up – before submit](#sign-up--before-submit)
  - [Sign Up – success redirect/alert](#sign-up--success-redirectalert)
  - [Login – success](#login--success)
  - [Logout – success](#logout--success)
  - [Navbar – logged-in state](#navbar--logged-in-state)
  - [Navbar – visitor state](#navbar--visitor-state)
  - [Protected page – redirect when not authenticated](#protected-page--redirect-when-not-authenticated)

- [2) CRUD — Bookings](#2-crud--bookings)
  - [Create – booking created (success alert)](#create--booking-created-success-alert)
  - [Read – dashboard lists bookings](#read--dashboard-lists-bookings)
  - [Update (future) – saved with success alert](#update-future--saved-with-success-alert)
  - [Delete (future) – removed with success alert](#delete-future--removed-with-success-alert)
  - [Guard (past) – edit/cancel blocked](#guard-past--editcancel-blocked)

- [3) UI & JS](#3-ui--js)
  - [Key links/buttons navigate correctly](#key-linksbuttons-navigate-correctly)
  - [Alerts – success/confirmation visible](#alerts--successconfirmation-visible)
  - [Console – no errors](#console--no-errors)

- [4) Responsive](#4-responsive)
  - [Mobile (~390–414px) – Home](#mobile-390414px--home)
  - [Desktop (≥1366px) – Home](#desktop-1366px--home)

- [5) Validators & Audits](#5-validators--audits)
  - [W3C HTML/CSS – no critical errors](#w3c-htmlcss--no-critical-errors)
  - [Python style (ruff) – all checks passed](#python-style-ruff--all-checks-passed)
  - [Lighthouse – Home summary](#lighthouse--home-summary)
  - [WAVE – Home (no critical a11y errors)](#wave--home-no-critical-a11y-errors)

- [6) Bugs & Fixes (Next iteration)](#6-bugs--fixes-next-iteration)

---

## 1) Authentication

<details>
<summary><strong>Sign Up – before submit</strong></summary>

![Sign Up (1)](assets/testing/auth-signup-1.webp)
</details>

**Steps:** Open `/accounts/signup/`.  
**Expected:** Registration form renders.  
**Actual:** Form visible and ready.

<details>
<summary><strong>Sign Up – success redirect/alert</strong></summary>

![Sign Up (2)](assets/testing/auth-signup-2.webp)
</details>

**Steps:** Fill fields → Submit.  
**Expected:** Account created → success alert + redirect.  
**Actual:** Created and redirected with alert.

<details>
<summary><strong>Login – success</strong></summary>

![Login](assets/testing/auth-login.webp)
</details>

**Steps:** Open `/accounts/login/` → enter valid creds → Submit.  
**Expected:** Logged in; navbar shows authenticated state.  
**Actual:** Login successful; navbar updated.

<details>
<summary><strong>Logout – success</strong></summary>

![Logout](assets/testing/auth-logout.webp)
</details>

**Steps:** Click “Sign out”.  
**Expected:** Logged out → success alert on public page.  
**Actual:** Works as expected.

<details>
<summary><strong>Navbar – logged-in state</strong></summary>

![Navbar (Logged-in)](assets/testing/auth-navbar-logged-in.webp)
</details>

**Steps:** Log in → view navbar.  
**Expected:** “My bookings / Sign out”.  
**Actual:** Correct links shown.

<details>
<summary><strong>Navbar – visitor state</strong></summary>

![Navbar (Visitor)](assets/testing/auth-navbar-visitor.webp)
</details>

**Steps:** Log out → view navbar.  
**Expected:** “Sign up / Sign in”.  
**Actual:** Correct visitor links shown.

<details>
<summary><strong>Protected page – redirect when not authenticated</strong></summary>

![Auth Protected](assets/testing/auth-protected.webp)
</details>

**Steps:** While logged out, open `/bookings/`.  
**Expected:** Redirect to login with `?next=/bookings/`.  
**Actual:** Redirect occurs as expected.

--- 

## 2) CRUD — Bookings

<details>
<summary><strong>Create – booking created (success alert)</strong></summary>

![CRUD Create](assets/testing/crud-create.webp)
</details>

**Steps:** Sessions → choose session → create booking.  
**Expected:** Success alert + booking listed.  
**Actual:** Created and listed.

<details>
<summary><strong>Read – dashboard lists bookings</strong></summary>

![CRUD Read (Dashboard)](assets/testing/crud-read-dashboard.webp)
</details>

**Steps:** Open `/bookings/`.  
**Expected:** Lists my bookings.  
**Actual:** Future bookings listed correctly.

<details>
<summary><strong>Update (future) – saved with success alert</strong></summary>

![CRUD Update (Future)](assets/testing/crud-update-future.webp)
</details>

**Steps:** Edit a future booking → save.  
**Expected:** Success alert; data updated.  
**Actual:** Updated; alert shown.

<details>
<summary><strong>Delete (future) – removed with success alert</strong></summary>

![CRUD Delete (Future)](assets/testing/crud-delete-future.webp)
</details>

**Steps:** Click “Cancel” → confirm.  
**Expected:** Success alert; booking removed.  
**Actual:** Removed and alert shown.

<details>
<summary><strong>Guard (past) – edit/cancel blocked</strong></summary>

![CRUD Guard (Past)](assets/testing/crud-guard-past.webp)
</details>

**Steps:** Try to edit/cancel a past booking.  
**Expected:** Actions prevented (disabled/validation).  
**Actual:** Prevented as designed.

---

## 3) UI & JS


<details>
<summary><strong>Key links/buttons navigate correctly</strong></summary>

![UI Links](assets/testing/ui-links.webp)
</details>

**Steps:** Click Home / Sessions / Book buttons.  
**Expected:** Navigate to correct routes without errors.  
**Actual:** Navigation works.

<details>
<summary><strong>Alerts – success/confirmation visible</strong></summary>

![UI Alerts](assets/testing/ui-alerts.webp)
</details>

**Steps:** Trigger create/update/delete.  
**Expected:** Bootstrap success alert, auto-dismiss.  
**Actual:** Alerts display and auto-close.

<details>
<summary><strong>Console – no errors</strong></summary>

![UI Console](assets/testing/ui-console.webp)
</details>

**Steps:** Open DevTools Console on Home; interact.  
**Expected:** No console errors.  
**Actual:** Console clean.

---

## 4) Responsive

<details>
<summary><strong>Mobile (~390–414px) – Home</strong></summary>

![Responsive Mobile](assets/testing/rsp-mobile.webp)
</details>

**Steps:** DevTools → iPhone 12/13 Pro preset → reload.  
**Expected:** No horizontal scroll; readable layout.  
**Actual:** OK.

<details>
<summary><strong>Desktop (≥1366px) – Home</strong></summary>

![Responsive Desktop](assets/testing/rsp-desktop.webp)
</details>

**Steps:** Resize to ≥1366px width.  
**Expected:** Grid expands; hero/cards align.  
**Actual:** OK.

---

## 5) Validators & Audits

<details>
<summary><strong>W3C HTML/CSS – no critical errors</strong></summary>

![W3C HTML/CSS](assets/testing/validator-html.webp)
</details>

**Steps:** Run Nu Checker on deployed Home.  
**Expected:** No critical errors (warnings acceptable).  
**Actual:** No errors; info notes only.

<details>
<summary><strong>Python style (ruff) – all checks passed</strong></summary>

![PEP8 / Ruff](assets/testing/validator-pep8.webp)
</details>

**Steps:** `ruff check . --exclude '.venv,venv,env,staticfiles,assets,**/migrations/**'`  
**Expected:** Pass with no critical findings.  
**Actual:** All checks passed.

<details>
<summary><strong>Lighthouse – Home summary</strong></summary>

![Lighthouse](assets/testing/audit-lighthouse-home.webp)
</details>

**Steps:** DevTools → Lighthouse → Analyze (Navigation).  
**Expected:** Good scores across categories.  
**Actual:** Perf ~98, A11y ~93, BP 100, SEO ~91.

<details>
<summary><strong>WAVE – Home (no critical a11y errors)</strong></summary>

![WAVE](assets/testing/audit-wave-home.webp)
</details>

**Steps:** WAVE on Home.  
**Expected:** No critical a11y errors.  
**Actual:** None; minor contrast/structure notes OK.

---
## 6) Bugs & Fixes (Next iteration)
- Harden direct-URL authorization for cross-user booking access.
