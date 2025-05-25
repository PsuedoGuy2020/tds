from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load the marks from the JSON file
with open("marks.json", "r") as f:
    student_marks = json.load(f)

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    """
    Example: /api?name=Alice&name=Bob
    """
    results = [student_marks.get(n, None) for n in name]
    return {"marks": results}
