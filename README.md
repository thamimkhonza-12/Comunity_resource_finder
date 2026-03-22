# 🌍 Smart Community Resource Finder API

A Django REST API that helps users discover nearby community resources such as clinics, shelters, food banks, and educational services.

Built with **Django, Django REST Framework, and JWT Authentication**.

---

## 🚀 Live API (Local Development)

Base URL:  
 http://127.0.0.1:8000/

 Register User

 http://127.0.0.1:8000/api/users/register/

 
  Get JWT Token

 http://127.0.0.1:8000/api/token/

 
  Refresh Token

 http://127.0.0.1:8000/api/token/refresh/

 
  Locations

 http://127.0.0.1:8000/api/locations/

 
  Resources

 http://127.0.0.1:8000/api/resources/

 
  Reviews

 http://127.0.0.1:8000/api/reviews/


 Find resources within a given radius:

 http://127.0.0.1:8000/api/resources/nearby/?lat=-29.8587&lng=31.0218&radius=10



---

## 🚀 Features

- 🔐 JWT Authentication
- 👤 User registration
- 📍 Geolocation filtering (nearby resources)
- 🏥 Resource management (CRUD)
- ⭐ Reviews and ratings system
- 📊 Automatic average rating calculation
- 🔒 Permissions (owner-based access control)

---

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- SimpleJWT

---

## ⚙️ Installation

```bash
cd community-resource-finder

python -m venv venv
.\venv\Scripts\activate

pip install -r requirements.txt