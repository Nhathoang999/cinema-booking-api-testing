# Acceptance Criteria

This document defines the conditions that a software product must satisfy to be accepted by a user, customer, or other stakeholder. It bridges User Stories (US) to Test Scenarios.

## AC-01: User Registration (US-01)
- **AC-01.1**: If the user submits a valid email format (e.g., `user@example.com`) and a password (min 6 characters), the system returns a `201 Created` status code and the user's ID.
- **AC-01.2**: If the user submits an email that is already registered, the system returns a `409 Conflict` status code.
- **AC-01.3**: If the user submits an invalid email format (e.g., `userdomain.com`), the system returns a `422 Unprocessable Entity` status code.
- **AC-01.4**: If the user submits a password less than 6 characters, the system returns a `422 Unprocessable Entity` status code.

## AC-02: User Login (US-02)
- **AC-02.1**: If the user submits the correct registered email and password, the system returns a `200 OK` status and a valid JWT access token.
- **AC-02.2**: If the user submits an incorrect password, the system returns a `401 Unauthorized` status code.
- **AC-02.3**: If the user submits an unregistered email, the system returns a `401 Unauthorized` or `404 Not Found` status code.

## AC-03: Browse Movies (US-03)
- **AC-03.1**: When requested, the system returns a `200 OK` status and a JSON array containing at least one movie object (ID, title, genre, duration).

## AC-04: Create Booking (US-04)
- **AC-04.1**: If a user provides a valid JWT token in the Authorization header and a valid `movie_id`, the system creates the booking and returns a `201 Created` status with the `booking_id`.
- **AC-04.2**: If a user does not provide a JWT token, the system returns a `401 Unauthorized` status code.
- **AC-04.3**: If a user provides an invalid or expired JWT token, the system returns a `401 Unauthorized` status code.
- **AC-04.4**: If a user provides a `movie_id` that does not exist, the system returns a `404 Not Found` or `422 Unprocessable Entity`.

## AC-05: View Booking History (US-05)
- **AC-05.1**: If a user provides a valid JWT token, the system returns a `200 OK` status and a JSON array of all bookings made by that specific user.
- **AC-05.2**: The returned list must not contain bookings made by any other users.

## AC-06: Cancel Booking (US-06)
- **AC-06.1**: If a user provides a valid JWT token and the ID of a booking they own, the system deletes/cancels the booking and returns a `200 OK` or `204 No Content` status.
- **AC-06.2**: If a user tries to cancel a booking ID that belongs to another user, the system returns a `403 Forbidden` or `404 Not Found` status.
- **AC-06.3**: If a user tries to cancel a booking ID that does not exist, the system returns a `404 Not Found` status.
