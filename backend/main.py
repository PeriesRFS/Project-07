# main.py
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field
from typing import List
from threading import Lock


app = FastAPI(title="Student Management API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for dev
    #allow_origins=["http://127.0.0.1:5501"],  # frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Thread-safe in-memory storage
# -------------------------
students = []
next_id = 1
lock = Lock()

# -------------------------
# Models
# -------------------------
class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1, example="John Doe")
    email: EmailStr = Field(..., example="john@example.com")
    course: str = Field(..., min_length=1, example="Machine Learning")

class StudentOut(StudentCreate):
    id: int

# -------------------------
# Routes
# -------------------------

@app.get("/")
def root():
    return {"message": "Student Management API is running"}


@app.post("/students/", response_model=StudentOut, status_code=status.HTTP_201_CREATED)
def add_student(student: StudentCreate):
    global next_id

    # Prevent duplicate emails
    for s in students:
        if s["email"] == student.email:
            raise HTTPException(
                status_code=400,
                detail="A student with this email already exists."
            )

    with lock:
        student_dict = student.model_dump()
        student_dict["id"] = next_id
        students.append(student_dict)
        next_id += 1

    return student_dict


@app.get("/students/", response_model=List[StudentOut])
def list_students():
    return students


@app.delete("/students/{student_id}", response_model=StudentOut)
def delete_student(student_id: int):
    for i, s in enumerate(students):
        if s["id"] == student_id:
            deleted = students.pop(i)
            return deleted

    raise HTTPException(
        status_code=404,
        detail="Student not found."
    )