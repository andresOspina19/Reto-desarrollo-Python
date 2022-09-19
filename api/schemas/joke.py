def localJokeEntity(item) -> dict:
    return {
        "number": str(item["_id"]),
        "text": item["text"],
        "source": "local"
    }

def chuckNorrisJokeEntity(item) -> dict:
    return {
        "number": item["id"],
        "text": item["value"],
        "source": "https://api.chucknorris.io/"
    }

def dadJokeEntity(item) -> dict:
    return {
        "number": item["id"],
        "text": item["joke"],
        "source": "https://icanhazdadjoke.com/api"
    }