# Document Library

This is a demo project to showcase building a restful python flask application.

## You can find the following demonstrations in this project:

1. Dependencies listed in requirements.txt for the creation of a suitable virtual environment.
2. CI Pipeline defined as a github action workflow in `.github/workflows/ci.yaml`. The pipeline does the following:
    - Check code format using `black`
    - Lint the code using `flake8`
    - Run rests and create code coverage report using `pytest`, and `pytest-cov`
3. Configurations for the database connnection is read dynamically from a dot env file.
4. For testing, an in-memory sql-lite databse is used.
5. Simple blueprint with routes defined for document upload and retrieval.
6. A useful .gitignore file to help with version control.
