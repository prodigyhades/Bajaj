# REST API for Web Development Project

This project is a Flask-based REST API designed to handle both POST and GET requests as per the provided specifications.

## Features

- **POST Method**: Accepts JSON input, processes it, and returns a response containing:
  - Status of the operation
  - User ID
  - College Email ID
  - College Roll Number
  - Separated numbers and alphabets
  - Highest lowercase alphabet (if any)

- **GET Method**: Returns a hardcoded operation code.

## Deployment

To deploy this application on Heroku:

1. Clone the repository.
2. Navigate to the project directory.
3. Run `heroku create` to create a new Heroku app.
4. Run `git push heroku main` to deploy the app.
5. The API will be accessible at the URL provided by Heroku.

## Local Development

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. The API will be accessible at `http://localhost:5000/bfhl`