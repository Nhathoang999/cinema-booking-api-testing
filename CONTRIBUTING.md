# Contributing to Cinema Booking API Testing

Thank you for your interest in contributing to this project! This repository demonstrates an end-to-end Enterprise QA Workflow. We welcome contributions that align with our QA automation goals.

## 1. Coding Style

- Follow PEP 8 for Python code (`tests/`, `scripts/`, `ai/`).
- Use `black` for code formatting and `isort` for import sorting.
- Use `flake8` for linting.

## 2. Branch Naming

Use the following prefixes for branch names:
- `feat/`: A new feature or test suite
- `fix/`: A bug fix or script correction
- `docs/`: Documentation updates
- `refactor/`: Refactoring code or tests
- `chore/`: Maintenance tasks (e.g., dependency updates)

Example: `feat/add-booking-schema-validation`

## 3. Commit Convention

We strictly follow [Conventional Commits](https://www.conventionalcommits.org/).

**Format**: `<type>(<scope>): <description>`

**Types**:
- `feat`: A new feature (e.g., new test cases, new script)
- `fix`: A bug fix
- `docs`: Documentation only changes
- `test`: Adding missing tests or correcting existing tests
- `ci`: Changes to our CI configuration files and scripts
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `chore`: Other changes that don't modify `src` or `test` files

**Examples**:
- `feat(qa): add business requirements document`
- `test(api): add schema validation for booking endpoint`
- `docs(test): create release checklist`
- `ci: add Azure DevOps pipeline`
- `refactor(metrics): generate QA dashboard automatically`

## 4. Testing Workflow

1. Setup the backend locally using `docker-compose up` (if using Docker) or natively via `venv`.
2. Ensure you have the `requirements-dev.txt` installed.
3. Add your new test cases to the appropriate suite (Postman, Newman, or Pytest).
4. Run `python scripts/run-all.py` locally to verify that all tests pass, the database asserts correctly, and metrics generate without error.

## 5. Pull Request Checklist

Before submitting a Pull Request, please ensure the following:
- [ ] Your code follows the coding guidelines.
- [ ] You have formatted your code with `black` and `isort`.
- [ ] Your commit messages follow the Conventional Commits format.
- [ ] You have updated the relevant documentation (`docs/`, `README.md`) if necessary.
- [ ] You have run `scripts/run-all.py` and all tests pass.
