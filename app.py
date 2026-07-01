from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "healthy", "message": "Flask API is running"})

@app.route("/multiply/<int:num1>/<int:num2>")
def multiply(num1, num2):
    return jsonify({"result": num1 * num2})

if __name__ == "__main__":
    app.run(debug=True)
