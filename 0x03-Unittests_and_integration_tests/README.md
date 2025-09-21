# 0x03. Unittests and Integration Tests

This project covers writing effective **unit tests** and **integration tests** in Python using the `unittest` framework.  
It focuses on mocking, parametrization, fixtures, and testing best practices.

## Learning Objectives
By the end of this project, you should be able to explain:
- The difference between unit and integration tests.
- How to apply mocking to isolate code under test.
- Common testing patterns such as parametrization and fixtures.
- How to implement memoization tests.
- How to run tests using `python -m unittest`.

## Requirements
- All code will be executed on **Ubuntu 18.04 LTS** using **Python 3.7**.
- Files must follow **pycodestyle** (PEP8) style guide.
- All files must be executable and end with a new line.
- The first line of every file should be `#!/usr/bin/env python3`.
- Each module, class, and function must include proper documentation.
- All functions and coroutines must have type annotations.

## Project Structure
```
alx-backend-python/
└── 0x03-Unittests_and_integration_tests/
    ├── utils.py
    ├── client.py
    ├── fixtures.py
    ├── test_utils.py
    ├── test_client.py
    └── README.md
```

## Tasks Overview
1. **Unit Tests for utils.access_nested_map**
   - Test with multiple inputs using `parameterized.expand`.
   - Test KeyError exceptions.

2. **Mock HTTP Calls**
   - Test `utils.get_json` using `unittest.mock.patch`.

3. **Test Memoization**
   - Verify `@memoize` decorator only calls a method once.

4. **Client Tests**
   - Test `GithubOrgClient.org`, `_public_repos_url`, `public_repos`, and `has_license` methods.

5. **Integration Tests**
   - Use `fixtures.py` to run end-to-end tests for `GithubOrgClient.public_repos`.

## Running Tests
Run all tests with:
```bash
python -m unittest discover 0x03-Unittests_and_integration_tests
```

Run a specific test file:
```bash
python -m unittest 0x03-Unittests_and_integration_tests/test_utils.py
```

## Resources
- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [parameterized](https://pypi.org/project/parameterized/)
- [Memoization in Python](https://en.wikipedia.org/wiki/Memoization)
