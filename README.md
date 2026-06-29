# Cinema Booking API Testing
**Manual Testing • API Automation • AI-assisted QA • Azure DevOps**

This project demonstrates an end-to-end Enterprise QA workflow for a RESTful Cinema Booking API. It covers requirement analysis, manual testing, API automation, database validation, AI-assisted test design, and CI/CD integration.

---

## 1. Overview
The goal of this repository is to showcase a structured approach to Quality Assurance, bridging the gap between Business Analysis (BA) and Automation Engineering. The API under test is built with FastAPI and SQLite.

## 2. Architecture & QA Workflow

The project strictly follows a traceability and execution pipeline:

```ascii
Business Requirements
        │
        ▼
Functional Requirements
        │
        ▼
User Stories
        │
        ▼
Acceptance Criteria
        │
        ▼
Test Scenarios & Cases
        │
        ▼
API Automation (Newman/Pytest)
        │
        ▼
Database Validation
        │
        ▼
Metrics & Reports
        │
        ▼
Release
```

## 3. Features
- **Requirements Traceability**: Python-generated RTM linking BRs down to Test Cases.
- **AI Gap Analysis**: Human-in-the-loop Gemini API script that reviews existing test cases and suggests missing boundary conditions.
- **API Contract Validation**: Postman JSON schema validation.
- **Multi-layer Automation**: End-to-End flows tested in Newman, unit/integration layer tested in Pytest.
- **Database Verification**: Python scripts directly query SQLite to assert backend states.

## 4. Tech Stack
- **API**: FastAPI, Python 3.12, SQLite
- **Automation**: Postman, Newman, Pytest, `requests`
- **CI/CD & DevOps**: Docker, Azure Pipelines, GitHub Actions
- **AI/Scripting**: Google Generative AI (Gemini), `openpyxl`, `pandas`

## 5. Project Structure
See `docs/environment.md` for full environment specs.
- `docs/`: Planning, requirements, strategies, risk analysis.
- `artifacts/templates/`: Test case and RTM Excel templates.
- `ai/`: Gap analysis scripts and QA review outcomes.
- `tests/`: Pytest fixtures and assertions.
- `test-data/`: JSON datasets for data-driven testing.
- `scripts/`: Orchestration (`run-all.py`) and DB validation.

## 6. Quick Start

**Run the API locally (Docker):**
```bash
docker-compose up -d
```

**Run the QA Automation Workflow:**
```bash
python scripts/run-all.py
```
This script acts as the QA Automation Runner executing health checks, Newman, Pytest, DB assertions, and metrics generation.

## 7. Defect Management Lifecycle
```
New -> Assigned -> In Progress -> Resolved -> Retest -> Closed
```
*(Duplicate, Rejected, and Deferred states are utilized where applicable).*

## 8. CI/CD Integration
The project features dual-pipeline architecture:
- **Azure DevOps**: Primary enterprise pipeline handling artifacts, test plans, and boards.
- **GitHub Actions**: Public-facing CI workflow demonstrating automated test execution on push.

## 9. Documentation
- [QA Dashboard (Metrics & Coverage)](reports/qa-dashboard.md)
- [Test Plan](docs/test-plan.md)
- [Test Strategy & Design Techniques](docs/test-strategy.md)
- [Requirements & Traceability](docs/requirements.md)
- [AI QA Gap Analysis](ai/review-result.md)

## 10. Future Improvements
- Performance Testing using **k6**
- Security Testing utilizing **OWASP ZAP**
- Accessibility Testing utilizing **axe-core** (if UI is developed)
