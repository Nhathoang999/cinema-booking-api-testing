# Defect Report: Cinema Booking API

## Defect 1: BUG-001

**ID:** BUG-001  
**Title:** Negative Seat Booking Accepted  
**Related Test Case:** TC_BKG_005  
**Severity:** High  
**Priority:** High  
**Status:** Open  

### Environment
- **Server:** Local Testing Sandbox (`http://localhost:8000`)
- **API Version:** v1.0.0
- **Database:** SQLite

### Preconditions
- The testing database is seeded with movies.
- The tester is registered, logged in, and holds a valid JWT authentication token.

### Steps To Reproduce
1. Open Postman or execute via Newman.
2. Send a `POST` request to `/api/v1/bookings`.
3. Include the header: `Authorization: Bearer <valid_token>`.
4. Include the following JSON payload in the request body:
   ```json
   {
       "movie_id": 1,
       "seats": -5
   }
   ```
5. Execute the request and observe the response code and body.

### Expected Result
The API payload validator should instantly reject the negative integer. It must return a `400 Bad Request` status code with the standard JSON error schema:
```json
{
    "error_code": "VALIDATION_ERROR",
    "message": "Seats must be greater than 0"
}
```

### Actual Result
The validation layer fails to catch the negative value. The request either crashes throwing a `500 Internal Server Error`, or improperly updates the database by mathematically subtracting negative seats (effectively increasing the available seat pool).

### Root Cause Analysis
The `BookingCreate` schema located in `app/schemas.py` is likely missing or incorrectly applying the Pydantic boundary constraint. The field is defined as `seats: int` without the strictly enforced `Field(gt=0)` parameter. Consequently, negative numbers successfully pass through the router and inject corrupt logic into the database transaction.

---

## Defect 2: BUG-002

**ID:** BUG-002  
**Title:** User Can Cancel Another User Booking  
**Related Test Case:** TC_SEC_004  
**Severity:** Critical  
**Priority:** High  
**Status:** Open  

### Environment
- **Server:** Local Testing Sandbox (`http://localhost:8000`)
- **API Version:** v1.0.0
- **Database:** SQLite

### Preconditions
- **User A** is registered and has successfully booked a ticket (e.g., resulting in Booking ID: `123`).
- **User B** is registered, logged in, and holds their own valid JWT authentication token.

### Steps To Reproduce
1. Send a `DELETE` request to `/api/v1/bookings/123` (targeting User A's booking).
2. Include the header: `Authorization: Bearer <User_B_Token>`.
3. Execute the request and observe the response.

### Expected Result
The API should query the database, verify that `booking.user_id` does not match the token's authenticated `user_id`, and immediately reject the cancellation. It should return a `403 Forbidden` status code.

### Actual Result
The API successfully cancels the booking on behalf of User A and returns `200 OK`, bypassing ownership validation entirely.

### Root Cause Analysis
This is an Insecure Direct Object Reference (IDOR) vulnerability. In `app/crud.py`, the `cancel_booking` function fetches the target booking by ID but skips the authorization check. It fails to implement the strict programmatic constraint:
```python
if booking.user_id != user_id:
    raise HTTPException(status_code=403, detail="Forbidden")
```
As a result, any authenticated user can cancel any booking in the database if they know or guess the `booking_id`.
