# 🎓 KGP Course Platform

[![Django](https://img.shields.io/badge/Django-6.0.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

> A comprehensive **Learning Management System (LMS)** designed to bridge the gap between Instructors, Students, and Administrators. This project demonstrates a robust **Hybrid Database Architecture**, integrating Django's ORM for authentication with **Raw SQL** for core business logic and complex relational data handling.

---

## 📸 Platform Previews

| **Student Dashboard** | **Course Content & Progress** |
|:---:|:---:|
| ![Student Dashboard](screenshots/image_c4aff1.png) | ![Course Content](screenshots/image_c5246e.png) |
| *Browse courses and track active enrollments.* | *View lectures, video links, and mark progress.* |

| **Instructor Management** | **Analyst Analytics** |
|:---:|:---:|
| ![Instructor Grading](screenshots/image_c59c34.png) | ![Analyst Dashboard](screenshots/image_d10fa3.png) |
| *Track student progress (%) and assign grades.* | *Visualize enrollment trends and grade histograms.* |

---

## 🚀 Key Features

### 👨‍🎓 **Student Module**
* **Smart Enrollment:** One-click registration logic that detects existing enrollments.
* **Progress Tracking:** "Mark as Done" functionality for individual course materials.
* **Dynamic Dashboard:** Real-time view of enrolled courses, grades, and feedback.
* **Resource Access:** Direct links to PDFs, video lectures, and external resources.

### 👨‍🏫 **Instructor Module**
* **Course Management:** Upload learning materials (PDFs, Links) to specific courses.
* **Student Monitoring:** View detailed progress bars (e.g., "50% Completed") for every student.
* **Grading System:** Assign marks and provide personalized feedback.
* **Dashboard:** Overview of all assigned teaching responsibilities.

### 📊 **Analyst Module (Data Visualization)**
* **Interactive Dashboards:** Powered by **Chart.js**.
* **Enrollment Trends:** Compare popularity across different courses.
* **Performance Histograms:** Analyze grade distributions (e.g., how many students scored 80-90).
* **KPI Cards:** Instant view of total platform enrollments and average performance metrics.

### 🛡️ **Role-Based Access Control (RBAC)**
* **Secure Authentication:** Django's robust auth system.
* **Profile Management:** Auto-generates `Student` or `Instructor` IDs upon signup using Signals.
* **Permission Gates:** Decorators ensure users only access views relevant to their role.

---

## 🛠️ Technical Architecture

**This project uses a unique Hybrid Database Model:**

1.  **Managed by Django (ORM):**
    * User Authentication (`User`, `Profile`).
    * Session Management.
    * Admin Interface Logs.

2.  **Managed by Raw SQL (Legacy Integration):**
    * Core Entities: `Student`, `Course`, `Instructor`, `University`.
    * **Why?** To demonstrate advanced DBMS skills, these tables are defined via SQL scripts and accessed in Django using `managed = False`.
    * **Complex Queries:** Usage of `connection.cursor()` for optimized data fetching and insertions.

---

## 📂 Project Structure

```bash
ONLINE-COURSE-PLATFORM
├── core
│   ├── migrations/
│   ├── static/js/          # Custom JavaScript (Profile toggle, Charts)
│   ├── admin.py            # Admin panel configuration
│   ├── models.py           # Hybrid models (managed=False & True)
│   ├── views.py            # Business logic (SQL Queries & View logic)
│   ├── forms.py            # User input handling
│   └── urls.py             # Route definitions
├── course_platform
│   ├── settings.py         # DB config, Static files, Apps
│   └── urls.py             # Main URL entry point
├── templates
│   ├── admin/              # Custom Admin templates
│   ├── dashboards/         # Role-specific dashboards (Student/Instructor/Analyst)
│   ├── instructor/         # Grading & Content Management pages
│   ├── student/            # Course listing & Detail pages
│   ├── base.html           # Main layout wrapper
│   ├── login.html          # Auth pages
│   └── signup.html
├── venv/                   # Virtual Environment
├── database_setup.sql      # Core SQL Schema Script
├── manage.py
├── requirements.txt
└── .env                    # Environment Variables

---

```
## ⚙️ Installation & Setup

### 1. Prerequisites
* **Python** 3.10+
* **PostgreSQL**

### 2. Clone the Repository
```bash
git clone [https://github.com/yourusername/online-course-platform.git](https://github.com/yourusername/online-course-platform.git)
cd online-course-platform
```
### 3. Setup Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Environment Configuration

Create a .env file in the root directory:
```bash
Ini, TOML

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your_django_secret_key
DEBUG=True
```
### 6. Database Initialization (Crucial Step)

Since this project uses Raw SQL for the core schema, you must create the tables manually before running Django migrations.

 1. Open the Django Database Shell:
    ```bash

    python manage.py dbshell
    ```
 2. Copy and paste the contents of database_setup.sql (included in repo) into the shell terminal.

 3. Exit the shell (\q).

### 7. Run Migrations & Start Server

```bash
# Creates the auth tables and junction tables managed by Django
python manage.py makemigrations
python manage.py migrate

# Create a Superuser for the Admin Panel
python manage.py createsuperuser

# Run the Server
python manage.py runserver

---
```
## 🧪 Testing the Platform

Use the following credentials to test the different roles (or create your own via Sign Up):

| Role | Username | Password | Features to Test |
| :--- | :--- | :--- | :--- |
| **Admin** | `admin` | *(your set pass)* | Assign Instructors, View DB Tables |
| **Student** | `student_01` | `testpass123` | Register, Mark Content Done |
| **Instructor** | `ins_01` | `testpass123` | Upload Content, Grade Students |
| **Analyst** | `analyst_01` | `testpass123` | View Histograms & Graphs |

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

Built with ❤️ by Hritwik,Akshat at IIT Kharagpur.

---

### **Your `database_setup.sql` File Content**
Create a file named `database_setup.sql` in your main folder and paste this code. This is the "Industry Standard" way to distribute SQL schemas.

```sql
-- 1. Create Core Tables
CREATE TABLE IF NOT EXISTS university (
    university_id INTEGER PRIMARY KEY,
    university_name VARCHAR(100),
    country VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS instructor (
    instructor_id INTEGER PRIMARY KEY,
    instructor_name VARCHAR(100),
    email VARCHAR(100),
    years_experience INTEGER,
    expertise VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS topic (
    topic_id INTEGER PRIMARY KEY,
    topic_name VARCHAR(50),
    category VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS course (
    course_id INTEGER PRIMARY KEY,
    course_name VARCHAR(100),
    duration_months INTEGER,
    program_type VARCHAR(50),
    rating DECIMAL(3, 2)
);

CREATE TABLE IF NOT EXISTS student (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(100),
    age INTEGER,
    country VARCHAR(50),
    category VARCHAR(50),
    email VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS textbook (
    isbn_number VARCHAR(20) PRIMARY KEY,
    author VARCHAR(100),
    title VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS online_content (
    content_id INTEGER PRIMARY KEY,
    content_type VARCHAR(50),
    title VARCHAR(150),
    url VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS evaluation (
    evaluation_id INTEGER PRIMARY KEY,
    student_id INTEGER REFERENCES student(student_id),
    course_id INTEGER REFERENCES course(course_id),
    marks DECIMAL(5, 2),
    feedback VARCHAR(500)
);

-- 2. Create Junction Tables (With ID for Django Compatibility)
CREATE TABLE IF NOT EXISTS course_content (
    id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES course(course_id),
    content_id INTEGER REFERENCES online_content(content_id)
);

CREATE TABLE IF NOT EXISTS course_instructor (
    id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES course(course_id),
    instructor_id INTEGER REFERENCES instructor(instructor_id)
);

CREATE TABLE IF NOT EXISTS enrollment (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES student(student_id),
    course_id INTEGER REFERENCES course(course_id),
    enrollment_date DATE,
    status VARCHAR(20)
);
