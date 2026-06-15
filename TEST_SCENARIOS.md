# Cinema Booking API - Test Scenarios

| Module | Scenario ID | Scenario Name | Description | Priority |
| :--- | :--- | :--- | :--- | :--- |
| **1. Authentication** | TS_AUTH_01 | Register with valid details | Verify successful registration with valid username, email, and password. | High |
| | TS_AUTH_02 | Register with existing email | Verify registration fails with `400 Bad Request` when using an email that is already registered. | High |
| | TS_AUTH_03 | Login with valid credentials | Verify successful login and auth token generation with correct email and password. | High |
| | TS_AUTH_04 | Login with incorrect password | Verify login fails and returns `401 Unauthorized` when password is incorrect. | High |
| | TS_AUTH_05 | Register with missing fields | Verify registration fails when required fields (username/email/password) are omitted. | Medium |
| **2. Movies** | TS_MOV_01 | Get all movies list | Verify the API returns an array of currently showing movies with `200 OK`. | High |
| | TS_MOV_02 | Get movie details by valid ID | Verify the API returns correct details (title, genre, seats, etc.) for a valid movie ID. | High |
| | TS_MOV_03 | Get movie details by invalid ID | Verify the API returns a `404 Not Found` error when querying a non-existent movie ID. | High |
| | TS_MOV_04 | Validate movie data schema | Verify that the returned movie JSON payload matches the expected schema types. | Medium |
| **3. Booking** | TS_BKG_01 | Book valid number of tickets | Verify successful booking creation and accurate deduction of available seats for a valid request. | High |
| | TS_BKG_02 | Book tickets exceeding capacity | Verify booking fails when requested seats exceed the currently available movie capacity. | High |
| | TS_BKG_03 | Book zero or negative seats | Verify booking fails with `400 Bad Request` when requesting 0 or a negative number of seats. | Medium |
| | TS_BKG_04 | Cancel an existing booking | Verify successful cancellation and correct restoration of available seats for a valid booking ID. | High |
| | TS_BKG_05 | Cancel an already cancelled booking | Verify cancellation fails or returns appropriate error if the booking was already cancelled. | Medium |
| **4. History** | TS_HIS_01 | View populated booking history | Verify the API returns a correct list of past and active bookings for the logged-in user. | High |
| | TS_HIS_02 | View history for new user | Verify the API returns an empty list (`[]`) for a user with no prior bookings. | Medium |
| | TS_HIS_03 | View history formatting | Verify that history response correctly distinguishes between 'active' and 'cancelled' status. | Low |
| **5. Authorization**| TS_AUTHZ_01 | Access protected route without token | Verify a `401 Unauthorized` error is returned when accessing bookings/history without providing a Bearer token. | High |
| | TS_AUTHZ_02 | Access protected route with invalid token| Verify a `401/403` error is returned when using a malformed, manipulated, or expired token. | High |
| | TS_AUTHZ_03 | Cancel another user's booking | Verify a `403 Forbidden` error is returned when trying to cancel a valid booking owned by a different user. | High |
| **6. Error Handling** | TS_ERR_01 | Submit malformed JSON payload | Verify the API returns a `400 Bad Request` when the POST/PUT request body contains invalid JSON syntax. | Medium |
| | TS_ERR_02 | Submit unsupported HTTP method | Verify the API returns `405 Method Not Allowed` when using an incorrect HTTP method (e.g., POST to `/movies`). | Low |
| | TS_ERR_03 | Verify standard error schema | Verify that all API error responses follow a consistent JSON schema containing standard fields like `error_code` and `message`. | Medium |
