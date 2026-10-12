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
