# DevOps Core Tooling

[![Python CI](https://img.shields.io/github/actions/workflow/status/DhirajCloud/devops-core-tooling/ci.yml?branch=main&label=build)](https://github.com/DhirajCloud/devops-core-tooling/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)

A foundational Python project demonstrating professional Git workflows, modular application structure, automated testing, code quality checks, and GitHub Actions CI.

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Testing and Code Quality](#testing-and-code-quality)
- [CI Workflow](#ci-workflow)
- [Project Structure](#project-structure)
- [Security Notes](#security-notes)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [License](#license)

## Overview

DevOps Core Tooling is a learning and demonstration repository for core software engineering and DevOps practices.

The project includes:
- A Python application entry point.
- Dashboard summary and display utilities.
- Demonstration authentication and logging modules.
- Central application configuration.
- Automated unit tests using Pytest.
- Code quality checks using Flake8.
- GitHub Actions automation for continuous integration.

## Architecture

The application uses a simple modular structure. GitHub Actions validates code changes through linting and automated tests.

### System Architecture Diagram

```mermaid
flowchart TD
    A[Developer] --> B[Git Repository]
    B --> C[GitHub]
    C --> D[GitHub Actions]
    D --> E[Install Dependencies]
    E --> F[Flake8 Code Quality]
    F --> G[Pytest Unit Tests]
    G --> H[CI Result]
    B --> I[Python Application]
    I --> J[Dashboard]
    I --> K[Authentication Demo]
    I --> L[Logger]
    I --> M[Configuration]
