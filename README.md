# Cinema Booking API Testing

This project contains the backend API for a Cinema Booking system, built with FastAPI, and an automated API testing suite using Postman and Newman.

## Project Structure

- /app: Contains the FastAPI application, database models, and routing logic.
- /postman: Contains the Postman Collection and Environment files for API testing.
- /newman: Contains the Newman configuration and runner script to execute tests automatically.

## Prerequisites

- Python 3.8 or higher
- Node.js and npm (for running Newman)

## Running the API Server

1. Create and activate a virtual environment:
   python -m venv venv
   Windows: venv\Scripts\activate
   Linux/Mac: source venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Start the API server:
   uvicorn app.main:app --reload

The API will be available at http://localhost:8000. You can view the Swagger documentation at http://localhost:8000/docs.

## Running Automated Tests

1. Ensure the API server is running locally.

2. Open a new terminal and navigate to the newman folder:
   cd newman

3. Install Newman and the HTMLExtra reporter:
   npm install

4. Run the test suite:
   Windows: run-tests.bat
   Linux/Mac: npm test

5. View the test report:
   A detailed HTML report will be generated in the newman/reports directory. Open report.html in any web browser to view the test results.

## Endpoints Tested

- POST /api/v1/auth/register : Registers a new user with dynamic email generation.
- POST /api/v1/auth/login : Authenticates the user and retrieves a JWT token.
- GET /api/v1/movies : Returns a list of available movies.
- POST /api/v1/bookings : Creates a new booking using the authenticated token.
- DELETE /api/v1/bookings/{id} : Cancels the previously created booking.
- GET /api/v1/user/bookings : Retrieves the booking history for the logged-in user.
