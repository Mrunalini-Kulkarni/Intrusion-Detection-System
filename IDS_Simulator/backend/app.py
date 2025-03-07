# backend/app.py

from flask import Flask
from routes.ids_routes import ids_bp  # Import the Blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Register the Blueprint
app.register_blueprint(ids_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)