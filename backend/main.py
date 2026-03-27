from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Working"}
 
DB_URL = "sqlite:///sample.db"