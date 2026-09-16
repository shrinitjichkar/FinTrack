# FinTrack

**Personal Finance Management Platform** built with Django for managing income and expense records through a server-side rendered web application.

FinTrack follows Django's **MVT (Model–View–Template) architecture** and uses **MySQL** for persistent data storage. The application handles user authentication, authorization, financial record CRUD operations, input validation, and income/expense calculations on the backend.

---

## Tech Stack

* **Language:** Python
* **Framework:** Django
* **Database:** MySQL
* **Frontend:** HTML, Django Templates
* **ORM:** Django ORM
* **Forms:** Django ModelForms
* **Authentication:** Django built-in authentication framework

---

## Application Architecture

FinTrack follows Django's MVT architecture.

```text
                         Browser
                            │
                            │ HTTP Request
                            ▼
                       URL Routing
                            │
                            ▼
                         View
                            │
                 ┌──────────┴──────────┐
                 │                     │
                 ▼                     ▼
               Model                Template
                 │                     │
                 ▼                     │
            Django ORM                │
                 │                     │
                 ▼                     │
               MySQL                   │
                 │                     │
                 └──────────┬──────────┘
                            │
                            ▼
                    Rendered HTML
                            │
                            ▼
                         Browser
```

### Request Lifecycle

A typical request follows:

```text
HTTP Request
     ↓
URL
     ↓
View
     ↓
Database / Business Logic
     ↓
Context Data
     ↓
Django Template
     ↓
Rendered HTML Response
```

This server-side approach keeps request handling, database interaction, and presentation within the Django application.

---

## Core Functionality

### 1. Income & Expense Management

FinTrack allows users to manage their financial records through standard CRUD operations.

```text
Create
  ↓
Read
  ↓
Update
  ↓
Delete
```

Financial records are stored in the MySQL database and retrieved through Django ORM queries.

---

### 2. Database Models & Relationships

The application's financial data is represented using Django models.

A simplified relationship is:

```text
┌──────────────┐
│     User     │
└──────┬───────┘
       │
       │ 1 : N
       ▼
┌──────────────────┐
│ Financial Record │
├──────────────────┤
│ amount           │
│ type             │
│ date             │
│ category         │
│ description      │
│ user             │
└──────────────────┘
```

A user can have multiple financial records, while each record is associated with its corresponding user.

Django migrations are used to keep the database schema synchronized with the application models.

---

## 3. Django ORM

FinTrack uses Django ORM for database interaction.

The application works with Django models and QuerySets rather than directly handling database operations throughout the views.

```text
Django View
     ↓
Django Model / QuerySet
     ↓
Django ORM
     ↓
MySQL
```

This provides a structured way to create, retrieve, update, and delete financial records.

---

## 4. Authentication & Authorization

User registration and authentication are implemented using Django's built-in authentication framework.

The application protects relevant routes so that authenticated users can access the financial management functionality.

```text
User
 ↓
Registration
 ↓
Login
 ↓
Authenticated Session
 ↓
Protected Route
 ↓
Application
```

Financial records are associated with users, allowing the application to work with the records belonging to the authenticated user.

---

## 5. ModelForms & Input Validation

Django **ModelForms** are used to handle financial record input.

The form layer provides a structured way to accept and validate user input before interacting with the database.

```text
User Input
    ↓
ModelForm
    ↓
Validation
    ↓
View / Business Logic
    ↓
Model
    ↓
MySQL
```

This keeps form handling and validation organized instead of placing all input-processing logic directly inside the view.

---

## 6. Financial Calculations

Backend business logic is used to process income and expense records and perform the required financial calculations.

Conceptually:

```text
Income Records
      │
      ▼
 Total Income
      │
      ├──────────────┐
      │              │
      ▼              ▼
Expense Records   Calculations
      │              │
      ▼              ▼
 Total Expenses → Financial Summary
```

The calculations are performed from the application's stored financial records.

---

# Database Flow

The complete data flow for a financial record is:

```text
                 User
                  │
                  ▼
             Django Form
                  │
                  ▼
              Validation
                  │
                  ▼
                View
                  │
                  ▼
             Django Model
                  │
                  ▼
              Django ORM
                  │
                  ▼
                MySQL
                  │
                  ▼
             Django ORM
                  │
                  ▼
                View
                  │
                  ▼
          Django Template
                  │
                  ▼
             HTML Response
```

---

# Key Django Concepts Demonstrated

* **MVT Architecture**
* Server-Side Rendering
* URL Routing
* Django Views
* Django Models
* Django Templates
* Django ORM
* MySQL Database Integration
* Database Migrations
* Foreign-Key Relationships
* CRUD Operations
* User Registration
* Authentication
* Authorization
* Protected Routes
* ModelForms
* Input Validation
* Backend Business Logic
* Income & Expense Calculations

---

# Project Structure

A typical Django structure for the application is:

```text
FinTrack/
│
├── manage.py
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── ...
│
├── templates/
│   └── ...
│
└── requirements.txt
```

The application separates Django configuration, application logic, forms, models, URL routing, and templates according to Django's project structure.

---

# What This Project Demonstrates

FinTrack demonstrates the complete flow of a **server-rendered Django application**, from receiving an HTTP request to processing business logic, interacting with a relational database, and returning dynamically rendered HTML.

The main development focus was understanding how:

```text
Django
  +
MVT
  +
ORM
  +
MySQL
  +
Authentication
  +
ModelForms
  +
Business Logic
```

work together to build a functional web application.

---

## Project Status

**Completed**

* Server-side Django application
* MVT architecture
* Income and expense CRUD
* MySQL database integration
* Django ORM
* Database models and relationships
* Database migrations
* User registration
* Authentication
* Authorization
* Protected routes
* ModelForms
* Input validation
* Income/expense calculations
