# Cinema Booking API

## Project Overview
This project is a REST API System designed for software testing practice, built with FastAPI, SQLAlchemy, and SQLite. It provides comprehensive functionality for user authentication, movie browsing, and ticket booking, along with built-in defects (such as IDOR and Negative Value injection) intentionally designed for QA and API testing exercises.

## Modules & Features

### 1. Authentication
- POST /api/v1/auth/register: Register a new user account.
- POST /api/v1/auth/login: Login to obtain a JWT Bearer token.

### 2. Movies
- GET /api/v1/movies: View the list of all available movies and their seating capacities.
- GET /api/v1/movies/{id}: View detailed information of a specific movie.

### 3. Booking
- POST /api/v1/bookings: Book tickets for a specific movie.
- DELETE /api/v1/bookings/{id}: Cancel an existing booking.

### 4. History
- GET /api/v1/user/bookings: View the booking history of the authenticated user.

## Technology Stack
- Framework: FastAPI
- Database: SQLite
- ORM: SQLAlchemy
- Data Validation: Pydantic
- Authentication: JWT (python-jose) & Password Hashing (passlib, bcrypt)
- Testing: Pytest (Unit), Postman & Newman (API Automation)

## Installation & Setup

1. Create a virtual environment:
   python -m venv venv

2. Activate the virtual environment:
   - Windows: venv\Scripts\activate
   - Mac/Linux: source venv/bin/activate

3. Install the required dependencies:
   pip install -r requirements.txt

4. Configure environment variables:
   Copy `.env.example` to `.env` and adjust the configuration variables if necessary.

5. Seed the database with sample movies:
   python -m app.seed

6. Start the development server:
   python -m uvicorn app.main:app --reload

## Testing

### Swagger UI
Once the server is running, navigate to http://localhost:8000/docs to explore the API endpoints interactively.

### Automated Testing (Newman)
The project includes a ready-to-run Postman Collection for automated testing.
1. Navigate to the newman directory:
   cd newman
2. Run the test script:
   - Windows: run-tests.bat
   - Mac/Linux: ./run-tests.sh
3. View the detailed HTML execution report inside the `newman/reports` directory.

### Unit Testing (Pytest)
To execute the backend unit tests:
   python -m pytest

## Automated Test Cases & Defect Reports
Please refer to the following documents in the root directory for testing materials:
- REQUIREMENTS.md: Business and functional requirements.
- TEST_SCENARIOS.md: Test scenario outlines.
- TEST_CASES.md: Detailed API test cases (Positive, Negative, Boundary, Security).
- POSTMAN_SCRIPTS.md: JavaScript automation scripts used in the collection.
- TEST_EXECUTION_REPORT.md: Summary of test executions.
- DEFECT_REPORT.md: Found vulnerabilities and bugs (e.g., BUG-001, BUG-002).
