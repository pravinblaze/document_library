# Document Library

This demo project showcases building a restful Python flask application for a document library.
The application provides endpoints for uploading, querying, and deleting document objects.

## You can find the following demonstrations in this project:

1. Dependencies listed in requirements.txt for the creation of a suitable virtual environment.
2. Defined a simple data model for tracking documents in the database.
3. Used flask migrate to initialize and create corresponding schema.
4. Simple blueprint with routes defined for document upload and retrieval.
5. Simple unit tests with appropriate fixtures defined for providing a suitable testing environment.
6. Configurations and the password for the database connection are read dynamically from a dot env file.
7. For testing, an in-memory sql-lite database is used.
8. A useful .gitignore file to help with version control.
9. CI Pipeline is  defined as a GitHub action workflow in `.github/workflows/ci.yaml`. The pipeline does the following:
    - Check code format using `black`
    - Lint the code using `flake8`
    - Run rests and create a code coverage report using `pytest` and `pytest-cov`
10. You can see the results of the CI pipeline runs here: [https://github.com/pravinblaze/document_library/actions](https://github.com/pravinblaze/document_library/actions).
