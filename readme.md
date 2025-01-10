# E-Commerce API with Flask, SQLAlchemy, Marshmallow, and MySQL

## Overview
This project implements a RESTful API for managing an e-commerce system using Flask, SQLAlchemy, Marshmallow, and MySQL. The API provides endpoints to handle **Users**, **Orders**, and **Products**, including relationships such as one-to-many and many-to-many associations. This project is designed for learning purposes and provides a foundation for building scalable web applications.

---

## Features

- **CRUD operations** for Users, Products, and Orders.
- **Pagination** for user and product listings.
- **Order management** with the ability to:
  - Add multiple products to an order.
  - Remove products from an order.
  - Update the status of an order.
  - Retrieve all products associated with an order.
- **MySQL Database** integration with proper model relationships.
- **Marshmallow Schemas** for data serialization and validation.

---

## Project Structure

```
project_root/
|-- app.py                # Main application entry point
|-- models.py             # Database models
|-- schemas.py            # Marshmallow schemas
|-- utils/
|   |-- db_setup.py       # Database and Marshmallow initialization
|-- routes/
|   |-- user_routes.py    # User-related routes
|   |-- product_routes.py # Product-related routes
|   |-- order_routes.py   # Order-related routes
|-- requirements.txt      # Python dependencies
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- MySQL 8+
- Virtual Environment (optional but recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd project_root
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Mac/Linux
   venv\Scripts\activate   # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a MySQL database:
   ```sql
   CREATE DATABASE ecommerce_api;
   ```

5. Configure the database URI in `app.py`:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<username>:<password>@localhost/ecommerce_api'
   ```

6. Initialize the database:
   ```bash
   flask db_create_all
   ```

7. Run the Flask application:
   ```bash
   flask run
   ```

8. Access the API at:
   ```
   http://127.0.0.1:5000
   ```

---

## Endpoints

### User Endpoints
| Method | Endpoint            | Description                |
|--------|---------------------|----------------------------|
| GET    | `/users`            | Retrieve all users         |
| GET    | `/users/<id>`       | Retrieve a user by ID      |
| POST   | `/users`            | Create a new user          |
| PUT    | `/users/<id>`       | Update a user by ID        |
| DELETE | `/users/<id>`       | Delete a user by ID        |

### Product Endpoints
| Method | Endpoint            | Description                 |
|--------|---------------------|-----------------------------|
| GET    | `/products`         | Retrieve all products (paginated) |
| GET    | `/products/<id>`    | Retrieve a product by ID    |
| POST   | `/products`         | Create a new product        |
| PUT    | `/products/<id>`    | Update a product by ID      |
| DELETE | `/products/<id>`    | Delete a product by ID      |

### Order Endpoints
| Method | Endpoint                                | Description                                 |
|--------|----------------------------------------|---------------------------------------------|
| POST   | `/orders`                              | Create a new order                         |
| POST   | `/orders/<order_id>/add_products`      | Add multiple products to an order          |
| DELETE | `/orders/<order_id>/remove_product/<product_id>` | Remove a product from an order     |
| PUT    | `/orders/<order_id>/status`            | Update the status of an order              |
| GET    | `/orders/user/<user_id>`               | Get all orders for a user (paginated)      |
| GET    | `/orders/<order_id>/products`          | Get all products in an order               |
| GET    | `/orders/<order_id>`                   | Retrieve a single order by ID              |

---

## Example Usage

### Creating a Product
#### Request
```bash
curl -X POST http://127.0.0.1:5000/products \
-H "Content-Type: application/json" \
-d '{
    "product_name": "Laptop",
    "price": 999.99,
    "description": "High-performance laptop"
}'
```
#### Response
```json
{
    "id": 1,
    "product_name": "Laptop",
    "price": 999.99,
    "description": "High-performance laptop"
}
```

### Adding Products to an Order
#### Request
```bash
curl -X POST http://127.0.0.1:5000/orders/1/add_products \
-H "Content-Type: application/json" \
-d '{
    "product_ids": [1, 2, 3]
}'
```
#### Response
```json
{
    "message": "Products added to order successfully.",
    "added_products": [
        {"id": 1, "product_name": "Laptop"},
        {"id": 2, "product_name": "Mouse"}
    ]
}
```

---

## Testing

1. Use [Postman](https://www.postman.com/) or `curl` to test the API endpoints.
2. Verify data is correctly stored in the database using MySQL Workbench or a similar tool.
3. Run automated tests (if implemented) to validate functionality.

---

## Future Improvements

- Implement **JWT authentication** for secure access.
- Add **advanced filtering** for product and user listings.
- Enable **bulk user creation**.
- Add **unit tests** and integrate CI/CD pipelines.

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute this code as you wish.

