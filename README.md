### Gym Membership System (CLI Project)

## Overview
This is a Command-Line Interface (CLI) application to manage gym members, gym classes, and bookings. It was built using Python and SQLAlchemy ORM as part of a Phase 3 project at Moringa School.

## Features
- Register new gym members
- Create gym classes with schedule and capacity
- Book members into classes (with capacity validation)
- View all members, classes, and bookings
- Delete members and classes

## Technologies Used
- Python 3.8+
- SQLAlchemy ORM
- SQLite (gym.db)
- Pipenv

## Project Structure
```
project/
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib/
    ├── cli.py
    ├── debug.py
    ├── helpers.py
    ├── seed.py
    └── models/
        ├── __init__.py
        ├── member.py
        ├── gym_class.py
        └── booking.py
```

## Setup Instructions
1. Clone the repository
2. Run `pipenv install` to install dependencies
3. Run `pipenv shell` to activate the virtual environment
4. Run `PYTHONPATH=. python lib/debug.py` to create the tables
5. Run `PYTHONPATH=. python lib/seed.py` to populate test data
6. Run `PYTHONPATH=. python lib/cli.py` to start the app

## Author
Alex Njugi Karanja
