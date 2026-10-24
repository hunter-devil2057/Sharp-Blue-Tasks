# Law Firm Management System

## Introduction

The **Law Firm Management System** is a Django web application for organizing core law-firm records in one place. It models the relationships between clients, lawyers, and cases, and provides server-rendered web pages for staff to create, review, edit, and delete those records. A case is assigned to one client and one lawyer and can be marked Open, Pending, or Closed.

The project is built as a traditional Django application: Django handles URL routing, form validation, database access, and HTML rendering; PostgreSQL stores the application data; and locally bundled Bootstrap assets provide the interface styling. The separate Django apps keep the main business areas organized, while the shared templates provide common navigation and page layout.

This repository is useful as a learning project or local prototype for Django CRUD workflows, model relationships, migrations, and PostgreSQL setup. It is not yet a complete law-practice platform: features such as authentication for the management pages, document storage, billing, appointments, and audit history are not implemented.

**Repository:** [github.com/hunter-devil2057/LawFirm_Management_System](https://github.com/hunter-devil2057/LawFirm_Management_System)

> **Important:** This project is currently a development/demo application, not a production-ready case-management system. It has no application-level login or access control for its CRUD pages, and its Django/database settings contain development defaults. Do not use it with real client or privileged case information until it has been secured and reviewed.

## Contents

- [Features](#features)
- [Technology](#technology)
- [How the application is organized](#how-the-application-is-organized)
- [Project layout](#project-layout)
- [Clone the repository](#clone-the-repository)
- [Requirements](#requirements)
- [Setup](#setup)
- [Run the application](#run-the-application)
- [Using the application](#using-the-application)
- [URL reference](#url-reference)
- [Database model](#database-model)
- [Tests and maintenance](#tests-and-maintenance)
- [Configuration and deployment notes](#configuration-and-deployment-notes)
- [Current limitations](#current-limitations)
- [Contact](#contact)

## Features

- **Clients:** store first and last names, email addresses, and phone numbers.
- **Lawyers:** store first and last names, email addresses, and phone numbers.
- **Cases:** store a title, description, status, assigned client, assigned lawyer, and creation/update timestamps.
- **Case statuses:** Open, Closed, and Pending.
- **Django admin:** manage the registered Client, Lawyer, and Case records at `/admin/`.
- **Responsive UI:** server-rendered Django templates styled with the Bootstrap assets in `static/`.

## Technology

- Python 3.12 or later
- Django 6.1.2
- PostgreSQL
- `psycopg2` PostgreSQL adapter
- `django-widget-tweaks` for form rendering
- Bootstrap CSS and JavaScript assets stored in the repository

Exact Python package versions are listed in [`requirements.txt`](requirements.txt).

## How the application is organized

The browser sends a request to a URL declared in `bls_project/urls.py`. That root URL configuration delegates requests to the `home`, `clients`, `lawyers`, or `cases` app. Each management app connects its URL patterns to Django class-based views. The views use a `ModelForm` to validate submitted data and a model to read or write PostgreSQL records, then render the corresponding template. Shared navigation and Bootstrap assets are included by the base template.

The main records relate as follows:

```text
Client 1 ---- many Cases many ---- 1 Lawyer
```

Each case is associated with exactly one client and one lawyer; a client or lawyer may be associated with multiple cases. Deleting either related record cascades to its associated cases.

## Project layout

```text
.
├── bls_project/
│   ├── settings.py     # Installed apps, database, templates, static files, and security settings
│   ├── urls.py         # Root routes: admin, home, clients, lawyers, and cases
│   ├── asgi.py         # ASGI application entry point
│   └── wsgi.py         # WSGI application entry point
├── cases/
│   ├── models.py       # Case model and client/lawyer relationships
│   ├── forms.py        # Case form
│   ├── views.py        # Case list/create/update/delete views
│   ├── urls.py         # Case page routes
│   ├── admin.py        # Case registration in Django admin
│   ├── tests.py        # Case test module (currently scaffolding)
│   └── migrations/     # Case schema history
├── clients/            # Client model, form, CRUD views/routes, admin, tests, migrations
├── lawyers/            # Lawyer model, form, CRUD views/routes, admin, tests, migrations
├── home/               # Home page view and route
├── templates/
│   ├── base.html       # Shared page layout and navigation
│   ├── home.html       # Landing page
│   ├── cases/          # Case list, form, and delete confirmation templates
│   ├── clients/        # Client list, form, and delete confirmation templates
│   └── lawyers/        # Lawyer list, form, and delete confirmation templates
├── static/
│   ├── css/            # Bootstrap stylesheet
│   └── js/             # Bootstrap JavaScript bundles
├── manage.py           # Django command-line entry point
└── requirements.txt    # Python dependency pins
```

Each app's `models.py` defines its database records, `forms.py` defines accepted form fields, `views.py` implements page behavior, and `urls.py` maps that behavior to paths. Migration files describe database schema changes over time. The `home` app currently provides the landing page and does not define a model.

## Clone the repository

Install Git, then clone the GitHub repository and enter its directory:

```console
git clone https://github.com/hunter-devil2057/LawFirm_Management_System.git
cd LawFirm_Management_System
```

In Windows PowerShell, you can choose a parent directory before cloning, for example:

```powershell
Set-Location "$HOME\Documents\My-Codes"
git clone https://github.com/hunter-devil2057/LawFirm_Management_System.git
Set-Location .\LawFirm_Management_System
```

Continue with the [setup](#setup) steps below. Create the virtual environment after cloning; `.venv/` is ignored by Git and should not be committed.

## Requirements

Before setting up, install:

1. **Python 3.12+** and `pip`.
2. **PostgreSQL**, running locally or reachable from the development machine. The configured default host and port are `localhost:5432`.
3. A PostgreSQL role and database. The current Django settings expect a database named `bls`; adjust `bls_project/settings.py` if you choose different database credentials or a different database name.

Check the installed Python version:

```powershell
python --version
```

## Setup

Run the following commands from the project root (the directory containing `manage.py`).

### 1. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell prevents activation, either allow scripts for this terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Or use Command Prompt:

```bat
py -m venv .venv
.venv\Scripts\activate.bat
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```console
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The PostgreSQL adapter may require platform-specific prerequisites if a compatible wheel is unavailable. Install the PostgreSQL client/development tools for your operating system, then retry the dependency installation.

### 3. Create a PostgreSQL role and database

Connect to PostgreSQL as an administrative role, for example:

```console
psql -U postgres -h localhost -p 5432
```

In the `psql` prompt, create a dedicated application role and database. Replace the example password with a strong local development password:

```sql
CREATE ROLE bls_app WITH LOGIN PASSWORD 'replace-with-a-strong-password';
CREATE DATABASE bls OWNER bls_app;
```

Exit with `\q`. If PostgreSQL is installed as a Windows service, make sure that service is running before starting Django.

### 4. Configure the database connection

Database settings are currently written directly in `bls_project/settings.py`; this project does not currently load them from environment variables. Update the `DATABASES['default']` values there to match the role, password, database name, host, and port you created. For example:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "bls",
        "USER": "bls_app",
        "PASSWORD": "replace-with-a-strong-password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

Do not commit real credentials. For a shared or deployed environment, move secrets out of source control and load them through a proper environment-based configuration mechanism.

### 5. Apply database migrations

```console
python manage.py migrate
```

This creates the built-in Django tables and the application tables for clients, lawyers, and cases. If the command fails with a connection error, check that PostgreSQL is running and that the database settings and role permissions are correct.

### 6. (Optional) Create an admin account

```console
python manage.py createsuperuser
```

Follow the prompts. This account is for Django's admin site; the regular client, lawyer, and case pages do not currently require sign-in.

## Run the application

Start Django's development server from the project root:

```console
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in a browser. Stop the server with `Ctrl+C`.

The development server is intended for local development only. Do not expose it publicly or use it as a production server.

## Using the application

Use the navigation menu to open the Clients, Lawyers, or Cases pages.

1. Add clients and lawyers before creating cases.
2. Create a case by entering a title and description, selecting a status, and assigning an existing client and lawyer.
3. Use the Edit and Delete actions in each list to update or remove records.
4. Alternatively, sign in to `/admin/` with the superuser created above.

Deleting a client or lawyer also deletes every case assigned to that record because both case relationships use database-level cascading deletion. Review linked cases before deleting either record.

## URL reference

These are the URL patterns currently declared by the project. Some paths are unconventional (for example, the record ID is immediately followed by `update` or `delete`); use the links generated by the application rather than assuming conventional trailing slashes.

| Purpose | URL |
| --- | --- |
| Home | `/` |
| Django admin | `/admin/` |
| Client list | `/clients/client/` |
| Create client | `/clients/client/create` |
| Edit client | `/clients/client/<id>update` |
| Delete client | `/clients/client/<id>delete` |
| Lawyer list | `/lawyers/details/` |
| Create lawyer | `/lawyers/lawyer/create` |
| Edit lawyer | `/lawyers/lawyer/<id>update` |
| Delete lawyer | `/lawyers/lawyer/<id>delete` |
| Case list | `/cases/case/` |
| Create case | `/cases/case/create` |
| Edit case | `/cases/case/<id>update` |
| Delete case | `/cases/case/<id>delete` |

Replace `<id>` with the integer primary key of the record, such as `/cases/case/3update`.

## Database model

- **Client:** `first_name`, `last_name`, `email`, and `phone`.
- **Lawyer:** `first_name`, `last_name`, `email`, and `phone`.
- **Case:** `title`, `description`, `status`, a required foreign key to a client, a required foreign key to a lawyer, `created_at`, and `updated_at`.

Case status values are `OPEN`, `CLOSED`, and `PENDING`; the UI displays their corresponding labels. A case must reference an existing client and lawyer.

## Tests and maintenance

Run Django's system checks:

```console
python manage.py check
```

Run the project test suite:

```console
python manage.py test
```

The current `tests.py` files contain only Django test scaffolding, so the test command does not yet provide meaningful coverage of CRUD behavior.

After changing models, generate and apply migrations:

```console
python manage.py makemigrations
python manage.py migrate
```

If static assets are prepared for a deployment, collect them with:

```console
python manage.py collectstatic
```

The project sets `STATIC_ROOT` to `staticfiles/`; a production web server or static-file service still needs to be configured to serve the collected files.

## Configuration and deployment notes

The checked-in settings are development-oriented. Before deploying or handling actual client data:

- Replace the development `SECRET_KEY` and store it outside source control.
- Set `DEBUG = False` and restrict `ALLOWED_HOSTS` to the actual host names.
- Move database credentials into environment-based configuration and use a dedicated, least-privileged database role.
- Add authentication and authorization to all client, lawyer, and case views; the current CRUD pages are not protected by login.
- Configure HTTPS, secure session and CSRF cookies, logging, backups, and a production-capable WSGI/ASGI server.
- Review privacy, retention, access auditing, and applicable legal/professional obligations before storing confidential or privileged information.

The settings currently define a console email backend under `MAILERS`. Django's standard email configuration uses `EMAIL_BACKEND`; configure that setting if the application is extended to send email.

## Current limitations

- No application-level authentication or per-user permissions are implemented for the CRUD pages.
- Automated tests are placeholders; CRUD flows and production behavior need test coverage.
- Some create/update success URLs and delete redirects do not match the list URL patterns declared in the app routes. The list pages and their generated CRUD links may work, but redirects after saving or deleting should be verified and corrected before relying on those flows.
- Routes omit trailing slashes on several create, update, and delete patterns.
- Database and Django security settings are hard-coded in the project settings rather than loaded from environment variables.
- There is no deployment configuration, production server, or static-file hosting configuration included.

## Contact

For questions or project feedback, contact the author:

- **Email:** [manishshiwakoti42@gmail.com](mailto:manishshiwakoti42@gmail.com)
- **LinkedIn:** [manish-shiwakoti-01721b260](https://www.linkedin.com/in/manish-shiwakoti-01721b260)
- **Instagram:** [@shiwakoti.manish](https://www.instagram.com/shiwakoti.manish/)
- **GitHub repository:** [hunter-devil2057/LawFirm_Management_System](https://github.com/hunter-devil2057/LawFirm_Management_System)
