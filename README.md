# VWINGS24X7 Backend API

A FastAPI-based backend application for admin management with PostgreSQL database.

## Features

- Admin user registration and login
- PostgreSQL database integration
- Auto-generated admin IDs with timestamp pattern
- RESTful API endpoints
- Health check endpoint
- CORS enabled for all origins

## Prerequisites

- Python 3.8 or higher
- PostgreSQL database
- pgAdmin (optional, for database management)

## Setup Instructions

### 1. Clone the Repository

```bash
cd /Users/debasishbaidya/Documents/VWINGS24X7/BACKEND
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

Make sure your `.env` file has the correct PostgreSQL credentials:

```env
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=2004
DB_NAME=app_admin_db
```

### 5. Create Database

Create the PostgreSQL database using pgAdmin or psql:

```sql
CREATE DATABASE app_admin_db;
```

### 6. Run the Backend Server

```bash
python main.py
```

Or using uvicorn directly:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The server will start on `http://0.0.0.0:8000` (accessible from any IP)

Database tables will be created automatically on startup.

## API Endpoints

### Health Check
- **GET** `/health` - Check server status

### Admin Management
- **POST** `/api/admin/register` - Register a new admin
- **POST** `/api/admin/login` - Login admin
- **GET** `/api/admin/{admin_id}` - Get admin by ID
- **GET** `/api/admin/` - Get all admins (with pagination)

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Admin ID Format

Admin IDs are auto-generated in the format: `ADMIN-{4-digit-timestamp}{full-timestamp}`

Example: `ADMIN-12341705132800`

## Example API Usage

### Register Admin

```bash
curl -X POST "http://localhost:8000/api/admin/register" \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@example.com", "password": "securepassword"}'
```

### Login Admin

```bash
curl -X POST "http://localhost:8000/api/admin/login" \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@example.com", "password": "securepassword"}'
```

### Get All Admins

```bash
curl -X GET "http://localhost:8000/api/admin/"
```

## Project Structure

```
BACKEND/
├── main.py                 # FastAPI application entry point
├── db.py                   # Database configuration
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
├── models/
│   └── auth/
│       └── admin_models.py # Admin database model
├── routes/
│   └── auth/
│       └── admin_routes.py # Admin API routes
└── services/
    └── admin_id_generator.py # Admin ID generation service
```

## Deactivating Virtual Environment

When you're done working:

```bash
deactivate
```

## Troubleshooting

### Database Connection Error
- Ensure PostgreSQL is running
- Verify database credentials in `.env`
- Check if the database exists

### Import Errors
- Make sure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

### Port Already in Use
- Change the port in `main.py` or kill the process using port 8000

## License

MIT
