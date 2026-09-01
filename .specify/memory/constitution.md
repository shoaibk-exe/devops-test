<!--
Sync Impact Report
- Version change: (template) → 1.0.0
- Modified principles: All placeholders replaced with project-specific rules
- Added sections: Security Requirements, Django Coding Standards, Development Workflow
- Removed sections: None
- Follow-up TODOs: None
-->

# devops-test Constitution

## Core Principles

### I. Secrets Never in Source Control
All sensitive values (SECRET_KEY, database credentials, API keys, tokens) MUST be loaded from environment variables via `.env` at runtime. `.env` MUST remain gitignored. Only `.env.example` with placeholder or fake values MAY be committed. Hardcoded secrets in Python, templates, or config files are forbidden.

### II. Environment-First Configuration
Django settings MUST read configuration from environment variables with safe development fallbacks only. DEBUG MUST default to False in production. ALLOWED_HOSTS MUST be explicitly set before deployment. No production-specific values in committed code.

### III. Minimal Scope Changes
Every change MUST solve the stated problem with the smallest correct diff. Do not refactor, rename, or add features outside the current task. Match existing naming, structure, and patterns in `store/` and `watchstore/`.

### IV. Security by Default
User input MUST be validated and escaped. CSRF protection MUST remain enabled on all forms. SQL injection prevention via Django ORM (no raw SQL unless parameterized). Dependencies MUST be pinned in `requirements.txt`. Run `python manage.py check --deploy` before production releases.

### V. Simplicity Over Abstraction
Prefer Django built-ins over third-party libraries unless clearly justified. No premature models, APIs, or microservices. One-page architecture stays one-page until a spec explicitly expands scope.

## Security Requirements

- NEVER commit `.env`, credentials, private keys, or real secret keys
- `.env.example` MAY contain fake-looking keys for scanner/testing purposes only — they MUST NOT be used in production
- Rotate any secret that appears in git history immediately
- Static files served via `collectstatic` in production; DEBUG=False disables dev error pages
- Admin panel MUST use strong credentials and SHOULD be restricted by IP or disabled in production if unused
- All new endpoints MUST be reviewed for authentication and authorization requirements

## Django Coding Standards

- Views: function-based for simple pages; class-based only when reuse warrants it
- Templates live in `store/templates/store/`; static assets in `store/static/store/`
- URL names MUST be declared for every route (`name=` in `urlpatterns`)
- Migrations MUST be created for any model change and committed alongside code
- Tests in `store/tests.py` for business logic; run `python manage.py test` before merge
- Follow PEP 8; keep views thin — business logic in models or dedicated modules

## Development Workflow

- Work on feature branches (`setup/*`, `feature/*`); never commit directly to `main`
- Constitution compliance MUST be verified in every PR review
- Spec Kit workflow: constitution → specify → plan → tasks → implement
- Commit messages: imperative mood, describe why not what (`fix: load SECRET_KEY from env for prod safety`)
- Before merge: tests pass, no secrets in diff, `python manage.py check` clean

## Governance

This constitution supersedes ad-hoc practices for the devops-test project. Amendments require a PR updating this file with a version bump and rationale in the Sync Impact Report comment. All PRs MUST verify compliance with Security Requirements and Django Coding Standards. Complexity beyond these rules MUST be justified in the spec or plan.

**Version**: 1.0.0 | **Ratified**: 2026-09-01 | **Last Amended**: 2026-09-01
