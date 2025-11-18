# 🧶 Craft Application

![Python](https://img.shields.io/badge/Python-3.11-blue) ![Django](https://img.shields.io/badge/Django-5.0-green) ![DRF](https://img.shields.io/badge/DRF-Rest_Framework-red) ![Docker](https://img.shields.io/badge/Docker-Containerized-blue) ![License](https://img.shields.io/badge/License-MIT-lightgrey)

**Craft** is a comprehensive multi-vendor marketplace and e-learning platform designed to bridge the gap between handcraft suppliers (Crafters) and Customers. 

This extensive backend project exposes over **150 endpoints**, integrating E-commerce logic, Social networking, Video streaming for courses, and Real-time communication into a single, scalable architecture.

## 📋 Table of Contents
- [Key Features](#key-features)
- [Technical Architecture](#technical-architecture)
- [User Interfaces](#user-interfaces)
- [Prerequisites](#prerequisites)
- [Installation (Docker - Recommended)](#installation-docker---recommended)
- [Installation (Manual)](#installation-manual)
- [Environment Configuration](#environment-configuration)
- [API Documentation](#api-documentation)
- [Contact](#contact)

## 🚀 Key Features

### 🛒 E-commerce Core
- **Marketplace:** Multi-vendor support allowing Crafters to manage products and stock.
- **Order Management:** Complex order lifecycle (Cart -> Order -> Shipment -> Delivery).
- **Financials:** Integrated **Stripe** payments, custom wallet system, and refund handling.
- **Promotions:** Coupon and discount management system.

### 🎓 E-Learning Platform
- **Courses:** Crafters can upload video courses to teach their craft.
- **Progress Tracking:** Users can enroll in courses and track their learning progress.
- **Certificates:** System to issue certifications upon course completion.

### 💬 Social & Real-Time
- **Chat App:** Real-time messaging between buyers and sellers using **WebSockets (Django Channels)** and **Redis**.
- **Social Feed:** Users can follow Crafters, like products, and view activity feeds.
- **Notifications:** Real-time push notifications for order updates and chat messages.

### 🤖 Smart Features
- **Recommendations:** AI/Logic-based engine to suggest products and courses.
- **Background Tasks:** Uses **Celery** for handling heavy tasks like email sending and report generation asynchronously.

## 🛠 Technical Architecture

* **Backend Framework:** Django & Django REST Framework (DRF)
* **Database:** PostgreSQL
* **Caching & Message Broker:** Redis
* **Async Task Queue:** Celery
* **Real-Time Communication:** Django Channels (ASGI)
* **Containerization:** Docker & Docker Compose
* **Authentication:** JWT (SimpleJWT) & Social Auth (Google/Facebook)
* **API Documentation:** Swagger (drf-yasg)

## 👥 User Interfaces
The backend serves three distinct frontend applications:
1.  **Customer App:** For browsing products, buying courses, and social interaction.
2.  **Crafter Dashboard:** For inventory management, course uploading, and sales analytics.
3.  **Delivery App:** A streamlined interface for drivers to update shipment statuses.

## ⚙️ Prerequisites
* Python 3.10+
* PostgreSQL
* Redis Server
* Git

## 🐳 Installation (Docker - Recommended)
The easiest way to run the project is using Docker Compose.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Waleeddarwesh/Craft.git](https://github.com/Waleeddarwesh/Craft.git)
    cd Craft
    ```

2.  **Create the environment file:**
    Create a `.env` file in the root directory (see [Environment Configuration](#environment-configuration)).

3.  **Build and Run:**
    ```bash
    docker-compose up --build
    ```
    This will spin up the Django web server, PostgreSQL database, Redis, and Celery workers automatically.

## 🔧 Installation (Manual)

If you prefer running it without Docker:

1.  **Set Up Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment:**
    Create a `.env` file in the root folder based on the example below.

4.  **Apply Migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create Superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run Server:**
    ```bash
    python manage.py runserver
    ```
    *(Note: To use Chat and Async tasks manually, you must verify Redis is running locally).*

## 🔐 Environment Configuration

Create a `.env` file in the root directory (same level as `manage.py`). Do **not** hardcode credentials in `settings.py`.

```ini
# Core Settings
DEBUG=True
SECRET_KEY=your_secret_key_here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (PostgreSQL)
DATABASE_URL=postgres://user:password@localhost:5432/craft_db

# Redis (Required for Chat & Celery)
REDIS_URL=redis://localhost:6379/0

# Stripe Payments
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...

# Google Auth
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret

# Email (Mailtrap or Sendgrid)
EMAIL_HOST=sandbox.smtp.mailtrap.io
EMAIL_HOST_USER=your_user
EMAIL_HOST_PASSWORD=your_password
```
## 📖 API Documentation
Once the server is running, you can access the interactive API documentation to test over 150 endpoints.

* **Swagger UI:** [http://localhost:8000/docs/](http://localhost:8000/docs/)
* **Redoc:** [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

## 🤝 Contributing
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/AmazingFeature
    ```
3. Commit your changes:
    ```bash
    git commit -m 'Add some AmazingFeature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature/AmazingFeature
    ```
5. Open a Pull Request.

## 📞 Contact
**Waleed Darwesh** - Backend Software Engineer  
📧 [Waleeddarwesh2002@gmail.com](mailto:Waleeddarwesh2002@gmail.com)  
🔗 [LinkedIn Profile](#)

