# Python Django Box Selection System

## Project Overview

This project is a Django REST API that recommends the most suitable shipping box for an order based on the dimensions and weight of the selected products. The recommendation is made by evaluating the available boxes and selecting the lowest-cost box that satisfies the required volume and weight constraints.

The project was developed using Django and Django REST Framework as part of the Python Django assignment.

---

## Features

- Product management through Django Admin
- Shipping box management
- Order and order item models
- REST API for box recommendation
- Input validation
- Error handling for invalid requests
- Automated unit tests

---

## Technology Stack

- Python 3
- Django
- Django REST Framework
- SQLite

---

## Project Structure

```
Python_Django_Assignment/

├── config/
├── shipping/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── services.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
├── AI_USAGE.md
├── TEST_OUTPUT.md
└── .gitignore
```

---

## Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd python-django-box-selection
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Run Development Server

```bash
python manage.py runserver
```

---

## Admin Panel

```
http://127.0.0.1:8000/admin/
```

---

## API Endpoint

### POST

```
/api/recommend-box/
```

### Sample Request

```json
{
    "items": [
        {
            "product_id": 1,
            "quantity": 1
        }
    ]
}
```

### Sample Response

```json
{
    "recommended_box": "Small Box",
    "cost": "40.00",
    "dimensions": {
        "length": 35,
        "width": 25,
        "height": 10
    },
    "max_weight": 3
}
```

---

## Recommendation Logic

The recommendation algorithm performs the following steps:

1. Calculates the total weight of the order.
2. Calculates the total volume of all products.
3. Finds boxes that satisfy both weight and volume requirements.
4. Selects the lowest-cost suitable box.
5. If multiple boxes have the same cost, the smaller box is selected.

---

## Assumptions

- Product packing is approximated using total volume.
- Products are assumed to fit within the selected box if the total volume and maximum weight constraints are satisfied.
- Product orientation and advanced 3D packing are outside the scope of this implementation.
- Product quantities must be greater than zero.

---

## Running Tests

```bash
python manage.py test
```

---

## Author

Shashvat Upadhyay