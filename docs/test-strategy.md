# Test Strategy

This document describes the testing techniques and levels applied to the Cinema Booking API.

## 1. Testing Levels

### Functional Testing
Validating the API against the provided business requirements and user stories to ensure core features (Auth, Booking, Movies) work as expected.

### API Contract Testing
Verifying that API responses strictly adhere to predefined JSON Schemas. This prevents frontend parsing errors if the backend unexpectedly changes response structures.

### Security & Authorization Testing
Ensuring that JWT tokens are correctly validated. Testing access control to prevent users from interacting with bookings they do not own (IDOR - Insecure Direct Object Reference prevention).

### Database Verification
Bypassing the API layer and querying the SQLite database directly using Python to assert that API actions correctly altered the persistent storage state.

## 2. Automation Strategy

- **Postman/Newman**: Primary tool for API E2E workflows and schema validation.
- **Pytest**: Used for targeted, programmatic testing of core authentication and booking logic utilizing reusable fixtures.
- **Python Scripts**: Custom orchestration for metrics generation, Database validation, and Requirement Traceability Matrix (RTM) generation.

## 3. Test Design Techniques

To ensure comprehensive coverage, the following formal QA techniques will be used when designing test cases:

- **Equivalence Partitioning (EP)**: Dividing input data into valid and invalid partitions. (e.g., Valid Email Format vs. Invalid Email Format).
- **Boundary Value Analysis (BVA)**: Testing the edges of input constraints. (e.g., Password length = 5, 6, 7 chars).
- **Error Guessing**: Using experience to anticipate common developer mistakes (e.g., sending Empty JSON `{}` or omitting required headers).
- **State Transition**: Testing the lifecycle of a booking (e.g., Create -> Cancel -> Attempt to Cancel Again).

*Note: Each manual test case in the Excel artifact will explicitly state the Test Design Technique used.*
