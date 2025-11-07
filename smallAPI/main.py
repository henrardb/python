from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    return "{'Bonjour': 'tout le monde', 'Fast': 'API2'}"
