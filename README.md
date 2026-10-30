# fastapi-modular

A production-ready **FastAPI** project built with a modular structure — routers, models, middleware, dependencies, and logging all separated into their own modules.

This project is the companion code for the Medium article:
📖 [Building a Production-Ready FastAPI Project with Modular Structure](https://medium.com/@shivampahariya6225/building-a-production-ready-fastapi-project-with-modular-structure-c21becfd3595?postPublishedType=initial)

---

## Project Structure

```
fastapi-modular/
├── src/
│   ├── main.py                        # App entry point
│   ├── routers/
│   │   ├── __init__.py
│   │   └── user_data_router.py        # User data endpoints
│   ├── models/
│   │   ├── __init__.py
│   │   └── user_data_models.py        # Pydantic request/response models
│   ├── services/
│   │   └── __init__.py                # Business logic layer
│   ├── middleware/
│   │   ├── __init__.py
│   │   └── cors.py                    # CORS middleware
│   └── dependencies/
│       ├── __init__.py
│       └── logger.py                  # Singleton logger
├── logs/                              # Auto-created on first run
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Prerequisites

- Python 3.7+

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/shivam6225/fastapi-modular.git
cd fastapi-modular
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn src.main:app --reload
```

Or run directly with Python:

```bash
python src/main.py
```

The server starts at **http://localhost:8000**

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Health check — verify the service is running |
| `POST` | `/user-data/get-user-data` | Fetch user data by `user_id` |

### Interactive Docs

FastAPI auto-generates a Swagger UI — no setup needed:

```
http://localhost:8000/docs
```

---

## Example Request

**POST** `/user-data/get-user-data`

```json
{
  "user_id": 1
}
```

**Response `200 OK`**

```json
{
  "user_id": 1,
  "name": "Shivam Pahariya",
  "email": "shivam.pahariya@example.com",
  "age": 25,
  "address": "Karnataka, India"
}
```

**Response `404 Not Found`** (when `user_id <= 0`)

```json
{
  "detail": "User Not Found or Invalid User ID"
}
```

---

## Logging

Logs are written automatically to the `logs/` folder on first request:

```
logs/
└── user_data_logs/
    └── user_data_router_YYYY-MM-DD_HH-MM-SS.log
```

---

## Author

**Shivam Pahariya**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/shivam-pahariya-3963aa183/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/shivam6225)

