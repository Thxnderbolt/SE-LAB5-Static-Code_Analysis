# Lab 5 Reflection

## 1. Which issues were the easiest to fix, and which were the hardest? Why?

**Easiest:** Style issues like adding blank lines, removing unused imports, and fixing string formatting were straightforward since they only required minor syntax changes without affecting logic.

**Hardest:** The mutable default argument issue was trickiest because it required understanding how Python handles default arguments and implementing the None-check pattern correctly to avoid the shared state bug.

## 2. Did the static analysis tools report any false positives?

The "global statement" warning (W0603) could be considered a borderline case. While using global variables isn't ideal, in this small script it's intentional for the stock_data dictionary. However, it's not technically a false positive since globals should generally be avoided.

## 3. How would you integrate static analysis tools into your actual software development workflow?

I would integrate these tools in multiple ways:
- **Pre-commit hooks**: Run Flake8 automatically before each commit to catch style issues immediately
- **CI/CD pipeline**: Include Pylint and Bandit in GitHub Actions to prevent merging code with quality/security issues
- **IDE integration**: Configure VS Code/PyCharm to show Pylint warnings in real-time while coding
- **Code review process**: Make passing all three tools a requirement before PR approval

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

- **Security**: Removed eval() eliminated a critical vulnerability
- **Reliability**: Fixed mutable default argument prevents subtle bugs with shared state
- **Maintainability**: Snake_case naming and docstrings make code more readable and self-documenting
- **Robustness**: Using context managers ensures files are properly closed even if errors occur
- **Debugging**: Specific exception handling makes it easier to identify and fix errors