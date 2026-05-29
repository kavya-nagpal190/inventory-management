# Inventory Management System

A production-ready Inventory Management Backend built using Django REST Framework (DRF) and PostgreSQL. The system enables inventory tracking, sales management, stock validation, revenue analytics, authentication, and API documentation through Swagger.

## Live Demo

🔗 https://inventory-management-vvsy.onrender.com

## Tech Stack

- Python
- Django
- Django REST Framework (DRF)
- PostgreSQL
- JWT Authentication (SimpleJWT)
- Swagger (drf-yasg)
- Django ORM
- Django Filter
- Render
- Git & GitHub

---

## Features

### Authentication & Security
- JWT-based Authentication
- Access Token & Refresh Token support
- Protected API endpoints
- User authentication using DRF permissions

### Product Management
- Create Products
- Update Products
- Delete Products
- View Product Details
- Inventory Quantity Tracking

### Sales Management
- Record Product Sales
- Automatic Stock Deduction
- Prevent Overselling using Atomic Transactions
- Sales History Tracking

### Analytics
- Revenue per Product
- Total Revenue Calculation
- Top Selling Products
- Sales Summary Reports
- Date Range Revenue Filtering

### Search & Filtering
- Search Products by Name
- Filter Products by Price
- Filter Products by Quantity
- Dynamic Query Support using DjangoFilterBackend

### API Documentation
- Interactive Swagger UI
- Request/Response Schemas
- API Testing Interface

---

## Database Models

### Product

| Field | Type |
|---------|---------|
| id | Integer |
| name | CharField |
| price | DecimalField |
| quantity | IntegerField |
| created_at | DateTimeField |

### Sales

| Field | Type |
|---------|---------|
| id | Integer |
| product | ForeignKey(Product) |
| quantity_sold | IntegerField |
| sale_date | DateTimeField |

---

## Custom API Endpoints

### Product APIs

| Method | Endpoint |
|----------|------------|
| GET | /api/products/ |
| POST | /api/products/ |
| GET | /api/products/{id}/ |
| PUT | /api/products/{id}/ |
| DELETE | /api/products/{id}/ |

### Sales APIs

| Method | Endpoint |
|----------|------------|
| GET | /api/sales/ |
| POST | /api/sales/ |

### Analytics Endpoints

| Endpoint | Description |
|------------|----------------|
| low_stock/ | View low stock products |
| revenue/ | Revenue per product |
| sales-history/ | Product sales history |
| top-products/ | Top selling products |
| restock/ | Increase product quantity |
| sales-summary/ | Overall sales analytics |
| revenue-range/ | Revenue between dates |

---

## Business Logic

### Stock Validation

The application prevents overselling by validating available inventory before every sale transaction.

Implemented using:

```python
transaction.atomic()
```

This ensures database consistency and prevents race conditions.

---

## Testing

The project includes unit tests for:

- Product APIs
- Sales APIs
- Authentication
- Protected Endpoints
- Serializer Validation

Testing Framework:

- Django APITestCase
- Django TestCase

Run tests:

```bash
python manage.py test
```

---

## API Documentation

Swagger Documentation:

```text
/swagger/
```

After running the project, open:

```text
http://127.0.0.1:8000/swagger/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/kavya-nagpal190/inventory-management.git
cd inventory-management
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

---

## Deployment

The application is deployed on Render.

Features configured for deployment:

- Environment Variables
- PostgreSQL Database
- Static File Handling
- Production Settings
- Gunicorn

---

## Project Structure

```text
inventory-management/
│
├── products/
├── sales/
├── users/
├── serializers/
├── views/
├── urls/
├── tests/
├── requirements.txt
├── manage.py
└── README.md
```

---

## Key Backend Concepts Demonstrated

- REST API Design
- Django REST Framework
- PostgreSQL Integration
- JWT Authentication
- Serializer Validation
- Database Transactions
- Django ORM Aggregations
- Search & Filtering
- Unit Testing
- API Documentation
- Cloud Deployment

---

## Author

**Kavya Nagpal**

- LinkedIn: https://linkedin.com/in/kavya-nagpal-890613277
- GitHub: https://github.com/kavya-nagpal190
- LeetCode: https://leetcode.com/u/kavya_nagpal00
