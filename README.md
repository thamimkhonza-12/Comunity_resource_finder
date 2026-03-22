# 🌍 Community Resource Finder API

A Django REST API that helps users find community resources (such as clinics, shelters, and services) based on location.

---

## 🚀 Live API

🔗 Base URL:  
https://community-resource-api.onrender.com

---

## 📌 API Endpoints

### 🔹 Get All Resources
👉 https://community-resource-api.onrender.com/api/resources/

---

### 🔹 Get Nearby Resources (Location-based)
👉 https://community-resource-api.onrender.com/api/resources/nearby/?lat=-29.8587&lng=31.0218&radius=10

---

### 🔹 Get Resource by ID
👉 https://community-resource-api.onrender.com/api/resources/1/

---

### 🔹 User Registration
👉 https://community-resource-api.onrender.com/api/accounts/register/

---

### 🔹 Login (Get JWT Token)
👉 https://community-resource-api.onrender.com/api/accounts/login/

---

### 🔹 Reviews
👉 https://community-resource-api.onrender.com/api/reviews/

---

## 🛠 Tech Stack

- Django
- Django REST Framework
- SQLite (development)
- Render (deployment)
- SimpleJWT (authentication)

---

## ⚡ Features

- 🔐 User authentication (JWT)
- 📍 Location-based resource search
- ⭐ Reviews system
- 🌍 RESTful API design

---

## 🧪 How to Test

Use a browser or tools like Postman:

1. Open:
   👉 https://community-resource-api.onrender.com/api/resources/

2. Try filters:
   - Nearby search
   - Specific resource IDs

---

## 📦 Local Setup

```bash
git clone https://github.com/thamimkhonza-12/Comunity_resource_finder.git
cd Comunity_resource_finder

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver