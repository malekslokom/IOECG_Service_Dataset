from flask import Flask, jsonify, request
from flask_cors import CORS
from database import db
from config.config import Config
from consul import register_service_with_consul,SERVICE_PORT

# initialisation de l'application
app = Flask(__name__)
CORS(app)
# configuration de la base de donnée
app.config.from_object(Config)
db.init_app(app)

# les apis
from api import health, getAll, getDatasetById, getDatasetsWithFilter

# les routes
app.route('/api/datasets/health')(health)
app.route('/api/datasets/',methods=["GET"])(getAll)
app.route('/api/datasets/<int:id_project>', methods=["GET"])(getDatasetById)
app.route('/api/datasets/filter', methods=["GET"])(getDatasetsWithFilter)


if __name__ == "__main__":
    register_service_with_consul()
    app.run(debug=True, port=Config.SERVICE_PORT)
