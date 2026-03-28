from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Hi Myself Krushna": "Working"}
 
DB_URL = "sqlite:///sample.db"