# 📚 Library Management System (LMS)

A web application built with **Django** to digitize library operations, automate book circulation, and manage member records cleanly and efficiently.

---

## 📌 Overview

Managing library records on paper or spreadsheets quickly becomes tedious and error-prone. This **Library Management System** replaces manual registers with a modern digital workspace. It provides librarians with an intuitive interface to catalog books, onboard members, track issued titles, and handle returns seamlessly while keeping real-time inventory counts accurate.

---

## ✨ Features

- **📊 Centralized Dashboard**: Real-time stats showing total book titles, active registered members, and currently issued books.
- **📚 Catalog & Book Management**: Add new titles with ISBN, author links, total copies, and track available stock automatically.
- **👥 Member Directory**: Register new library patrons with email and phone contact details.
- **📤 Book Issuance**: Simple workflow to issue available books to members while automatically decrementing the available stock.
- **📥 Return Processing**: One-click return workflow that updates transaction status, logs return timestamps, and restores inventory levels.
- **🛡️ Built-in Admin Interface**: Full control over records via Django's secure administration portal.

---

## 🛠️ Tech Stack

- **Backend**: Python 3, Django 6.x
- **Database**: MySQL (default configuration) / SQLite3 (for quick local setup)
- **Frontend**: HTML5, CSS3, Django Template Engine

---

## 📂 Project Structure

```text
library-management/
│
├── Library_Management_System/   # Main project configuration
│   ├── settings.py              # App settings & database configuration
│   ├── urls.py                  # Root URL routing
│   ├── wsgi.py / asgi.py        # Server deployment configs
│
├── LMS/                         # Main application app
│   ├── models.py                # Database schemas (Book, Author, Member, Staff, Transaction)
│   ├── views.py                 # Core application business logic
│   ├── urls.py                  # App-specific URL routes
│   └── templates/               # HTML Views (home, books, members, issue/return)
│
├── manage.py                    # Django CLI management utility
└── db.sqlite3                   # Local database file
```

---

## 🗄️ Database Models

- **`Author`**: Holds author names (`name`).
- **`Book`**: Stores book details (`title`, `author`, `isbn`, `quantity`, `available_copies`).
- **`Member`**: Stores patron contact information (`name`, `email`, `phone`).
- **`Staff`**: Holds library staff details (`name`, `role`).
- **`Transaction`**: Tracks book movement (`book`, `member`, `issue_date`, `return_date`, `fine`, `status`).

---

## 🚀 Getting Started

Follow these steps to set up and run the project locally on your machine.

### 1. Prerequisites
Make sure you have **Python 3.10+** installed.

### 2. Clone & Set Up Environment
```bash
# Clone the repository
git clone <repository-url>
cd library-management

# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django
```

> 💡 **Database Note**: The project is currently set up to connect to **MySQL** in `Library_Management_System/settings.py`. If you're using MySQL, install `mysqlclient`:
> ```bash
> pip install mysqlclient
> ```
> If you prefer using **SQLite** for local development, update `DATABASES` in `Library_Management_System/settings.py` to:
> ```python
> DATABASES = {
>     'default': {
>         'ENGINE': 'django.db.backends.sqlite3',
>         'NAME': BASE_DIR / 'db.sqlite3',
>     }
> }
> ```

### 4. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin Access)
```bash
python manage.py createsuperuser
```

### 6. Start Development Server
```bash
python manage.py runserver
```

Open your browser and visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/).  
To access the admin dashboard, head to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

---

## 🌟 Future Improvements

- [ ] Overdue fine calculation logic based on return dates
- [ ] Book search, category filtering, and pagination
- [ ] Automated email reminders for overdue books
- [ ] Member borrowing history and limits

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.
