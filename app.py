from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify(<center><h3>{"message": "Hello, World!"}</h3></center>)

if __name__ == "__main__":
    app.run()
