## Features

- FastAPI API with CRUD endpoints: `/api/v1/mil-symbols/`
- Image uploads to ImageKit with `icon_url` stored in DB
- CORS enabled, Pydantic validation, and Swagger/OpenAPI at `/docs`
- Docker + docker-compose for easy setup
- Option to run locally with `venv` and local PostgreSQL

---

## Quick links
- Swagger UI: `http://localhost:8000/docs`
- Health check: `http://localhost:8000/health`

---

## Prerequisites

### For Docker setup
- Docker Desktop (or engine) installed and running
- `docker` and `docker compose` available in PATH

### For local setup (without Docker)
- Python 3.11+ installed
- PostgreSQL server installed and running 
- `pip` available
- (optional) `virtualenv`

---

## Environment variables

Copy `.env.example` to `.env` in the project root and edit values:

## Steps to Run

# Docker
docker compose up --build

# OR local
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
