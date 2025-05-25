from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks from file
with open("marks.json") as f:
    student_marks = json.load(f)

@app.get("/api")
def get_marks(name: list[str] = []):
    results = [student_marks.get(n, None) for n in name]
    return {"marks": results}
