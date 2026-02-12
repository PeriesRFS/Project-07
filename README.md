# Student-Course Management System

A **Student-Course Management System** designed to manage student registrations and their course details. 
This project demonstrates both **Python backend API development** and **Frontend UI development**, integrating a responsive interface with a **RESTful API**.  

---

## 🔹 Project Overview

This application allows users To  
- Register new students with **Name, Email, and Course**.  
- View a **list of all registered students** dynamically.  
- **Delete students** from the list.  
- Analyze student marks and generate **statistics** using a Python script (core Python logic).  

The project is split into **frontend** and **backend** Folders.  
- Frontend: Responsive UI built with **HTML, CSS, JavaScript**.  
- Backend: **FastAPI** handles API requests with in-memory storage (no database).  
- Core Python Script - Processes student marks for Calculate display pass/fail count, average, highest, and lowest marks.  

You can see the **live application** here: [Deployed Site](https://studentcoursemgt.netlify.app/)

---

## 🔹 Features

### Backend (FastAPI)
- Add a student via API  
- List all students  
- Delete a student by ID  
- Prevent duplicate email registrations  
- Thread-safe in-memory storage  

### Frontend
- Responsive **registration form**  
- Dynamic **student list table**  
- Delete functionality integrated with backend API  
- Clean and modern UI with CSS styling  

### Core Python Task
- Enter student marks via console input  
- Calculate average, highest, lowest marks  
- Display pass/fail count and pass percentage  
- Handles invalid input  

---

## 🔹 Technologies Used

| Layer       | Technology                |
|------------|---------------------------|
| Frontend & Logic   | HTML, CSS, JavaScript     |
| Backend    | Python, FastAPI           |
| Python Logic | Core Python (Marks Analysis) |
| Deployment | Netlify (Frontend)        |
---

## 🔹 Folder Structure
<img width="598" height="447" alt="image" src="https://github.com/user-attachments/assets/3cd5a1df-c732-4035-8505-356b8c99e281" />
---

## 🔹 Setup Instructions (Run Locally)

### Prerequisites
- Python 3.12+ installed  
- Node.js and npm optional (frontend hosted separately)  
- Recommended IDE: VS Code
- Recommended VS Code Extensions: Prettier, Live Server

---
### 1. Clone the Repository
```bash
git clone <YOUR_GITHUB_REPO_LINK>
cd STUDENT-MANAGEMENT-SYSTEM-TASK-UKI
```
### 2. Backend Setup (TASK-2)
1.Navigate to the backend folder
```bash
cd backend
```

2.Install dependencies

```bash 
pip install fastapi uvicorn pydantic typing
```

3.Run the FastAPI server
```bash
uvicorn main:app --reload
```
4.The backend API will run at 
#### http://127.0.0.1:8000/

### 3. Frontend Setup

- Open index.html in your browser or serve using a local server:
- Optional: Use VS Code Live Server Extension(recommended)

- Ensure script.js points to the correct backend URL (API_URL variable).
Example:
```bash
const API_URL = "http://127.0.0.1:8000/students/";
```
### 4. Python Marks Analysis Script (TASK-1)

1.Navigate to the backend folder:
```bash
cd backend
```

2.Run the marks analysis script:
```bash
python task1_manage_students.py
```
***Follow console instructions to input marks and view results.***

### 5.Deployment

-Frontend hosted on Netlify: 
### https://studentcoursemgt.netlify.app/

Author
#### Peries RFS

