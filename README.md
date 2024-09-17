# Flask Unit Testing and CI/CD Demo

This project demonstrates unit testing and CI/CD skills using Flask, pytest, GitHub Actions, and Docker. It focuses on two main entities: Employee and Animal.

## Technologies Used

-   Python
-   Flask
-   pytest
-   pipenv
-   GitHub Actions
-   Docker and Docker Compose

## Prerequisites

-   Python 3.x
-   pipenv
-   Docker and Docker Compose (optional, for running in containers)

## Installation

1. Clone the repository
2. Install dependencies using pipenv:
    ```bash
    pipenv install
    ```

## Running the Application

To run the Flask application:

```bash
python run.py
```

The application will be available at `http://localhost:5000/apidocs/`.

## Running Tests and Coverage

To run the unit tests with coverage:

```bash
pipenv run coverage run -m pytest
pipenv run coverage report -m
pipenv run coverage html
```

These commands do the following:

1. Run all tests using pytest and collect coverage data
2. Generate a coverage report with missing lines indicated
3. Create an HTML coverage report

After running these commands, you'll see:

-   A summary of the coverage in the terminal
-   A `.coverage` file (raw coverage data)
-   An `htmlcov` directory containing a detailed HTML coverage report

To view the HTML coverage report, open `htmlcov/index.html` in your web browser.

## Continuous Integration/Continuous Deployment (CI/CD)

This project uses GitHub Actions for CI/CD. The workflow is defined in `.github/workflows/main.yml` and is triggered on pushes and pull requests to the `main` branch.

1. Sets up Python
2. Installs pipenv
3. Installs project dependencies
4. Runs all tests

## Docker

To build and run the application using Docker:

1. Build the Docker image:

    ```bash
    docker build -t flask-unit-testing .
    ```

2. Run the container:
    ```bash
    docker run -p 5000:5000 flask-unit-testing
    ```

Alternatively, you can use Docker Compose:

```bash
docker-compose up -d
```
