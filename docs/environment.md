# Test Environment

This document lists the environment configurations used for executing the QA workflows in this project.

## Local Execution Environment

| Item | Version | Description |
| :--- | :--- | :--- |
| **OS** | Windows 11 / Linux | Developer local machine |
| **Python** | 3.12+ | Required for FastAPI backend and Python scripts |
| **Node.js** | 18+ | Required for running Newman |
| **FastAPI** | 0.109+ | Web framework for the Backend API |
| **SQLite** | 3.x | Lightweight relational database |
| **Postman** | v10+ | API test design and contract validation |
| **Newman** | 6.x | CLI runner for Postman collections |
| **Pytest** | 8.x | Python testing framework |

## Docker Execution Environment (CI Simulation)

| Item | Image | Description |
| :--- | :--- | :--- |
| **Backend API** | `python:3.12-slim` | Runs the FastAPI Uvicorn server |
| **API Runner** | `postman/newman:alpine`| Containerized execution of Postman collections |

## Azure DevOps CI/CD Pipeline

| Item | Agent/Tool | Description |
| :--- | :--- | :--- |
| **Pipeline Agent** | `ubuntu-latest` | Microsoft-hosted agent for running CI jobs |
| **Python Task** | `UsePythonVersion@0`| Provisions Python 3.12 environment |
| **Node Task** | `NodeTool@0` | Provisions Node.js environment |
