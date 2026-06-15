# Test Execution Report: Cinema Booking API

## 1. Document Information
- **Tester:** QA Lead / Test Automation Engineer
- **Execution Date:** 2026-06-15
- **Environment:** Local Testing Sandbox (`http://localhost:8000`)
- **Testing Type:** API Testing (Postman / Newman Automation)

---

## 2. Test Summary

| Metric | Count | Percentage |
| :--- | :---: | :---: |
| **Total Test Cases** | 42 | 100% |
| **Executed** | 42 | 100% |
| **Passed** | 40 | 95.2% |
| **Failed** | 2 | 4.8% |
| **Blocked** | 0 | 0.0% |

**Overall Status:** <span style="color:orange">**CONDITIONAL PASS**</span>

---

## 3. Failed Test Cases Details

### Defect 1: TC_BKG_005
- **Module:** Booking
- **Test Case Name:** Book zero or negative seats
- **Severity:** Medium
- **Description:** Attempting to submit a POST request to `/api/v1/bookings` with a requested seat count of `-5`. 
- **Expected Result:** The API should validate the payload and return a `400 Bad Request` with `{"error": "Seats must be greater than 0"}`.
- **Actual Result:** The validation failed to trigger at the payload level, resulting in an internal database integrity error (`500 Internal Server Error`).

### Defect 2: TC_SEC_004
- **Module:** Authorization & Security
- **Test Case Name:** Cancel another user's booking
- **Severity:** High (Security Flaw)
- **Description:** Sending a `DELETE /api/v1/bookings/{id}` request where the `{id}` belongs to User A, but the `Authorization: Bearer <token>` belongs to User B.
- **Expected Result:** The API should verify resource ownership and return a `403 Forbidden`.
- **Actual Result:** The API successfully cancelled the booking (`200 OK`) and bypassed the ownership validation layer, allowing cross-user data manipulation.

---

## 4. Recommendations & Next Steps
1. **TC_BKG_005 Fix:** Review the Pydantic `Field(gt=0)` constraints in `schemas.py` to ensure negative numbers are intercepted before reaching the database router logic.
2. **TC_SEC_004 Fix:** Immediately patch the `cancel_booking` CRUD operation. Ensure the SQL query validates `booking.user_id == current_user.id` before executing the cancellation update. 
3. After fixes are deployed, re-run the `newman` automated test suite to verify the regression passes without breaking the 40 currently passing tests.
