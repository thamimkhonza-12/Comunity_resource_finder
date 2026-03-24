# 🌍 Community Resource Finder API

A Django REST API that helps users find community resources based on location.

---

## 🚀 Live API

👉 https://community-resource-api.onrender.com/

👉 API Root:
https://community-resource-api.onrender.com/api/

---

## 📦 Endpoints

### 🔹 Resources

https://community-resource-api.onrender.com/api/resources/

### 🔹 Locations

https://community-resource-api.onrender.com/api/locations/

### 🔹 Reviews

https://community-resource-api.onrender.com/api/reviews/

---

## 📍 Nearby Resources

⚠️ Requires query parameters (lat, lng, radius)

Example:
https://community-resource-api.onrender.com/api/resources/nearby/?lat=-29.8587&lng=31.0218&radius=10

---

## 🔐 Authentication

### 🔹 Register (POST)

https://community-resource-api.onrender.com/api/accounts/register/

```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "password123"
}
```

---

### 🔹 Get Token (Login)

https://community-resource-api.onrender.com/api/token/

---

### 🔹 Refresh Token

https://community-resource-api.onrender.com/api/token/refresh/

---

## 🛠 Tech Stack

* Django
* Django REST Framework
* JWT Authentication
* SQLite (Production-ready upgrade: PostgreSQL)

---

## ⚠️ Notes

* Some endpoints require **POST requests** (use Postman or Thunder Client)
* Nearby endpoint requires query parameters
* API is deployed on Render

---

## 👨‍💻 Author

Thami Dlamini
