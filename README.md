Student Task Manager

Student Task Manager is a web-based application to help students manage their school life more efficiently. It allows users to create, track, and categorize their tasks such as homework, exams, and projects with options such as deadlines, urgency levels, and a graphical dashboard.

Features:

User registration & authentication

Task categorization (Homework, Exam, Project)

Start & due date tracking

Urgency level: Low, Medium, High, Critical

Task completion status

Dashboard summary with stats

Sort tasks by start date, due date, or urgency

Countdown until task deadlines

Tech Stack:

Backend: Django 5

Frontend: HTML, CSS (custom)

Database: SQLite (for development)

Getting Started

Prerequisites:

Python 3.10+

pip (Python package installer)

Git (optional but recommended)

Setup Instructions:

Clone the repository:
git clone https://github.com/yourusername/student-task-manager.git
cd student-task-manager

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate # On Windows: venv\\Scripts\\activate

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Run the development server:
python manage.py runserver

Access the app:
Open http://127.0.0.1:8000/ in your browser.

Project Structure:
student-task-manager/
├── tasks/ # Main app
├── users/ # Auth service
├── templates/ # HTML
├── static/ # CSS & assets
├── db.sqlite3 # Dev db file
├── manage.py # Django start
└── README.md # This markdown file

Feedback:
Have friends test the app and give some feedback! It's a great way to learn and evaluate your project in real conditions.

License:
This is an educational purposes only or personal use project.
