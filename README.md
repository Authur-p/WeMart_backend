# WeMart Backend 🛒

WeMart is a backend service built with **Django & Django REST Framework (DRF)** to support a marketplace application.  
It handles **vendor registration, authentication, product management, and order processing**.  

---

## 🚀 Features
- Vendor registration & authentication (JWT Token-based login/logout)
- Secure storage of sensitive data (hashed NIN & passwords)
- Product management (CRUD APIs)
- Order management (create, update, track)
- Role-based access (Vendor / Customer)
- RESTful API design with DRF serializers & viewsets

---

## 🛠️ Tech Stack
- **Backend:** Django, Django REST Framework  
- **Database:** PostgreSQL (or SQLite for local dev)  
- **Authentication:** Django Rest Framework Token / JWT  
- **Other Tools:** Git, Virtualenv  

---

## 📂 Project Structure
```
project_root/
│── menv/            # Virtual environment (ignored in Git)
│── .idea/           # IDE config (ignored in Git)
│── WeMart/          # Django project folder (manage.py lives here)
│   ├── account/     # User and vendor accounts
│   ├── product/     # Product management
│   ├── order/       # Orders & transactions
│   ├── settings.py  # Main settings
│   └── ...
│── requirements.txt # Dependencies
│── README.md        # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/wemart-backend.git
cd wemart-backend
```

### 2. Create & activate virtual environment
```bash
python -m venv menv
source menv/bin/activate   # Mac/Linux
menv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create superuser
```bash
python manage.py createsuperuser
```

### 6. Run development server
```bash
python manage.py runserver
```

Server will run at:  
👉 `http://127.0.0.1:8000/`

---

## 🔑 API Endpoints (Sample)

### Authentication
- `POST /account/register/` → Vendor registration  
- `POST /account/login/` → Login & get token  
- `POST /account/logout/` → Logout (invalidate token)  

### Vendor
- `GET /vendor/profile/` → Get vendor profile  
- `PUT /vendor/profile/` → Update vendor profile  

### Products
- `GET /products/` → List all products  
- `POST /products/` → Add new product (vendor only)  

---

---

## Register Buyer
- **Method:** `POST`  
- **URL:** `/auth/register-buyer/`  
- **Request body (JSON):**
```json
{
  "username": "buyer123",
  "email": "buyer@example.com",
  "password": "P@ssw0rd!",
  "password2": "P@ssw0rd!",
  "first_name": "Ada",
  "last_name": "Lovelace",
  "phone": "08123456789"
}
```

### Success response (ideal)
**Status:** `201 Created`  
```json
{
  "message": "Registration successful",
  "user": "buyer123",
  "email": "buyer@example.com",
  "token": {
    "refresh": "eyJ0eXAiOiJKV1QiLCJh...",
    "access": "eyJ0eXAiOiJKV1QiLCJh..."
  }
}
```

### Common error responses
**Password mismatch**  
**Status:** `400 Bad Request`
```json
{
  "error": "Passwords must match"
}
```

**Email already registered**  
**Status:** `400 Bad Request`
```json
{
  "error": "Email already registered"
}
```

---

## Register Vendor
- **Method:** `POST`  
- **URL:** `/auth/register-vendor/`  
- **Request body (JSON):**
```json
{
  "username": "vendor123",
  "email": "vendor@example.com",
  "password": "P@ssw0rd!",
  "password2": "P@ssw0rd!",
  "first_name": "Tunde",
  "last_name": "Adebayo",
  "business_name": "Lagos Fresh Foods",
  "business_address": "24 Market St, Lagos",
  "phone": "08098765432"
}
```

### Success response (ideal)
**Status:** `201 Created`  
```json
{
  "message": "Registration successful",
  "user": "vendor123",
  "email": "vendor@example.com",
  "token": {
    "refresh": "eyJ0eXAiOiJKV1QiLCJh...",
    "access": "eyJ0eXAiOiJKV1QiLCJh..."
  }
}
```

### Common error responses
**Validation errors (missing fields or invalid)**  
**Status:** `400 Bad Request`
```json
{
  "business_name": ["This field is required."],
  "phone": ["This field is required."]
}
```

---

## Register Delivery Agent
- **Method:** `POST`  
- **URL:** `/auth/register-delivery/`  
- **Request body (JSON):**
```json
{
  "username": "agent123",
  "email": "agent@example.com",
  "password": "P@ssw0rd!",
  "password2": "P@ssw0rd!",
  "first_name": "Chika",
  "last_name": "Okafor",
  "phone": "09011223344",
  "vehicle_type": "Bike",
  "nin": "12345678901",
  "gender": "Male",
  "next_of_kin": "Emeka Okafor",
  "guarantor1": "John Doe",
  "guarantor2": "Jane Doe"
}
```

### Success response (ideal)
**Status:** `201 Created`  
```json
{
  "message": "Registration successful",
  "user": "agent123",
  "email": "agent@example.com",
  "token": {
    "refresh": "eyJ0eXAiOiJKV1QiLCJh...",
    "access": "eyJ0eXAiOiJKV1QiLCJh..."
  }
}
```

### Common error responses
**NIN stored hashed — trying to register with an existing email**  
**Status:** `400 Bad Request`
```json
{
  "error": "Email already registered"
}
```

---

## Login (JWT)
- **Method:** `POST`  
- **URL:** `/auth/api/token/`  
- **Request body:**
```json
{
  "username": "vendor123",
  "password": "P@ssw0rd!"
}
```

### Success response
**Status:** `200 OK`
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJh...",
  "access": "eyJ0eXAiOiJKV1QiLCJh..."
}
```

---

## Logout (if using token blacklisting or token delete)
- **Method:** `POST`  
- **URL:** `/auth/logout/`  
- **Headers:**
```
Authorization: Bearer <access-token>
```

### Success response
**Status:** `200 OK`
```json
{
  "message": "Successfully logged out"
}
```

---


## 📌 Contribution Guide
1. Fork the repository  
2. Create your feature branch:  
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:  
   ```bash
   git commit -m "Add your message"
   ```
4. Push to the branch:  
   ```bash
   git push origin feature/your-feature
   ```
5. Open a Pull Request 🎉  

---

## 📄 License
This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute with attribution.

---

## 👨‍💻 Author
Built by **Your Name** ✨  
📧 Contact: your.email@example.com  
🔗 GitHub: [your-username](https://github.com/your-username)  
