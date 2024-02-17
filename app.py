from fastapi import FastAPI

import utils

app = FastAPI(
    title="Backend-Study",
    version="0.0.1"
)

@app.get('/')
def greeting():
    return "Hello"


