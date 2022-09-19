from fastapi import FastAPI
from routes import joke, mathematics
from fastapi.openapi.utils import get_openapi


#Tags for grouping mathematics and joke methods.
tags_metadata = [
    {"name": "Jokes Methods", "description": "Here you can find all the methods to interact with Jokes"},
    {"name": "Mathematics Methods", "description": "Here you can find all the methods to interact with Mathematics"}
]


app = FastAPI(openapi_tags=tags_metadata)

app.include_router(joke.router)
app.include_router(mathematics.router)

#documentation
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="SquadMakers",
        version="3.0.2",
        description="This is the API for solving the challenge",
        routes=app.routes,
    )
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi