# Reto-desarrollo-Python

This REST API requires python 3.10+, MongoDB server and all the dependencies can be found int the requirements.txt file

I decided to use a MongoDB database instead of a relational database, because we just have one entity, so we don't need to worry about relationships so let's take advantage of the high performance that offers a document-oriented database.

The design and development of this API was based on TDD (Test-driven development) and the structure is the following:

- config: Configuration of the database
- models: Pydantic models for request bodies
- routes: Controllers  
- schemas: Responses 
- tests: Unit tests 
- app.py: Main file

For deployment could be used gunicorn but for development will be used uvicorn and to run the API use the following command line:

uvicorn app:app

To see the documentation of the API go to http://localhost:8000/docs