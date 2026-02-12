
const API_URL = "http://127.0.0.1:8000/students/";

const form = document.getElementById("studentForm");
const tableBody = document.getElementById("studentTable");

// Load students on page load
window.onload = fetchStudents;

// Fetch and display students
function fetchStudents() {
    fetch(API_URL)
        .then(res => res.json())
        .then(data => {
            tableBody.innerHTML = "";
            data.forEach(student => {
                const row = `
                    <tr>
                        <td>${student.id}</td>
                        <td>${student.name}</td>
                        <td>${student.email}</td>
                        <td>${student.course}</td>
                        <td>
                            <button onclick="deleteStudent(${student.id})">Delete</button>
                        </td>
                    </tr>
                `;
                tableBody.innerHTML += row;
            });
        });
}

// Add student
form.addEventListener("submit", function (e) {
    e.preventDefault();

    const student = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        course: document.getElementById("course").value
    };

    fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(student)
    })
    .then(res => {
        if (!res.ok) throw new Error("Failed to add student");
        return res.json();
    })
    .then(() => {
        form.reset();
        fetchStudents();
    })
    .catch(err => alert(err.message));
});

// Delete student
function deleteStudent(id) {
    fetch(API_URL + id, { method: "DELETE" })
        .then(res => {
            if (!res.ok) throw new Error("Delete failed");
            fetchStudents();
        });
}
