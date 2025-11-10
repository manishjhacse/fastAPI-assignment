# MIL Symbols Backend API Documentation

## Base URL
| Environment | URL |
|--------------|-----|
| Local | `http://127.0.0.1:8000` |
| Docker | `http://localhost:8000` |

---

## Endpoints Summary

| Method | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/api/v1/mil-symbols/` | List all military symbols |
| `GET` | `/api/v1/mil-symbols/{id}` | Retrieve symbol by UUID |
| `POST` | `/api/v1/mil-symbols/` | Create new symbol |
| `PUT` | `/api/v1/mil-symbols/{id}` | Update existing symbol |
| `DELETE` | `/api/v1/mil-symbols/{id}` | Delete symbol |
| `GET` | `/health` | Health check endpoint |

---

## Schema

### Symbol Object
| Field | Type | Required | Description |
|--------|------|-----------|-------------|
| `id` | UUID | Auto | Unique symbol identifier |
| `name` | string | ✅ | Symbol name |
| `code` | string | ✅ | Symbol short code (unique) |
| `type` | string | ❌ | Symbol type or classification |
| `description` | string | ❌ | Short info about the symbol |
| `icon_url` | string (URL) | Auto | ImageKit or external icon URL |
| `created_at` | datetime | Auto | Timestamp |
| `updated_at` | datetime | Auto | Timestamp |

---


