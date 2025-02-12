from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_task():
    task = request.args.get('task')
    if not task:
        return jsonify({"error": "Task description required"}), 400
    return jsonify({"message": f"Executing task: {task}"}), 200

@app.route('/read', methods=['GET'])
def read_file():
    file_path = request.args.get('path')
    if not file_path or not file_path.startswith("/data/"):
        return jsonify({"error": "Invalid file path"}), 400
    try:
        with open(file_path, 'r') as file:
            return file.read(), 200
    except FileNotFoundError:
        return "", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
