# Cinema Booking API - Detailed Test Cases

## 1. Authentication Module

| TC ID | TS ID | Endpoint | Preconditions | Method | Headers | Body Payload | Test Steps | Expected Code | Expected Response | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC_AUTH_001** | TS_AUTH_01 | `/api/v1/auth/register` | None | `POST` | `Content-Type: application/json` | `{"username": "user1", "email": "test1@test.com", "password": "Password123!"}` | 1. Send POST request with valid new user details. | `201` | `{"message": "User registered successfully"}` | High (Positive) |
| **TC_AUTH_002** | TS_AUTH_02 | `/api/v1/auth/register` | User with `test1@test.com` already exists | `POST` | `Content-Type: application/json` | `{"username": "user2", "email": "test1@test.com", "password": "pwd"}` | 1. Send POST request with an already registered email. | `400` | `{"error": "Email already exists"}` | High (Negative) |
| **TC_AUTH_003** | TS_AUTH_05 | `/api/v1/auth/register` | None | `POST` | `Content-Type: application/json` | `{"username": "user1"}` | 1. Send POST request omitting email and password. | `400` | `{"error": "Email and password are required"}` | Medium (Negative) |
| **TC_AUTH_004** | TS_AUTH_05 | `/api/v1/auth/register` | None | `POST` | `Content-Type: application/json` | `{"username": "u1", "email": "invalidemail", "password": "pwd"}` | 1. Send POST request with incorrect email format. | `400` | `{"error": "Invalid email format"}` | Medium (Negative) |
| **TC_AUTH_005** | TS_AUTH_03 | `/api/v1/auth/login` | User `test1@test.com` exists | `POST` | `Content-Type: application/json` | `{"email": "test1@test.com", "password": "Password123!"}` | 1. Send POST request with correct credentials. | `200` | `{"token": "jwt_token_string"}` | High (Positive) |
| **TC_AUTH_006** | TS_AUTH_04 | `/api/v1/auth/login` | User `test1@test.com` exists | `POST` | `Content-Type: application/json` | `{"email": "test1@test.com", "password": "WrongPassword!"}` | 1. Send POST request with incorrect password. | `401` | `{"error": "Invalid credentials"}` | High (Negative) |
| **TC_AUTH_007** | TS_AUTH_04 | `/api/v1/auth/login` | User does not exist | `POST` | `Content-Type: application/json` | `{"email": "nonexistent@test.com", "password": "pwd"}` | 1. Send POST request with non-existent email. | `401` | `{"error": "Invalid credentials"}` | High (Negative) |
| **TC_AUTH_008** | TS_AUTH_01 | `/api/v1/auth/register` | None | `POST` | `Content-Type: application/json` | `{"username": "A"x256, "email": "a@b.c", "password": "pwd"}` | 1. Send request with username string length at/over max limit (e.g., 256 chars). | `400` | `{"error": "Username too long"}` | Medium (Boundary) |

## 2. Movies Module

| TC ID | TS ID | Endpoint | Preconditions | Method | Headers | Body Payload | Test Steps | Expected Code | Expected Response | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC_MOV_001** | TS_MOV_01 | `/api/v1/movies` | Database has >0 movies | `GET` | None | None | 1. Send GET request to retrieve movies. | `200` | `[{"id":1, "title":"...", ...}]` (Array of objects) | High (Positive) |
| **TC_MOV_002** | TS_MOV_01 | `/api/v1/movies` | Database has 0 movies | `GET` | None | None | 1. Send GET request when no movies exist. | `200` | `[]` (Empty array) | Medium (Boundary) |
| **TC_MOV_003** | TS_MOV_02 | `/api/v1/movies/{id}` | Movie ID `1` exists | `GET` | None | None | 1. Send GET request for ID `1`. | `200` | `{"id": 1, "title": "...", ...}` | High (Positive) |
| **TC_MOV_004** | TS_MOV_03 | `/api/v1/movies/{id}` | Movie ID `9999` missing | `GET` | None | None | 1. Send GET request for non-existent ID `9999`. | `404` | `{"error": "Movie not found"}` | High (Negative) |
| **TC_MOV_005** | TS_MOV_03 | `/api/v1/movies/{id}` | None | `GET` | None | None | 1. Send GET request with invalid ID type (e.g., `abc`). | `400` | `{"error": "Invalid ID format"}` | Medium (Negative) |
| **TC_MOV_006** | TS_MOV_04 | `/api/v1/movies/{id}` | Movie ID `1` exists | `GET` | None | None | 1. Send GET request. 2. Validate response exactly matches JSON Schema. | `200` | Schema perfectly validates | Medium (Positive) |

## 3. Booking Module

