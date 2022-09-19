from fastapi import FastAPI

#Importing the routes
from api.routes import joke, mathematics

app = FastAPI()

app.include_router(joke.router)
app.include_router(mathematics.router)