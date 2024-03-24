from flask import Flask, jsonify, request
from flask_cors import CORS
from models.datasets import db, Dataset
from config.config import Config

# initialisation de l'application
app = Flask(__name__)
CORS(app)
# configuration de la base de donnée
app.config.from_object(Config)
db.init_app(app)

# les apis
from api import health, getAll, getDatasetById, filter_data

# les routes
app.route('/api/datasets/health')(health)
app.route('/api/datasets/',methods=["GET"])(getAll)
app.route('/api/datasets/<int:id>', methods=["GET"])(getDatasetById)
app.route('/api/datasets/filter', methods=['GET'])(filter_data)

if __name__ == "__main__":
    # Créer la base de données
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=Config.SERVICE_PORT)
