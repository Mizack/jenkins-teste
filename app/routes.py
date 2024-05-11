from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
DEBUG = False

@app.route("/", methods=["GET"])
def home():
    return {
        "message": "It`s works"
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=DEBUG)