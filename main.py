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
    student_marks_list = json.load(f)
    # Convert list to dictionary for faster lookups
    student_marks = {student["name"]: student["marks"] for student in student_marks_list}

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    """
    Example: /api?name=y5RgWANFU&name=v
    """
    results = [student_marks.get(n, None) for n in name]
    return {"marks": results}
