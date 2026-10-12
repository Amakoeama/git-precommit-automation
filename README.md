
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

Install the required tools:

pip install -r requirements.txt

Install the Git hook:

cp hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

#--- How the Hook Works ---

Before each commit, the hook runs Flake8 to check Python code quality and then runs PyTest to execute the unit tests.

If either check fails, the hook exits with a nonzero status and Git blocks the commit. If both checks pass, the commit is allowed to continue.

#--- Manual Validation ---

Run the linter:

flake8 src tests

Run the unit tests:

python -m pytest -q

#--- Advantages and Limitations ---

Local Git hooks provide immediate feedback before code enters the repository history. They can prevent common formatting problems and failing tests from being committed.

One limitation is that Git hooks are local to each repository clone and are not automatically installed when another developer clones the repository. Developers can also modify or bypass local hooks. For team projects, local hooks are therefore best combined with CI/CD validation.


# Mini Project 1.4: CI Quality Gate and Reporting 

## Objective
Extend the existing GitHub Actions CI pipeline with automated code quality, test coverage, security scanning, and static analysis checks.

## Quality Gates
- Build: Python source compilation must succeed.
- Linting: Flake8 must report zero errors.
- Testing: All pytest unit tests must pass.
- Coverage: Minimum 80%, enforced by pytest-cov.
- Security: Trivy fails CI on CRITICAL vulnerabilities.
- Static analysis: SonarQube Cloud scans code and reports quality gate status.
- Branch protection: The main branch requires pull requests and a passing build-and-test status check.

## Verified Results
- Unit tests: 1 passed
- Test coverage: 100%
- Flake8 errors: 0
- Trivy CRITICAL vulnerabilities: 0
- SonarQube quality gate: PASSED
- SonarQube new issues: 0
- GitHub Actions: PASSED

## Reports
HTML coverage: htmlcov/index.html
XML coverage: coverage.xml
GitHub Actions artifact: coverage-reports

SonarQube dashboard:
https://sonarcloud.io/dashboard?id=Amakoeama_git-precommit-automation&branch=mini-project-1.4-quality-gates

Coverage reports can be regenerated locally or downloaded from GitHub Actions artifacts.

## Local Verification
Install dependencies:
    python -m pip install -r requirements.txt

Run Flake8:
    python -m flake8 src tests

Run tests and enforce coverage:
    python -m pytest --cov=src --cov-report=html:htmlcov --cov-report=xml:coverage.xml --cov-fail-under=80

Verify the build:
    python -m compileall src

## CI Failure Demonstration
Commit bde1ffe intentionally introduced an unused import.

Flake8 detected F401, E305, and E402 errors, causing CI to fail.

Commit 7e4a929 reverted those changes and restored the successful pipeline.

## Quality Analysis
Automated checks provide consistent feedback before code advances through delivery. The sample module achieved 100% test coverage, although coverage alone does not guarantee complete testing. Flake8 successfully rejected intentional violations, while Trivy reported zero CRITICAL vulnerabilities in the scanned dependencies.

SonarQube reported a passing quality gate and zero new issues. Its dashboard did not calculate new-code coverage because there were insufficient new lines. The 80% coverage requirement is independently enforced by pytest-cov in GitHub Actions.

Together, these controls demonstrate how automated testing, static analysis, security scanning, and branch protection reduce delivery risk.