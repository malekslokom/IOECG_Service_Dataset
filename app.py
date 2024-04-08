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

from api import health, getAll, getDatasetById, getDatasetsWithFilter,create_dataset,associate_ecgs_with_dataset

# les routes
app.route('/api/datasets/health')(health)
app.route('/api/datasets/',methods=["GET"])(getAll)
app.route('/api/datasets/<int:id_project>', methods=["GET"])(getDatasetById)
app.route('/api/datasets/filter', methods=["GET"])(getDatasetsWithFilter)
app.route('/api/datasets/<int:dataset_id>/datasetEcg', methods=['POST'])(associate_ecgs_with_dataset)
app.route('/api/datasets', methods=['POST'])(create_dataset)





if __name__ == "__main__":
    register_service_with_consul()
    # Créer la base de données
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=Config.SERVICE_PORT)
