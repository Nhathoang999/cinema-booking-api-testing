# Business and Functional Requirements

This document outlines the core requirements for the Cinema Booking API, mapping high-level business goals to specific functional requirements. This serves as the foundation for our QA traceability matrix.

## 1. Authentication Module

### Business Requirement (BR-01)
The system must ensure that only authorized users can book tickets or view their booking history.

#### Functional Requirements
- **FR-01.1**: The system shall provide an endpoint for new users to register using an email and password.
- **FR-01.2**: The system shall provide an endpoint for users to log in and receive a JSON Web Token (JWT).
- **FR-01.3**: The system shall validate the JWT on all protected endpoints and return a `401 Unauthorized` if invalid or missing.

## 2. Movie Management Module

### Business Requirement (BR-02)
Customers must be able to browse available movies to decide what to watch.

#### Functional Requirements
- **FR-02.1**: The system shall provide an endpoint to list all available movies currently showing.
- **FR-02.2**: Each movie record shall contain a unique ID, title, genre, and duration.

## 3. Booking Module

### Business Requirement (BR-03)
Customers must be able to book tickets for a movie and subsequently manage or review their bookings.

#### Functional Requirements
- **FR-03.1**: The system shall allow an authenticated user to create a booking for a specific movie ID.
- **FR-03.2**: The system shall return a unique booking confirmation ID upon successful booking.
- **FR-03.3**: The system shall allow an authenticated user to retrieve a history of all their past and active bookings.
- **FR-03.4**: The system shall allow an authenticated user to cancel an existing booking they own, provided it has not already been cancelled.
- **FR-03.5**: The system shall prevent users from canceling bookings that belong to other users.
