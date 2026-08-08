# Job Board

A full-stack job board application where companies can post openings and users can browse and manage listings. Built as a hands-on project to practice backend, frontend, and cloud deployment end-to-end.

**Live demo:** http://job-board-adithyan-2026.s3-website.ap-south-1.amazonaws.com

## Features

- User registration and login with JWT-based authentication
- Passwords hashed with bcrypt (never stored in plain text)
- Create, view, update, and delete job postings
- Ownership checks — users can only edit or delete jobs they posted
- Relational data model — jobs linked to companies via foreign keys
- Deployed live: Flask API on AWS EC2, React frontend on AWS S3

## Tech Stack

**Backend:** Python, Flask, Flask-JWT-Extended, Flask-Bcrypt, MySQL
**Frontend:** React, Axios
**Deployment:** AWS EC2 (Gunicorn + systemd), AWS S3 (static hosting)

## API Endpoints

| Method | Endpoint | Description | Auth required |
|--------|----------|-------------|----------------|
| POST | `/register` | Create a new user account | No |
| POST | `/login` | Authenticate and receive a JWT | No |
| GET | `/jobs` | List all job postings | No |
| GET | `/jobs/<id>` | Get a single job posting | No |
| POST | `/jobs` | Create a new job posting | Yes |
| PUT | `/jobs/<id>` | Update a job posting (owner only) | Yes |
| DELETE | `/jobs/<id>` | Delete a job posting (owner only) | Yes |

## Running Locally

**Backend**
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# create a .env file with DB_PASSWORD and JWT_SECRET_KEY
python jobs_api.py
