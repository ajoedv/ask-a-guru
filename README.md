# ask-a-guru
A full-stack booking app for 1-to-1 creative sessions with email/Google auth and full booking CRUD.

---

![Am I responsive image](assets/readme/responsive-mockup.webp)

---

## Table of Contents
* [Live Demo](#live-demo)
* [Test User](#test-user)
* [Overview](#overview)
* [Agile Methodology](#agile-methodology)
* [User Experience (UX)](#user-experience-ux)
  * [Strategy / Site Goals](#strategy--site-goals)
  * [Scope / User Stories](#scope--user-stories)
  * [Structure / Design Choices](#structure--design-choices)
  * [Skeleton / Wireframes](#skeleton--wireframes)
  * [Surface](#surface)
  * [Accessibility](#accessibility)
* [Features](#features)
  * [Existing Features](#existing-features)
  * [Future Features](#future-features)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Known Issues](#known-issues)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

[Back To Top](#table-of-contents)

---

## Live Demo
[Click here to view the live app on Heroku](https://ask-a-guru-ef8ce16b4e6e.herokuapp.com/)

---

## Test User
- **Username:** askaguru.tester  
- **Email:** askaguru.tester@example.com  
- **Password:** AskAGuru_demo_P4!2025

---

## Overview
Ask a Guru is a focused full-stack booking app for 1-to-1 creative sessions. Users can browse sessions, choose a time slot, and manage bookings (create, edit, cancel) from a simple dashboard. Authentication supports both email/password and Google via **django-allauth**. The expert currently manages session offerings and bookings through **Django Admin**. The stack is **Django + PostgreSQL + Bootstrap**; the app is responsive, follows Agile/UX best practices, and is deployed on **Heroku** (static files via **WhiteNoise**).

---

## Agile Methodology
This project was planned and tracked using **GitHub Projects (Kanban)** with Epics and User Stories. Prioritisation followed the **MoSCoW** method (Must/Should/Could/Won’t). Issues include clear **acceptance criteria** and a concise **Definition of Done**.

- **Kanban board (project view):** https://github.com/users/ajoedv/projects/1/views/1  
  *(If the board is not publicly visible, screenshots are provided below as evidence.)*
- **All user stories & issues:** https://github.com/ajoedv/ask-a-guru/issues
- **Example Epic with full criteria (CRUD):** https://github.com/ajoedv/ask-a-guru/issues/4

**Workflow columns:** **No Status / To Do → In Progress → Done**. Items move right only when acceptance criteria are satisfied and the feature is verified on the deployed app.

<details>
<summary><strong>Kanban Board (project view)</strong></summary>

![Kanban Board](docs/agile/kanban-board.png)
</details>

<details>
<summary><strong>User Stories moved to Done (board view)</strong></summary>

![User Stories Done](docs/agile/user-stories-done.png)
</details>

<details>
<summary><strong>Issues closed (work completed)</strong></summary>

![Issues Closed](docs/agile/issues-closed.png)
</details>

<details>
<summary><strong>Epics overview (GitHub Projects)</strong></summary>

![Epics Overview](docs/agile/epics-overview.png)
</details>

<details>
<summary><strong>Example Epic (CRUD) — issue view</strong></summary>

![Epic Example CRUD](docs/agile/epic-example-crud.png)
</details>

<details>
<summary><strong>Milestones closed (100% complete)</strong></summary>

![Milestones Closed](docs/agile/milestones-closed.png)
</details>

<details>
<summary><strong>MoSCoW labels</strong></summary>

![MoSCoW Labels](docs/agile/labels-moscow.png)
</details>

[Back To Top](#table-of-contents)

---

## User Experience (UX)

### Strategy / Site Goals
- Simple, intuitive booking experience for users.  
- Efficient expert tools to create/manage sessions and bookings.  
- Accessibility, responsiveness, and clarity across devices.

### Scope / User Stories

#### Epics & User Stories – Ask a Guru Project 4

##### Epic 1: Authentication
**Goal:** Enable both users and the expert to log in securely. Regular users can register, log in, and manage bookings, while the expert has a dedicated login and access to a custom dashboard. All credentials are protected using Django’s built-in authentication and hashing system.  
**User Stories:**
- As an expert, I want to log in through a dedicated form and be redirected to my dashboard to manage sessions.
- As a user, I want to register an account so that I can book sessions.
- As a user, I want to log in and log out so that my information remains secure.
- As a developer, I want to store passwords securely using Django's built-in hashing system.
- As a developer, I want to protect sensitive keys by using environment variables and .env files.  
**MoSCoW Priority:** Must Have  
**Related to:** Django Auth, Security, Environment Configuration, Expert Dashboard

##### Epic 2: Session Booking System
**Goal:** Allow users to browse available creative sessions and book one with ease.  
**User Stories:**
- As an expert, I want to create, edit, and delete session offers so that I can manage the availability of my services.
- As a user, I want to view a list of available sessions so that I can choose the one I prefer.
- As a user, I want to view session details so that I understand what the session offers.
- As a user, I want to book a session so that I can receive creative support.  
**MoSCoW Priority:** Must Have  
**Related to:** Session Model, Booking Logic, UI Display, Expert Dashboard

##### Epic 3: User Dashboard
**Goal:** Provide each user with a personal dashboard where they can manage and track their bookings, and enable the expert (admin) to manage all user bookings through a dedicated expert dashboard.  
**User Stories:**
- As an expert, I want to view all user bookings from a frontend dashboard so that I can manage the session schedule.
- As an expert, I want to update or cancel user bookings from my dashboard to reflect real-time changes.
- As a user, I want to view my bookings so that I can track and manage them.
- As a user, I want to cancel a booking in case my schedule changes.
- As a user, I want to edit a booking so that I can update my selection if needed.  
**MoSCoW Priority:** Must Have  
**Related to:** User Profile, CRUD, Admin Dashboard, Session Management

##### Epic 4: CRUD Functionality
**Goal:** Ensure full frontend-based Create, Read, Update, and Delete operations for user bookings in a seamless and user-friendly way, and provide the expert with full control over all bookings through a dedicated dashboard.  
**User Stories:**
- As an expert, I want to view all booking details in a clear and organized format to make informed decisions.
- As a user, I want to create a booking from the session detail page.
- As a user, I want to view my current bookings so I can keep track of upcoming sessions.
- As a user, I want to update a booking from my dashboard.
- As a user, I want to cancel a booking in case my schedule changes.
- As a user, I want to permanently delete a booking so that it is removed from my dashboard.
- As a user, I want confirmation messages when I complete an action successfully.
- As a developer, I want to ensure that user input is validated to prevent form submission errors.  
**MoSCoW Priority:** Must Have  
**Related to:** Dashboard, Forms, Django Views, Validation, Expert Dashboard Controls

##### Epic 5: Frontend UI/UX Design
**Goal:** Design a clean, modern, and responsive interface using Bootstrap to enhance user experience.  
**User Stories:**
- As an expert, I want a clean and functional dashboard UI so that I can manage sessions easily.
- As a user, I want a simple and visually appealing layout so that I can use the platform easily.
- As a user, I want the interface to be responsive so I can use it on any device.
- As a user, I want intuitive navigation so I can find pages and features easily.
- As a user, I want readable text and accessible color contrasts so I can use the app comfortably.
- As a developer, I want to use Bootstrap components to speed up design and ensure responsiveness.  
**MoSCoW Priority:** Must Have  
**Related to:** Bootstrap, Layout, Mobile Responsiveness, Expert Dashboard

##### Epic 6: Deployment & Hosting
**Goal:** Deploy the application online to make it accessible to users at any time.  
**User Stories:**
- As a developer, I want to deploy the application to Heroku so that it is accessible online.
- As a user, I want the website to load quickly and be consistently available.
- As a developer, I want to hide the SECRET_KEY and database credentials before pushing to GitHub.
- As a developer, I want to configure the Procfile, requirements.txt, and allowed hosts properly for Heroku deployment.
- As a developer, I want to collect and serve static files correctly so that the frontend displays as expected after deployment.  
**MoSCoW Priority:** Must Have  
**Related to:** Heroku, GitHub, Environment Variables, Static Files, Deployment Config

##### Epic 7: Agile Planning & Workflow
**Goal:** Manage the development process using Agile methodology and GitHub Projects.  
**User Stories:**
- As a developer, I want to create wireframes for all pages before implementing both the frontend and backend, so that I can plan the layout, functionality, and user experience properly.
- As a developer, I want to manage all tasks using GitHub Projects so that I can plan and track my progress clearly.
- As a team member, I want to prioritize features using the MoSCoW method to focus on what matters most.
- As a developer, I want to break the project into Epics and User Stories so that each task has clear goals.
- As a developer, I want to organize tasks using columns like "To Do", "In Progress", and "Done" to monitor the workflow visually.
- As a developer, I want to update the status of each task regularly to stay aligned with my plan and timeline.  
**MoSCoW Priority:** Must Have  
**Related to:** GitHub Project Board, Workflow Organization, MoSCoW Method, Agile Methodology

##### Epic 8: Testing & Quality Assurance
**Goal:** Test the platform thoroughly and ensure a high-quality user experience across all devices, using manual testing methods.  
**User Stories:**
- As a user, I want to test each feature to ensure it works as expected.
- As a user, I want clear messages confirming successful actions like booking or cancellation.
- As a developer, I want to perform manual testing for all pages and actions.
- As a developer, I want to document my testing steps clearly in the README file.
- As a developer, I want to verify that the site looks good and works properly across different screen sizes.  
**MoSCoW Priority:** Must Have  
**Related to:** Quality Assurance, Manual Testing, Responsive Design, README

---

### Structure / Design Choices

**Site map & key flows**

![Site map & user flows](assets/readme/structure-sitemap.webp)

- **Browse:** Home → Sessions → Session Detail → Create Booking → My Bookings  
- **Auth (Email/Password):** Home → Sign In / Sign Up → My Bookings  
- **Google OAuth:** Sign In → Google OAuth → `/accounts/google/login/callback/` → My Bookings  
- **Sign Out:** My Bookings → Home  
- **Admin (optional):** Home → Django Admin (`/admin/`)  
- **404:** Broken/unknown URL → 404

**Information Architecture (IA)**  
- **Home** – value proposition + CTAs (browse/sign in)  
- **Sessions** – list with key info + link to details  
- **Session Detail** – description + booking action  
- **Sign In / Sign Up / Sign Out** – django-allauth + Google OAuth  
- **My Bookings (User Dashboard)** – list + edit/cancel  
- **Django Admin** – expert/admin management  
- **404** – custom not-found with link back to Home

**Data Model (high-level)**  
- **User** (Django User)  
- **Session** – title, description, duration, price (optional), availability  
- **Booking** – FK(User, Session), datetime, notes, status; validation blocks past/conflicting slots

**Defensive Design & Validation**  
- Server-side validation + clear inline errors  
- Past/cancelled bookings can’t be edited  
- Users manage **their own** bookings only  
- Bootstrap alerts for success/error  
- CSRF on all POST forms

**Responsiveness**  
Bootstrap grid/utilities; verified on mobile, tablet, and desktop.

---

## Skeleton / Wireframes
Below are the wireframes for the main pages of the "Ask a Guru" project (desktop/mobile).

<details>
<summary>Wireframes</summary>

### Home Page
![Home Page Desktop](documentation/wireframes/home-d.jpg)  
![Home Page Mobile](documentation/wireframes/home-m.jpg)
<br>

### Sign Up Page
![Sign Up Desktop](documentation/wireframes/signup-d.jpg)  
![Sign Up Mobile](documentation/wireframes/signup-m.jpg)
<br>

### Sign In Page
![Sign In Desktop](documentation/wireframes/signin-d.jpg)  
![Sign In Mobile](documentation/wireframes/signin-m.jpg)
<br>

### User Dashboard
![User Dashboard Desktop](documentation/wireframes/user-dashboard-d.jpg)  
![User Dashboard Mobile](documentation/wireframes/user-dashboard-m.jpg)
<br>

### Session Booking Page
![Booking Session Desktop](documentation/wireframes/booking-session-d.jpg)  
![Booking Session Mobile](documentation/wireframes/booking-session-m.jpg)
<br>

</details>

---

## Surface

**Colour Scheme**  
Modern, clean palette with white background, dark text, and subtle grays; green/red alerts for clear feedback.

| Color | Hex Code | Color Name       | Usage |
|------|----------|------------------|-------|
| ![White](documentation/colors/white.png) | #FFFFFF | White | Background |
| ![Black](documentation/colors/black.png) | #000000 | Black | Primary text & dark buttons |
| ![Light Gray](documentation/colors/light-gray.png) | #F8F9FA | Light Gray | Section backgrounds & card borders |
| ![Bootstrap Green](documentation/colors/green.png) | #198754 | Bootstrap Green | Success alerts |
| ![Bootstrap Red](documentation/colors/red.png) | #DC3545 | Bootstrap Red | Error/Delete alerts |
| ![Bootstrap Blue](documentation/colors/blue.png) | #0D6EFD | Bootstrap Blue | Links & primary buttons |

**Typography**  
**Roboto** 400/500/700 for readable, modern UI.

**Icons**  
**Bootstrap Icons** with appropriate `aria-label`s.

**Buttons**  
High-contrast logic: black-on-white, white-on-black.

**Feedback Colors**  
- Green (#198754) for success messages.  
- Red (#DC3545) for errors/deletions.

[Back To Top](#table-of-contents)

---

## Accessibility
- **Semantic HTML & landmarks**; logical heading order.  
- **Keyboard navigation** across all interactive elements; visible focus states.  
- **Color/contrast** meet readability; meaning isn’t conveyed by color alone.  
- **Alt text** for informative images; decorative images ignored by AT.  
- **Forms & errors** use inline messages near fields; clear button labels.  
- **Responsive text** and comfortable line lengths.  
- **No auto-playing media** or flashing content.

**Manual checks**: keyboard-only for sign in, browse, create/edit/cancel booking; focus order matches visual order.  
**Audit screenshots & results (Lighthouse / WAVE) are documented in [TESTING.md](TESTING.md).**

---

## Features

### Existing Features
<details>
<summary><strong>Home</strong></summary>

![Home](assets/readme/home.webp)
</details>

<details>
<summary><strong>Sessions list</strong></summary>

![Sessions](assets/readme/sessions.webp)
</details>

<details>
<summary><strong>Create booking</strong></summary>

![Create Booking](assets/readme/booking-create.webp)
</details>

<details>
<summary><strong>My Bookings (User Dashboard)</strong></summary>

![My Bookings](assets/readme/my-bookings.webp)
</details>

<details>
<summary><strong>Edit booking</strong></summary>

![Update Booking](assets/readme/booking-update.webp)
</details>

<details>
<summary><strong>Cancel booking</strong></summary>

![Cancel Booking](assets/readme/booking-cancel.webp)
</details>

<details>
<summary><strong>Sign Up (email/password)</strong></summary>

![Sign Up](assets/readme/signup.webp)
</details>

<details>
<summary><strong>Sign In (email/password)</strong></summary>

![Login](assets/readme/login.webp)
</details>

<details>
<summary><strong>Google Sign-In</strong></summary>

![Google Login](assets/readme/google-login.webp)
</details>

<details>
<summary><strong>Django Admin (expert/administration)</strong></summary>

![Admin](assets/readme/admin.webp)
</details>

<details>
<summary><strong>Custom 404</strong></summary>

![404](assets/readme/404.webp)
</details>

<details>
<summary><strong>Responsive views</strong></summary>

![Home on iPad](assets/readme/home-ipad.webp)  
![Home on Mobile](assets/readme/home-mobile.webp)
</details>

### Future Features
- Frontend **Expert Dashboard** (manage sessions & bookings without Django Admin).  
- Calendar view & improved time-slot picker.  
- Email notifications for booking confirmations/cancellations.  
- User profile page (avatar, preferences).

---

## Technologies Used

### Languages
- [HTML5](https://developer.mozilla.org/docs/Web/HTML)
- [CSS3](https://developer.mozilla.org/docs/Web/CSS)
- [JavaScript (ES6)](https://developer.mozilla.org/docs/Web/JavaScript)
- [Python 3](https://www.python.org/)

### Frameworks & Libraries
- [Django](https://www.djangoproject.com/) — Python web framework (MVC/MVT)
- [Bootstrap 5](https://getbootstrap.com/) — responsive UI components
- [django-allauth](https://django-allauth.readthedocs.io/) — authentication (email/password + Google OAuth)
- [Gunicorn](https://gunicorn.org/) — WSGI server for Django
- [WhiteNoise](https://whitenoise.readthedocs.io/) — serve static files on Heroku
- [psycopg2-binary](https://www.psycopg.org/docs/) — PostgreSQL adapter for Python

### Database & Hosting
- [PostgreSQL](https://www.postgresql.org/) — production database
- [Heroku](https://www.heroku.com/) — cloud hosting & deployment

### Tools
- [GitHub](https://github.com/) — repository hosting, Issues & Projects (Kanban)
- [VS Code](https://code.visualstudio.com/) — primary code editor
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) — debugging & performance checks
- [Adobe Photoshop](https://www.adobe.com/products/photoshop.html) — image editing, responsive mockups
- [Squoosh.app](https://squoosh.app/) — image compression

---

## Testing
Full testing (feature cases, responsiveness, accessibility, validators, and bug log) is documented in **[TESTING.md](TESTING.md)**, including step-by-step tables (Expected vs Actual) and screenshots (e.g., Lighthouse/WAVE, CRUD flows).

---

## Known Issues
- Expert/administrator management is currently via **Django Admin** (no custom expert dashboard UI yet).  
- Google login depends on provider credentials; if misconfigured, only email/password is available.

---


## Deployment

### Entity Relationship Diagram (ERD)
An Entity Relationship Diagram (ERD) is included to show how the database models relate to each other.

![ERD](docs/erd.png)

> ERD image path: `docs/erd.png`

---

### Heroku Deployment (Production)

This project is deployed to **Heroku** using **GitHub** integration and **Heroku Postgres**.

#### Prerequisites
- A **GitHub** account
- A **Heroku** account
- **Python 3.11.9** (matches `runtime.txt`)
- Required deployment files included in the repository root:
  - `Procfile` -> `web: gunicorn ask_a_guru.wsgi`
  - `runtime.txt` -> `python-3.11.9`
  - `requirements.txt`

#### Step-by-step deployment (Heroku Dashboard + GitHub)

1) **Create the Heroku App**
- Heroku Dashboard -> **New** -> **Create new app**
- Choose an app name and region, then create the app.

![Create Heroku app](docs/heroku-create-app.png)

2) **Add Heroku Postgres**
- App -> **Resources** -> Add-on: **Heroku Postgres**
- This automatically creates `DATABASE_URL`.

![Add Heroku Postgres](docs/heroku-add-postgres.png)

3) **Set Config Vars (Environment Variables)**
- App -> **Settings** -> **Reveal Config Vars**
- Add the required keys below.

**Important:** Never commit secret values to GitHub and do not write real secrets in this README.  
Only the *keys* are documented here; the *values* are stored privately in Heroku Config Vars.

Required:
- `SECRET_KEY` (private value stored in Heroku)
- `DEBUG` = `False`
- `ALLOWED_HOSTS` = `<your-app-name>.herokuapp.com`
- `DATABASE_URL` (auto-created by Heroku Postgres)

Optional (only if used by this project):
- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `CSRF_TRUSTED_ORIGINS` = `https://<your-app-name>.herokuapp.com` (only if a CSRF origin error occurs)

![Config Vars](docs/heroku-config-vars.png)

**Generating a SECRET_KEY securely (example command):**
```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

4) **Connect Heroku to GitHub**
- App -> **Deploy** tab
- Deployment method: **GitHub**
- Connect the repository: `ajoedv/ask-a-guru`
- Select branch: `main`

![Connect GitHub repo](docs/heroku-connect-github.png)

5) **Deploy**
- In the Deploy tab:
  - Manual deploy -> **Deploy Branch**
  - (Optional) Enable Automatic Deploys

![Deploy branch](docs/heroku-deploy-branch.png)

6) **Run migrations (Post-deploy)**
- App -> **More** -> **Run console**
- Run:
```bash
python manage.py migrate
```

![Run console migrate](docs/heroku-run-console-migrate.png)

(Optional) Create a superuser:
```bash
python manage.py createsuperuser
```

7) **Verify deployment**
- Open the deployed app URL
- Confirm authentication and core CRUD functionality operate correctly.

#### Troubleshooting
- Check logs in Heroku: **More** -> **View logs**
- Common issues:
  - Missing/incorrect Config Vars (`SECRET_KEY`, `ALLOWED_HOSTS`, `DATABASE_URL`)
  - `DEBUG` not set to `False`
  - Migrations not run after deployment
---

## Credits

### Code & Tutorials
The following resources helped shape the project. Code was adapted to fit this app’s requirements:
- Code Institute materials (Diploma in Software Development).
- Django walkthroughs & community snippets used for reference only (forms, views, messages, URL patterns).

### Documentation
- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [django-allauth Documentation](https://django-allauth.readthedocs.io/)
- [Heroku Dev Center](https://devcenter.heroku.com/)
- General search & troubleshooting via Google.
- ChatGPT (for documentation)

### UI, Icons & Fonts
- **Bootstrap** & **Bootstrap Icons** for UI components and icons.
- System font stack optimized for readability (no external web fonts).

### Media
- All UI screenshots, wireframes, and diagrams were created by the author for this project.
- If any stock images are later added, attributions will be listed here with source links and licenses.

### Inspiration & Community
- Stack Overflow / GitHub issues for targeted fixes (forms, CSRF, login flow).
- Code Institute community discussions and peers’ public READMEs for structure ideas.

## Acknowledgements
- My Code Institute mentor **Rory Patrickfor** timely feedback during development.
- Code Institute guidance and assessment criteria.
- Testers who tried the booking flows and reported notes.
- My family for their patience, encouragement, and constant support throughout the project.

[Back To Top](#table-of-contents)
