# Food Delivery Platform Backend

This project is the complete backend system for a modern food delivery application, similar to platforms like Swiggy, Zomato, or Uber Eats. It is built with a focus on clean architecture, scalability, and robust system design principles using Python and FastAPI.

## Key Features

- **Multi-Role Authentication**: A single, secure authentication system that handles three distinct user roles: Customers, Restaurant Owners, and Delivery Drivers.
- **Restaurant Management**: Endpoints for restaurants to manage their profile, menu items, and view incoming orders.
- **Geospatial Queries**: Customers can find and list nearby restaurants based on their current latitude and longitude.
- **Full Order Lifecycle**: Implements a complete and robust state machine for tracking orders: `Placed` -> `Accepted` -> `Preparing` -> `Out for Delivery` -> `Delivered` / `Cancelled`.
- **Driver & Order Assignment**: Logic for drivers to view available orders and for the system to assign orders efficiently.
- **Database Migrations**: Uses Alembic to manage database schema changes in a safe and version-controlled manner.

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL with the PostGIS extension for geospatial capabilities.
- **ORM**: SQLAlchemy with GeoAlchemy2 for interacting with the database.
- **Data Validation**: Pydantic
- **Async Support**: `asyncio` with `asyncpg` for high-performance, non-blocking database operations.
- **Authentication**: JWT (JSON Web Tokens)
- **Database Migrations**: Alembic

## Getting Started

### Prerequisites

- Python 3.9+
- PostgreSQL with PostGIS extension enabled
- An active Python virtual environment

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <your-repo-url>
    cd Food-Delievery-System-backend
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure environment variables:**
    Create a `.env` file in the project root and populate it with your settings. You can use the `.env.example` as a template:

    ```
    DATABASE_URL="postgresql+asyncpg://user:password@host:port/dbname"
    SECRET_KEY="your_super_secret_key"
    ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

4.  **Run database migrations:**
    Apply all database migrations to create the necessary tables.

    ```bash
    alembic upgrade head
    ```

5.  **Run the application:**
    ```bash
    uvicorn app.main:app --reload
    ```
    The application will be available at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.
