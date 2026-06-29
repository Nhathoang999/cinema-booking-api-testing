# QA Dashboard: Cinema Booking API

This dashboard aggregates the metrics and coverage across the entire test suite.

## 1. API Coverage

| Endpoint | Tested | Automation |
| :--- | :--- | :--- |
| `POST /register` | ✅ | ✅ |
| `POST /login` | ✅ | ✅ |
| `GET /movies` | ✅ | ✅ |
| `GET /movies/{id}` | ✅ | ❌ |
| `POST /bookings` | ✅ | ✅ |
| `DELETE /bookings/{id}`| ✅ | ✅ |
| `GET /user/bookings` | ✅ | ✅ |

**Overall API Coverage: 100% (Manual) / 85% (Automated)**

## 2. Requirement Coverage (Traceability)

- **Total Functional Requirements**: 9
- **Total User Stories**: 6
- **Test Scenarios**: 12
- **RTM Coverage**: 100% (All FRs mapped to at least one Test Case).

## 3. Automation Execution Metrics

*(Data pulled automatically from `metrics/test-metrics.md`)*

- **Pass Rate**: 96.3%
- **Total Executed**: 82
- **Failed**: 3

## 4. Defect Summary

| Severity | New | Assigned | In Progress | Resolved | Retest | Closed |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Critical** | 0 | 0 | 0 | 0 | 0 | 2 |
| **High** | 0 | 0 | 0 | 1 | 0 | 1 |
| **Medium** | 1 | 2 | 1 | 0 | 0 | 4 |
| **Low** | 0 | 1 | 0 | 0 | 0 | 8 |

## 5. Release Status
- [x] Pre-flight DB Check
- [x] Automation Pass
- [x] QA Sign-off
- **Decision**: GO for deployment.
