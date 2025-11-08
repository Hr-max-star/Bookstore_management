# Bookstore Management API (Django REST Framework)

## 1. Project Overview
This project is a REST API–based Bookstore Management System built using **Django REST Framework**.  
It allows managing **Authors, Genres, Books, and Customers**, along with handling **book purchasing** and enforcing validation rules.

The project demonstrates working with **M2M relationships**, **Foreign Keys**, **Serializer validation**, and **custom API endpoints**.

---

## 2. Technologies Used
- Python
- Django & Django REST Framework
- SQLite Database (default)
- Thunder Client / Postman for API testing

---

## 3. Database Models & Relationships

| Model     | Fields | Relationships |
|----------|--------|----------------|
| **Author** | name, bio | One Author → Many Books |
| **Genre** | name (unique) | Many Genres ↔ Many Books (M2M) |
| **Book** | title, price, author (FK to Author), genres (M2M to Genre) | A book can have multiple genres |
| **Customer** | name, email (unique), purchased_books (M2M to Book) | A customer can purchase multiple books |

### Relationship Summary
- **Author → Book** → One-to-Many
- **Book ↔ Genre** → Many-to-Many
- **Customer ↔ Book** → Many-to-Many

---

## 4. Validations

### Model & Serializer-Level Validation
- Book `price` must be **greater than 0**.
- Customer `email` must **end with @gmail.com**.

### View-Level Validation
- A **customer cannot purchase the same book more than once**.

---

## 5. API Endpoints

| Endpoint | Method(s) | Description |
|---------|-----------|-------------|
| `/authors/` | GET, POST | List all authors / Add new author |
| `/authors/{id}/` | GET, PUT, DELETE | Retrieve / Update / Delete author |
| `/genres/` | GET, POST | List all genres / Add new genre |
| `/genres/{id}/` | GET, PUT, DELETE | Retrieve / Update / Delete genre |
| `/books/` | GET, POST | List all books / Add new book |
| `/books/{id}/` | GET, PUT, DELETE | Retrieve / Update / Delete book |
| `/customers/` | GET, POST | List all customers / Add new customer |
| `/customers/{id}/purchase/` | POST | Customer purchases one or more books |

---

## 6. Installation & Setup

```bash
# Clone the repository
git clone https://github.com/Hr-max-star/Bookstore_management.git

# Navigate into the project folder
cd Bookstore_management

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the server
python manage.py runserver
# Bookstore_management
