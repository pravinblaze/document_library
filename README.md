# Document Library

This is a demo project to showcase building a restful python flask application.

## You can find the following demonstrations in this project:

1. Dependencies listed in requirements.txt for the creation of a suitable virtual environment.
2. Defined a simple data model for tracking document in the databse.
3. Used flask migrate to initialize and create corresponding schema.
4. Simple blueprint with routes defined for document upload and retrieval.
5. Simple unit tests with appropriate fixtures defined for providing a suitable testing environment.
6. CI Pipeline defined as a github action workflow in `.github/workflows/ci.yaml`. The pipeline does the following:
    - Check code format using `black`
    - Lint the code using `flake8`
    - Run rests and create code coverage report using `pytest`, and `pytest-cov`
7. Configurations and password for the database connnection and is read dynamically from a dot env file.
8. For testing, an in-memory sql-lite databse is used.
9. A useful .gitignore file to help with version control.
