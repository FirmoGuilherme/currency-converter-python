# Currency Converter API (FastAPI)

## Purpose
This project is a FastAPI-based service for managing users and currency transactions.  
It allows creating users, recording transactions between different currencies, and calculating conversion rates in real-time using an external API.  
The main goal is to provide a clean, modular, and extensible architecture with proper validation, error handling, and unit testability.

---

## Features
- `POST /transaction` to convert and persist a transaction.
- `GET /transactions?user_id=<id>` to list transactions for a user.
- SQLite by default (easy local setup). Optionally use Postgres via `DATABASE_URL` env var.
- Unit tests with pytest.
- Automatic OpenAPI docs (FastAPI). See `/docs`.

---

## Run locally (Docker)
1. Copy `.env.example` to `.env` and set `CURRENCYAPI_KEY`.
2. Build and run:
```bash
docker-compose build
docker-compose up
```