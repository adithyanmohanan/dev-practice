from flask import Flask, jsonify, request
from flask_bcrypt import Bcrypt
import mysql.connector

import os
from dotenv import load_dotenv

load_dotenv()

print("password loaded:", os.getenv("DB_PASSWORD"))

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="jobs_db"
    )

app = Flask(__name__)
bcrypt = Bcrypt(app)

# GET all jobs
@app.route("/jobs", methods=["GET"])
def get_jobs():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
    SELECT jobs.id, jobs.title, jobs.salary, 
           companies.name AS company_name, companies.location AS company_location
    FROM jobs
    LEFT JOIN companies ON jobs.company_id = companies.id
""")
    jobs = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(jobs)

# GET single job by ID
@app.route("/jobs/<int:id>", methods=["GET"])
def get_job(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
    SELECT jobs.id, jobs.title, jobs.salary,
           companies.name AS company_name, companies.location AS company_location
    FROM jobs
    LEFT JOIN companies ON jobs.company_id = companies.id
    WHERE jobs.id = %s
""", (id,))
    job = cursor.fetchone()
    cursor.close()
    conn.close()
    if job:
        return jsonify(job)
    return jsonify({"error": "Job not found"}), 404

# POST - Create new job
@app.route("/jobs", methods=["POST"])
def create_job():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO jobs (title, company, salary, company_id) VALUES (%s, %s, %s, %s)",
        (data["title"], data["company"], data["salary"], data.get("company_id"))
    )
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return jsonify({"id": new_id, "title": data["title"], "company": data["company"], "salary": data["salary"], "company_id": data.get("company_id")}), 201

# PUT - Update existing job
@app.route("/jobs/<int:job_id>", methods=["PUT"])
def update_job(job_id):
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM jobs WHERE id = %s", (job_id,))
    job = cursor.fetchone()
    if not job:
        cursor.close()
        conn.close()
        return jsonify({"error": "Job not found"}), 404

    title = data.get("title", job["title"])
    company = data.get("company", job["company"])
    salary = data.get("salary", job["salary"])

    update_cursor = conn.cursor()
    update_cursor.execute(
        "UPDATE jobs SET title = %s, company = %s, salary = %s WHERE id = %s",
        (title, company, salary, job_id)
    )
    conn.commit()
    update_cursor.close()
    cursor.close()
    conn.close()

    return jsonify({"id": job_id, "title": title, "company": company, "salary": salary}), 200

# DELETE - Remove a job
@app.route("/jobs/<int:job_id>", methods=["DELETE"])
def delete_job(job_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM jobs WHERE id = %s", (job_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Job deleted"}), 200

# REGISTER - Create a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"error": "Missing fields"}), 400

    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
    existing = cursor.fetchone()

    if existing:
        cursor.close()
        conn.close()
        return jsonify({"error": "Email already registered"}), 409

    cursor.execute(
        "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
        (username, email, hashed_pw)
    )
    conn.commit()
    new_user_id = cursor.lastrowid
    cursor.close()
    conn.close()

    return jsonify({"id": new_user_id, "username": username, "email": email}), 201

# LOGIN - Authenticate a user
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Missing fields"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if not user or not bcrypt.check_password_hash(user['password_hash'], password):
        return jsonify({"error": "Invalid email or password"}), 401

    return jsonify({"id": user['id'], "username": user['username'], "email": user['email']}), 200

if __name__ == "__main__":
    app.run(debug=True)