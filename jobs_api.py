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

if __name__ == "__main__":
    app.run(debug=True)