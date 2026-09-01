# devops-test

A one-page Django website for a luxury watch boutique (Aurum Watch Store).

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Environment Variables

Copy `.env.example` to `.env` and update values as needed:

| Variable       | Description                          |
|----------------|--------------------------------------|
| `SECRET_KEY`   | Django secret key (required in prod) |
| `DEBUG`        | Enable debug mode (`True`/`False`)     |
| `ALLOWED_HOSTS`| Comma-separated hostnames              |

## Structure

- `store/` — Django app with views, templates, and static assets
- `watchstore/` — Project settings and URL configuration

The homepage includes a hero section, featured watch collection, about section, contact form, and footer — all on a single scrollable page.
