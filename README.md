
# Local Commit-Stage Automation with Git Hooks

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
