# Release Notes - v1.0

**Release Date:** 2026-06-30

This is the initial production release of the Cinema Booking API.

## New Features
- **Authentication**: Users can register and login to receive JWT tokens for session management.
- **Movies**: Browse list of current movies and view movie details.
- **Booking Management**: 
  - Authenticated users can book tickets (seats) for a specific movie.
  - View personal active and past bookings.
  - Cancel active bookings.

## QA & Testing Summary
- Delivered robust End-to-End API automation suite using **Newman** and **Pytest**.
- Conducted AI Gap Analysis to secure edge cases (added TC015, TC016).
- RTM demonstrates 100% coverage of all baseline Business Requirements.
- CI/CD pipelines configured via Azure DevOps and GitHub Actions.

## Known Issues (Deferred)
- **BUG-005**: Response time for `GET /movies` spikes above 500ms when concurrent users > 1000. Mitigation: Planned indexing and caching in v1.1.
- **BUG-012**: Missing validation for negative seat counts in `POST /bookings`. Currently handled by DB constraints but missing 422 API response. Scheduled for next sprint.

## Deployment Instructions
Refer to the `README.md` and `docker-compose.yml` for automated deployment and health check steps.
