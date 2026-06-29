# QA Risk Analysis & Mitigation

This document identifies potential risks to the Cinema Booking API testing and outlines strategies to mitigate them.

| Risk ID | Risk Description | Impact (H/M/L) | Probability (H/M/L) | Mitigation Strategy |
| :--- | :--- | :--- | :--- | :--- |
| **R-01** | Database locking issues during concurrent booking attempts. | High | Medium | Implement automated testing scripts (planned for future) using k6 to simulate concurrent load on the SQLite DB. |
| **R-02** | Expiry of JWT tokens during automated test runs causes false negatives. | High | Low | Configure Pytest and Postman collections to authenticate and fetch a fresh token dynamically at the start of each suite. |
| **R-03** | Lack of test data isolation causes tests to fail due to duplicate bookings. | Medium | High | Use the `scripts/verify-db.py` to assert states, and implement tear-down functions in Pytest to clear created data after tests. |
| **R-04** | Security vulnerabilities such as SQL Injection or IDOR. | High | Medium | Explicitly include Security Test Cases covering invalid inputs and cross-user booking access. Future integration of OWASP ZAP. |
| **R-05** | Backend schema changes break the API automation runner. | High | Low | Implement robust JSON Schema validation in Postman to catch contract breaches immediately before functional assertions fail. |
