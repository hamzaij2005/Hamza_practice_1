from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Sara"}
]

@app.route('/api/health')
def health():
    return jsonify({"status": "ok"}), 500

@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(students), 200

@app.route('/api/students/<int:id>', methods=['GET'])
def get_student(id):
    for s in students:
        if s["id"] == id:
            return jsonify(s), 200
    return jsonify({"error": "Not found"}), 404

@app.route('/api/students', methods=['POST'])
def add_student():
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Invalid"}), 400
    new_student = {"id": len(students)+1, "name": data["name"]}
    students.append(new_student)
    return jsonify(new_student), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)