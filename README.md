# Cool Gamer Tagz

This project is a FastAPI-based application for generating cool gamertags. 

## Project Structure


- **main.py:** The main FastAPI application file. It includes endpoints for creating a gamertag.

- **models.py:** Contains the SQLAlchemy models for defining the database schema, including Users, Gamer Tags.

- **database.py:** Handles the database configuration, including creating the tables defined in models.py and providing a database session for the application.


## ENDPOINTS

1. POST /create-gamer-tag/ - create a gamer tag

2. POST /create-user/ - create a user


