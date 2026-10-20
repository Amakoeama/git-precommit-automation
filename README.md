
# Local Commit-Stage Automation with Git Hooks

![Python CI Pipeline](https://github.com/Amakoeama/git-precommit-automation/actions/workflows/ci.yml/badge.svg)

#--- Overview ---

This project demonstrates local commit-stage automation using a Git pre-commit hook. The hook automatically runs code quality checks before Git allows a commit to be completed.

The project uses Python with Flake8 for linting and PyTest for unit testing.

#--- Project Structure ---

- `src/calculator.py` - Sample Python source code
- `tests/test_calculator.py` - Unit test for the calculator
- `hooks/pre-commit` - Pre-commit hook script
- `requirements.txt` - Python development dependencies

#--- Setup ---

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required tools: 

```bash
pip install -r requirements.txt
```

Install the Git hook:

```bash
cp hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
#--- How the Hook Works ---

Before each commit, the hook runs Flake8 to check Python code quality and then runs PyTest to execute the unit tests.

If either check fails, the hook exits with a nonzero status and Git blocks the commit. If both checks pass, the commit is allowed to continue.

#--- Manual Validation ---

Run the linter:

```bash
flake8 src tests
```

Run the unit tests:

```bash
python -m pytest -q
```

#--- Advantages and Limitations ---

Local Git hooks provide immediate feedback before code enters the repository history. They can prevent common formatting problems and failing tests from being committed.

One limitation is that Git hooks are local to each repository clone and are not automatically installed when another developer clones the repository. Developers can also modify or bypass local hooks. For team projects, local hooks are therefore best combined with CI/CD validation.

---

# ITSD-4350 Midterm Project: Version Control and Continuous Integration

## Project Overview

This midterm project demonstrates a Git-based development workflow and an automated continuous integration pipeline using GitHub Actions.

The project includes a Flask web application, automated Python tests, code quality checks, and build validation.

## Technology Stack

- Python 3.10 for GitHub Actions
- Flask web framework
- Pytest for automated testing
- Flake8 for code quality checks
- Git and GitHub for version control
- GitHub Actions for continuous integration

## Running the Web Application

Install the project dependencies:

```bash
python -m pip install -r requirements.txt 
```


Start the Flask application:

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Automated Testing and Build Validation

Run automated tests:

```bash
python -m pytest -v
```

Run code quality checks:

```bash
python -m flake8 app.py src tests
```

Validate Python syntax:

```bash
python -m compileall -q app.py src
```

## Continuous Integration Pipeline

The GitHub Actions workflow is located at `.github/workflows/ci.yml`.

The pipeline performs the following steps:

1. Checks out the repository.
2. Sets up Python 3.10.
3. Installs dependencies.
4. Validates Python syntax.
5. Runs Flake8 code quality checks.
6. Executes automated tests with Pytest.
7. Confirms successful build validation.

### CI Triggers

The workflow executes on:

- Pushes to `main`, `develop`, and `feature/**` branches.
- Pull requests targeting `main` or `develop`.

## Branching Strategy

The project uses a feature-branch workflow.

- `main`: Stable project branch.
- `develop`: Optional integration branch for future development.
- `feature/*`: Branches for individual features.

The Flask application was developed on `feature/flask-web-app` and submitted through pull request #1.

## Commit Message Standards

The project follows Conventional Commit naming conventions.

Examples:

- `feat: add Flask web application and automated CI validation`
- `fix: correct GitHub Actions workflow YAML syntax`
- `docs: document midterm CI workflow and branching strategy`

Common prefixes include `feat`, `fix`, `docs`, `test`, and `chore`.

## Pull Request and Code Review Process

1. Create a feature branch from `main`.
2. Implement changes and run local tests.
3. Commit changes using meaningful messages.
4. Push the feature branch to GitHub.
5. Open a pull request targeting `main`.
6. Review changed files and automated CI results.
7. Request a reviewer when available.
8. Address feedback and rerun CI as needed.
9. Merge after required checks and reviews are satisfied.

## CI Troubleshooting

The initial GitHub Actions workflow failed because of a YAML syntax error.

The error was corrected in a separate fix commit. A subsequent push workflow completed successfully.

This demonstrates how automated CI feedback helps identify and resolve configuration problems.

## Midterm Evidence

The project demonstrates:

- A working Flask web application.
- Automated CI execution on push.
- Automated CI execution on pull request.
- Feature-branch development.
- Meaningful commit messages.
- Pull request creation and CI validation.

Repository: https://github.com/Amakoeama/git-precommit-automation
