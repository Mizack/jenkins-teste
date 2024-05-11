from app.routes import app, DEBUG

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=DEBUG)

def create_app():
    return app