# Cinema Booking REST API System - Requirements Document

## 1. Business Requirements

**Project Overview:** 
A REST API system designed to simulate a real-world cinema booking application. The primary purpose of this system is to serve as a training ground for software testers to practice API testing, test automation (using Postman/Newman), and defect tracking.

**Business Objectives:**
- Provide a reliable and predictable API sandbox for QA professionals to build test suites.
- Simulate real-world scenarios including successful operations, edge cases, and deliberate failure modes (to facilitate defect tracking practice).
- Support standard CRUD (Create, Read, Update, Delete) operations to enable comprehensive API test coverage.

---

## 2. Functional Requirements

### Authentication Module
- **FR1:** The system shall allow a new user to register by providing a username, email, and password.
- **FR2:** The system shall allow an existing user to login using their email and password, returning an authentication token (e.g., JWT).
- **FR3:** The system shall enforce unique email addresses for registration.

### Movies Module
- **FR4:** The system shall allow users (both authenticated and unauthenticated) to retrieve a list of all currently showing movies.
- **FR5:** The system shall allow users to view detailed information about a specific movie using its unique ID (including title, genre, duration, release date, and available seats).

### Booking Module
- **FR6:** The system shall allow authenticated users to book tickets for a specific movie, specifying the number of seats.
- **FR7:** The system shall prevent a booking from succeeding if the requested number of seats exceeds the currently available seats.
- **FR8:** The system shall allow authenticated users to cancel their booked ticket before the movie showtime.

### History Module
- **FR9:** The system shall allow authenticated users to view their past and upcoming booking history.

---

## 3. Non-Functional Requirements

- **Security:** All endpoints modifying data (booking/canceling) or accessing user-specific data (history) must require a valid authentication token via the `Authorization: Bearer <token>` header. Passwords must not be exposed in any API responses.
- **Performance:** API responses should generally be returned within 500ms under normal load to simulate a performant backend.
- **Error Handling:** The API must return standard HTTP status codes:
  - `200 OK` / `201 Created` for successful operations.
  - `400 Bad Request` for invalid inputs.
  - `401 Unauthorized` for missing or invalid tokens.
  - `403 Forbidden` for attempting to access/modify another user's resources.
  - `404 Not Found` for querying non-existent IDs.
  - `500 Internal Server Error` for unexpected server crashes.
- **Format:** All requests and responses must strictly use JSON format (`application/json`).

---

## 4. Use Cases

### UC1: User Registration & Login
- **Actor:** New User
- **Precondition:** None.
- **Flow:** User submits registration details -> System creates the account. User submits login credentials -> System validates and returns an Auth Token.

### UC2: Browse Movies
- **Actor:** Any User
- **Precondition:** None.
- **Flow:** User requests the movie list -> System returns an array of all movies. User requests a specific movie ID -> System returns the movie's detailed object.

### UC3: Book a Ticket
- **Actor:** Authenticated User
- **Precondition:** User is logged in and has a valid token.
- **Flow:** User selects a movie ID and number of seats -> Submits a POST request with the token -> System verifies seat availability -> System creates the booking, deducts available seats, and returns a Booking ID.
- **Alternate Flow (Sold Out / Insufficient Seats):** System verifies seat availability -> Not enough seats -> Returns an error message with a `400 Bad Request`.

### UC4: Cancel a Ticket
- **Actor:** Authenticated User
- **Precondition:** User has a valid, active booking.
- **Flow:** User submits a cancellation request with the Booking ID -> System validates ownership of the booking -> System cancels the booking, restores available seats, and returns a success message.

### UC5: View Booking History
- **Actor:** Authenticated User
- **Precondition:** User is logged in.
- **Flow:** User requests booking history -> System returns a list of the user's past and active bookings.

---

## 5. API Overview

| Module | Method | Endpoint | Description | Auth Required |
|---|---|---|---|---|
| Authentication | `POST` | `/api/v1/auth/register` | Register a new user account | No |
| Authentication | `POST` | `/api/v1/auth/login` | Login and receive an access token | No |
| Movies | `GET` | `/api/v1/movies` | Retrieve a list of all movies | No |
| Movies | `GET` | `/api/v1/movies/{id}` | Retrieve details of a specific movie | No |
| Booking | `POST` | `/api/v1/bookings` | Book a ticket for a movie | Yes |
| Booking | `DELETE` | `/api/v1/bookings/{id}` | Cancel an existing booking | Yes |
| History | `GET` | `/api/v1/user/bookings` | Retrieve the authenticated user's booking history | Yes |

---

## 6. Testing Scope

**In-Scope for API Testing Practice:**

1. **Positive Testing:** Verify that all endpoints return `200/201` status codes and correct JSON schemas when provided with valid request data.
2. **Negative Testing & Edge Cases:**
   - Test invalid login credentials (wrong email/password).
   - Test booking a movie with insufficient seats, zero seats, or negative seats.
   - Test booking with an invalid or non-existent movie ID.
   - Test canceling a booking that does not exist or belongs to another user.
   - Test missing required fields in request bodies.
3. **Authentication & Authorization:** Verify that protected routes return `401 Unauthorized` without a token, and `403 Forbidden` with an expired/invalid token.
4. **Data Integrity & State Transitions:** Verify that booking a ticket accurately decreases the movie's available seat count, and canceling a booking accurately restores it.
5. **Automated Testing Setup (Postman/Newman):**
   - Create a Postman Collection covering all API endpoints.
   - Implement environment variables for `{{baseUrl}}` and `{{token}}`.
   - Write Postman test scripts (e.g., `pm.test()`, `pm.response.to.have.status()`, schema validation) to assert responses automatically.
   - Run the collection from the CLI using Newman to simulate CI/CD pipeline integration.
6. **Defect Tracking Practice:** Actively look for intentional logical flaws (e.g., if the API allows booking negative seats, or if canceling an already canceled ticket works) and log them as bugs in a defect tracking tool (like Jira or Trello) with reproducible steps.

**Out-of-Scope:**
- Load, Stress, and Performance Testing.
- UI/Frontend Testing.
- Direct Database layer testing (testing is strictly black-box via the REST API endpoints).
