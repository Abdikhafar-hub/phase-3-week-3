
# Concerts API

Welcome to the Concerts API project! This application manages information about bands, venues, and concerts. It uses Flask for the web framework and SQLAlchemy for database interactions.

## Table of Contents

 [Project Overview](#projectoverview)
 [Setup](#setup)
 [Running the Application](#runningtheapplication)
 [Using the CLI](#usingthecli)
 [API Endpoints](#apiendpoints)
 [Contributing](#contributing)
 [License](#license)
## Features

 **View**: List all bands, venues, and concerts.
 **Add**: Add new bands, venues, and concerts.
 **Interact**: Use the API to manage and query concert data.

## Installation

### Prerequisites

 Python 3.x
 pip (Python package installer)
 [Flask](https://flask.palletsprojects.com/en/2.1.x/)
 [FlaskSQLAlchemy](https://flasksqlalchemy.palletsprojects.com/)
 [FlaskMigrate](https://flaskmigrate.readthedocs.io/en/latest/)
 [FlaskScript](https://flaskscript.readthedocs.io/en/latest/)

### Set Up a Virtual Environment

On your bash
python3 m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


### Install Dependencies

On your bash

pip install r requirements.txt

### Initialize the Database

Run the following commands to set up the database and apply migrations:

On your bash

flask db init
flask db migrate m "Initial migration"
flask db upgrade


## Usage

### Running the Application

To start the Flask development server, use:

On your bash

export FLASK_APP=app.py
export FLASK_ENV=development  # Optional: sets environment to development
flask run

The application will be available at `http://127.0.0.1:5000/`.

### Using the CLI

For database management and other tasks, you can use the Flask CLI commands. Here's how:

 **Initialize the migrations directory:**

  On your bash
 python manage.py db init


 **Create a new migration:**

  On your bash
  python manage.py db migrate m "Migration message"

  

 **Apply the migrations:**

  On your bash
  python manage.py db upgrade


### API Endpoints

#### GET `/`

 **Description**: Returns a welcome message.
 **Response**: `{"message": "Welcome to the Concerts API!"}`

#### GET `/bands`

 **Description**: Lists all bands.
 **Response**: JSON array of band objects.

#### POST `/bands`

 **Description**: Adds a new band.
 **Request Body**: JSON object with `name` and `hometown` fields.
 **Response**: JSON object with the details of the newly created band.

#### GET `/venues`

 **Description**: Lists all venues.
 **Response**: JSON array of venue objects.

#### POST `/venues`

 **Description**: Adds a new venue.
 **Request Body**: JSON object with `title` and `city` fields.
 **Response**: JSON object with the details of the newly created venue.

#### GET `/concerts`

 **Description**: Lists all concerts.
 **Response**: JSON array of concert objects.

#### POST `/concerts`

 **Description**: Adds a new concert.
 **Request Body**: JSON object with `date`, `band_id`, and `venue_id` fields.
 **Response**: JSON object with the details of the newly created concert.

## Contributing

We welcome contributions to improve the Concerts API! To contribute:

1. **Fork** the repository.
2. **Create** a new branch (`git checkout b featurebranch`).
3. **Make** your changes.
4. **Commit** your changes (`git commit am 'Add new feature'`).
5. **Push** to the branch (`git push origin featurebranch`).
6. **Open** a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.