| TC ID | TS ID | Endpoint | Preconditions | Method | Headers | Body Payload | Test Steps | Expected Code | Expected Response | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC_BKG_001** | TS_BKG_01 | `/api/v1/bookings` | Valid Token, Movie 1 has >=2 seats | `POST` | `Authorization: Bearer <t>`, `Content-Type: application/json` | `{"movie_id": 1, "seats": 2}` | 1. Send POST request to book 2 tickets. | `201` | `{"booking_id": 123, "status": "CONFIRMED"}` | High (Positive) |
| **TC_BKG_002** | TS_BKG_02 | `/api/v1/bookings` | Valid Token, Movie 1 has 5 seats | `POST` | `Authorization: Bearer <t>`, `Content-Type: application/json` | `{"movie_id": 1, "seats": 6}` | 1. Send POST request for more seats than available. | `400` | `{"error": "Not enough seats available"}` | High (Negative) |
| **TC_BKG_003** | TS_BKG_01 | `/api/v1/bookings` | Valid Token, Movie 1 has 1 seat | `POST` | `Authorization: Bearer <t>`, `Content-Type: application/json` | `{"movie_id": 1, "seats": 1}` | 1. Book the exactly last remaining seat. | `201` | `{"booking_id": 124, "status": "CONFIRMED"}` | High (Boundary) |
| **TC_BKG_004** | TS_BKG_03 | `/api/v1/bookings` | Valid Token, Movie 1 exists | `POST` | `Authorization: Bearer <t>`, `Content-Type: application/json` | `{"movie_id": 1, "seats": 0}` | 1. Send POST request attempting to book 0 seats. | `400` | `{"error": "Seats must be greater than 0"}` | Medium (Boundary) |
| **TC_BKG_005** | TS_BKG_03 | `/api/v1/bookings` | Valid Token, Movie 1 exists | `POST` | `Authorization: Bearer <t>`, `Content-Type: application/json` | `{"movie_id": 1, "seats": -5}` | 1. Send POST request attempting to book negative seats. | `400` | `{"error": "Seats must be greater than 0"}` | Medium (Boundary) |
| **TC_BKG_006** | TS_BKG_03 | `/api/v1/bookings` | Valid Token, Movie 1 exists | `POST` | `Authorization: Bearer <t>`, `Content-Type: application/json` | `{"movie_id": 1, "seats": 1000000}` | 1. Send POST request for an absurdly high number of seats. | `400` | `{"error": "Not enough seats available"}` | Medium (Boundary) |
| **TC_BKG_007** | TS_BKG_01 | `/api/v1/bookings` | Valid Token | `POST` | `Authorization: Bearer <t>`, `Content-Type: application/json` | `{"movie_id": 9999, "seats": 2}` | 1. Send POST request for a non-existent movie ID. | `404` | `{"error": "Movie not found"}` | High (Negative) |
| **TC_BKG_008** | TS_BKG_04 | `/api/v1/bookings/{id}`| Valid Token, Booking `123` belongs to User | `DELETE` | `Authorization: Bearer <t>` | None | 1. Send DELETE request for valid booking. | `200` | `{"message": "Booking cancelled successfully"}` | High (Positive) |
| **TC_BKG_009** | TS_BKG_05 | `/api/v1/bookings/{id}`| Valid Token, Booking `123` is cancelled | `DELETE` | `Authorization: Bearer <t>` | None | 1. Send DELETE request for already cancelled booking. | `400` | `{"error": "Booking already cancelled"}` | Medium (Negative) |
| **TC_BKG_010** | TS_BKG_04 | `/api/v1/bookings/{id}`| Valid Token | `DELETE` | `Authorization: Bearer <t>` | None | 1. Send DELETE request for non-existent booking `9999`. | `404` | `{"error": "Booking not found"}` | High (Negative) |
| **TC_BKG_011** | TS_BKG_04 | `/api/v1/bookings/{id}`| Valid Token | `DELETE` | `Authorization: Bearer <t>` | None | 1. Send DELETE request with ID format `abc`. | `400` | `{"error": "Invalid ID format"}` | Medium (Negative) |

## 4. History Module

