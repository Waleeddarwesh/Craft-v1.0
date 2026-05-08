````md
# 🧶 Craft Application

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-5.0-green)
![DRF](https://img.shields.io/badge/DRF-Rest_Framework-red)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📌 Overview

**Craft** is a comprehensive multi-vendor marketplace and e-learning platform designed to connect handcraft suppliers with customers through a scalable and feature-rich ecosystem.

The platform integrates multiple advanced systems into a single architecture, including:

- 🛒 E-commerce Operations
- 🎓 E-Learning Features
- 💬 Real-Time Communication
- 🤝 Social Networking
- 📦 Delivery Management
- 🤖 Smart Recommendations

The project follows scalable backend architecture principles using Django and modern DevOps-friendly technologies.

---

# 📋 Table of Contents

- [Key Features](#-key-features)
- [Technical Architecture](#-technical-architecture)
- [User Interfaces](#-user-interfaces)
- [Prerequisites](#-prerequisites)
- [Installation Using Docker](#-installation-using-docker)
- [Manual Installation](#-manual-installation)
- [Environment Configuration](#-environment-configuration)
- [API Documentation](#-api-documentation)
- [Contributing](#-contributing)
- [Contact](#-contact)

---

# 🚀 Key Features

## 🛒 E-Commerce System

- Multi-vendor marketplace architecture
- Product and inventory management
- Cart and order lifecycle management
- Integrated Stripe payment gateway
- Wallet and refund system
- Coupons and discount handling

---

## 🎓 E-Learning Platform

- Video course uploading for suppliers
- Course enrollment and progress tracking
- Course completion certificates

---

## 💬 Real-Time & Social Features

- Real-time chat using Django Channels and WebSockets
- Redis-powered messaging infrastructure
- Follow suppliers and interact socially
- Activity feeds and engagement system
- Real-time notifications

---

## 🤖 Smart Services

- Recommendation engine for products and courses
- Background task processing using Celery
- Email sending and asynchronous report generation

---

# 🛠 Technical Architecture

| Technology | Usage |
|---|---|
| Django | Backend Framework |
| Django REST Framework | REST APIs |
| PostgreSQL | Primary Database |
| Redis | Cache & Message Broker |
| Celery | Background Tasks |
| Django Channels | Real-Time Communication |
| Docker & Docker Compose | Containerization |
| JWT (SimpleJWT) | Authentication |
| Swagger (drf-yasg) | API Documentation |

---

# 👥 User Interfaces

The backend serves three separate frontend applications:

### 1️⃣ Customer Application
- Browse products
- Purchase courses
- Social interactions
- Track orders

### 2️⃣ Supplier Dashboard
- Product management
- Course management
- Sales analytics
- Order handling

### 3️⃣ Delivery Application
- Shipment tracking
- Delivery status updates
- Driver workflow management

---

# ⚙️ Prerequisites

Before running the project, ensure you have:

- Python 3.10+
- PostgreSQL
- Redis Server
- Docker & Docker Compose (Recommended)
- Git

---

# 🐳 Installation Using Docker

The recommended way to run the project.

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Waleeddarwesh/Craft-V1.0.git
cd Craft-V1.0
````

---

## 2️⃣ Create Environment File

Create a `.env` file in the root directory.

Example configuration is available below in the Environment Configuration section.

---

## 3️⃣ Build and Run Containers

```bash
docker-compose up --build
```

This will automatically start:

* Django Server
* PostgreSQL Database
* Redis Server
* Celery Workers

---

# 🔧 Manual Installation

## 1️⃣ Create Virtual Environment

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Configure Environment Variables

Create `.env` file in the root directory.

---

## 4️⃣ Apply Database Migrations

```bash
python manage.py migrate
```

---

## 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

## 6️⃣ Run Development Server

```bash
python manage.py runserver
```

---

## 7️⃣ Run Redis & Celery (Optional)

For chat and asynchronous tasks:

```bash
celery -A craft worker -l info
```

Ensure Redis server is running locally.

---

# 🔐 Environment Configuration

Create a `.env` file in the project root.

```ini
# Django Settings
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1

# PostgreSQL
DATABASE_URL=postgres://user:password@localhost:5432/craft_db

# Redis
REDIS_URL=redis://localhost:6379/0

# Stripe
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...

# Google OAuth
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret

# Email Service
EMAIL_HOST=sandbox.smtp.mailtrap.io
EMAIL_HOST_USER=your_user
EMAIL_HOST_PASSWORD=your_password
```

---

# 📖 API Documentation

After running the server:

### Swagger UI

http://localhost:8000/docs/

### Redoc Documentation

http://localhost:8000/redoc/

---

# 🤝 Contributing

1️⃣ Fork the repository

2️⃣ Create feature branch

```bash
git checkout -b feature/AmazingFeature
```

3️⃣ Commit changes

```bash
git commit -m "Add Amazing Feature"
```

4️⃣ Push to GitHub

```bash
git push origin feature/AmazingFeature
```

5️⃣ Open Pull Request

---

# 📞 Contact

## Waleed Darwesh

Backend Software Engineer | Django Developer | Junior DevOps Engineer

📧 Email:
[Waleeddarwesh2002@gmail.com](mailto:Waleeddarwesh2002@gmail.com)

🔗 LinkedIn:
https://www.linkedin.com/in/waleeddarwesh1/

🔗 GitHub:
https://github.com/Waleeddarwesh

---

```
```
