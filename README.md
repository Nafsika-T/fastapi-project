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

## ⚙️ Local Setup

### 1. Clone the repository

git clone https://github.com/USERNAME/REPO_NAME.git
cd REPO_NAME
2. Create a virtual environment

python -m venv venv
Windows

venv\Scripts\activate
macOS / Linux

source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Environment variables

cp .env.example .env
Update the values inside .env if needed.

5. Run the API

uvicorn app.main:app --reload
The API will be available at: http://127.0.0.1:8000

📚 API Documentation

Swagger UI:
http://127.0.0.1:8000/docs
🧪 Run Tests

pytest

🔐 Authentication
The API uses JWT authentication.

Include the access token in the request header:

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

---

### ✅ Τι κάνεις τώρα

git add README.md
git commit -m "Add README"
git push
