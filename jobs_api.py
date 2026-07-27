from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary database (list of jobs)
jobs = [
    {"id": 1, "title": "Backend Developer", "company": "TechStartup", "salary": 45000},
    {"id": 2, "title": "Full Stack Developer", "company": "ProductCo", "salary": 50000},
    {"id": 3, "title": "Python Developer", "company": "DataFirm", "salary": 40000}
]

# GET all jobs
@app.route("/jobs", methods=["GET"])
def get_jobs():
    return jsonify(jobs)

# GET single job by ID
@app.route("/jobs/<int:id>", methods=["GET"])
def get_job(id):
    job = next((j for j in jobs if j["id"] == id), None)
    if job:
        return jsonify(job)
    return jsonify({"error": "Job not found"}), 404

# POST - Create new job
@app.route("/jobs", methods=["POST"])
def create_job():
    data = request.get_json()
    new_job = {
        "id": len(jobs) + 1,
        "title": data["title"],
        "company": data["company"],
        "salary": data["salary"]
    }
    jobs.append(new_job)
    return jsonify(new_job), 201

# PUT - Update existing job
@app.route("/jobs/<int:job_id>", methods=["PUT"])
def update_job(job_id):
    data = request.get_json()
    for job in jobs:
        if job["id"] == job_id:
            job["title"] = data.get("title", job["title"])
            job["company"] = data.get("company", job["company"])
            job["salary"] = data.get("salary", job["salary"])
            return jsonify(job), 200
    return jsonify({"error": "Job not found"}), 404

# DELETE - Remove a job
@app.route("/jobs/<int:job_id>", methods=["DELETE"])
def delete_job(job_id):
    global jobs
    jobs = [job for job in jobs if job["id"] != job_id]
    return jsonify({"message": "Job deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)

