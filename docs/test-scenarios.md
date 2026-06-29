# High-Level Test Scenarios

This document groups test cases into high-level scenarios.

## Authentication (Auth)
- **TS-AUTH-01**: Verify a new user can successfully register with valid details.
- **TS-AUTH-02**: Verify a user cannot register with an existing email or invalid inputs.
- **TS-AUTH-03**: Verify a user can successfully login with correct credentials.
- **TS-AUTH-04**: Verify login fails with incorrect credentials or non-existent email.

## Movie Discovery (Movies)
- **TS-MOV-01**: Verify any user (authenticated or not) can retrieve the list of available movies.
- **TS-MOV-02**: Verify the movie list returns all expected attributes (title, duration, genre).

## Booking Management (Booking)
- **TS-BKG-01**: Verify an authenticated user can create a booking for a valid movie.
- **TS-BKG-02**: Verify booking fails if authentication is missing, invalid, or expired.
- **TS-BKG-03**: Verify booking fails for a non-existent movie ID.
- **TS-BKG-04**: Verify an authenticated user can view their booking history.
- **TS-BKG-05**: Verify an authenticated user can cancel their own booking.
- **TS-BKG-06**: Verify a user is forbidden from viewing or canceling another user's booking.