| TC ID | TS ID | Endpoint | Preconditions | Method | Headers | Body Payload | Test Steps | Expected Code | Expected Response | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC_HIS_001** | TS_HIS_01 | `/api/v1/user/bookings` | Valid Token, User has 2 active bookings | `GET` | `Authorization: Bearer <t>` | None | 1. Send GET request for history. | `200` | Array of 2 booking objects | High (Positive) |
| **TC_HIS_002** | TS_HIS_02 | `/api/v1/user/bookings` | Valid Token, User has 0 bookings | `GET` | `Authorization: Bearer <t>` | None | 1. Send GET request for history. | `200` | `[]` | Medium (Boundary) |
| **TC_HIS_003** | TS_HIS_01 | `/api/v1/user/bookings` | Valid Token, User has 1 active, 1 cancelled | `GET` | `Authorization: Bearer <t>` | None | 1. Send GET request. 2. Verify statuses in array. | `200` | Array containing `ACTIVE` and `CANCELLED` status fields | Medium (Positive) |
| **TC_HIS_004** | TS_HIS_03 | `/api/v1/user/bookings?status=active` | Valid Token, User has mixed bookings | `GET` | `Authorization: Bearer <t>` | None | 1. Send GET request with URL query parameter `status=active`. | `200` | Array containing ONLY bookings with `ACTIVE` status | Low (Positive) |
| **TC_HIS_005** | TS_HIS_03 | `/api/v1/user/bookings?limit=1000` | Valid Token | `GET` | `Authorization: Bearer <t>` | None | 1. Send GET request with a very high limit parameter. | `200/400` | Truncated array OR error enforcing max limit (e.g. 100) | Low (Boundary) |

## 5. Authorization & Security Module

| TC ID | TS ID | Endpoint | Preconditions | Method | Headers | Body Payload | Test Steps | Expected Code | Expected Response | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC_SEC_001** | TS_AUTHZ_01 | `/api/v1/bookings` | None (No Token provided) | `POST` | `Content-Type: application/json` | `{"movie_id": 1, "seats": 2}` | 1. Send POST request WITHOUT `Authorization` header. | `401` | `{"error": "Missing authorization token"}` | High (Security) |
| **TC_SEC_002** | TS_AUTHZ_02 | `/api/v1/user/bookings` | Token has expired | `GET` | `Authorization: Bearer <expired_t>` | None | 1. Send GET request using an expired JWT. | `401` | `{"error": "Token expired"}` | High (Security) |
| **TC_SEC_003** | TS_AUTHZ_02 | `/api/v1/bookings/1` | Invalid JWT string | `DELETE`| `Authorization: Bearer random123` | None | 1. Send DELETE using a fake/malformed token string. | `401` | `{"error": "Invalid token"}` | High (Security) |
| **TC_SEC_004** | TS_AUTHZ_03 | `/api/v1/bookings/{id}` | Token of User B, Booking ID belongs to User A | `DELETE`| `Authorization: Bearer <user_b_t>`| None | 1. Send DELETE requesting cancellation of User A's booking. | `403` | `{"error": "Forbidden: You do not own this booking"}` | High (Security) |
| **TC_SEC_005** | TS_AUTHZ_01 | `/api/v1/auth/login` | None | `POST` | `Content-Type: application/json` | `{"email": "' OR '1'='1", "password": "pwd"}` | 1. Attempt basic SQL injection in the email field. | `401` | `{"error": "Invalid credentials"}` | High (Security) |
| **TC_SEC_006** | TS_AUTHZ_01 | `/api/v1/bookings` | Valid Token | `POST` | `Authorization: Bearer <t>`, `Content-Type: application/json` | `{"movie_id": 1, "seats": 2, "price": 0}` | 1. Attempt mass assignment attack by injecting `price=0`. | `201` | Successful booking, but injected price is ignored | Medium (Security) |
| **TC_SEC_007** | TS_AUTHZ_01 | `/api/v1/movies/1` | None | `GET` | None | None | 1. Send GET request to public route without auth header. | `200` | Movie details (Validates public routes stay public) | Medium (Security) |

## 6. Error Handling & Edge Cases Module

| TC ID | TS ID | Endpoint | Preconditions | Method | Headers | Body Payload | Test Steps | Expected Code | Expected Response | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC_ERR_001** | TS_ERR_01 | `/api/v1/bookings` | Valid Token | `POST` | `Authorization: Bearer <t>`, `Content-Type: application/json` | `{movie_id: 1, seats: 2` (broken JSON) | 1. Send POST with syntax-broken JSON. | `400` | `{"error": "Malformed JSON payload"}` | Medium (Negative) |
| **TC_ERR_002** | TS_ERR_02 | `/api/v1/movies` | None | `POST` | None | None | 1. Send POST request to a route that only accepts GET. | `405` | `{"error": "Method Not Allowed"}` | Low (Negative) |
| **TC_ERR_003** | TS_ERR_03 | `/api/wrong_path` | None | `GET` | None | None | 1. Send request to a completely invalid URL path. | `404` | `{"error": "Endpoint not found"}` | Low (Negative) |
| **TC_ERR_004** | TS_ERR_01 | `/api/v1/auth/register` | None | `POST` | `Content-Type: application/json` | Huge payload (>10MB string) | 1. Send POST with excessively large JSON body to test server limits. | `413` | `{"error": "Payload Too Large"}` | Medium (Boundary) |
