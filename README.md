# FastAPI Todos API 🚀

A REST API for managing todos with authentication, built using **FastAPI**.

---

## ✨ Features

- FastAPI
- JWT Authentication
- CRUD operations for Todos
- SQLite database
- Environment variables with `.env`
- Tests with pytest

---

## 📁 Project Structure

.
├── app/
│ ├── routers/
│ │ ├── auth.py
│ │ └── todos.py
│ ├── database.py
│ ├── models.py
│ ├── config.py
│ └── main.py
├── tests/
│ ├── test_auth.py
│ ├── test_todos.py
│ └── test_smoke.py
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt

yaml
Αντιγραφή κώδικα

---

## ⚙️ Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/USERNAME/REPO_NAME.git
cd REPO_NAME
2. Create a virtual environment
bash
Αντιγραφή κώδικα
python -m venv venv
Windows

powershell
Αντιγραφή κώδικα
venv\Scripts\activate
macOS / Linux

bash
Αντιγραφή κώδικα
source venv/bin/activate
3. Install dependencies
bash
Αντιγραφή κώδικα
pip install -r requirements.txt
4. Environment variables
Copy the example file:

bash
Αντιγραφή κώδικα
cp .env.example .env
Update the values inside .env if needed.

5. Run the API
bash
Αντιγραφή κώδικα
uvicorn app.main:app --reload
The API will be available at:

cpp
Αντιγραφή κώδικα
http://127.0.0.1:8000
📚 API Documentation
Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc

🧪 Run Tests
bash
Αντιγραφή κώδικα
pytest
🔐 Authentication
The API uses JWT authentication.

Include the access token in the request header:

makefile
Αντιγραφή κώδικα
Authorization: Bearer <token>
🛠 Tech Stack
Python

FastAPI

SQLAlchemy

SQLite

Pytest

JWT

📄 License
MIT License

yaml
Αντιγραφή κώδικα

---

### ✅ Τι κάνεις τώρα
```bash
git add README.md
git commit -m "Add README"
git push
