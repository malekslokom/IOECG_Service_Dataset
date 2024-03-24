import json
from datetime import datetime
from flask import jsonify, request
from models.datasets import Dataset


def health():
    return jsonify({"status": "up"})

def getAll():
    # Récupérer tous les modèles depuis la base de données
    datasets = Dataset.query.all()
    # Convertir les données des enregistrements en un format JSON
    dataset_data = [{
        "idDataset": dataset.idDataset,
        "created_at": dataset.created_at,
        "nameDataset": dataset.nameDataset,
        "descriptionDataset": dataset.descriptionDataset,
        "typeDataset": dataset.typeDataset,
        "leads_name": dataset.leads_name,
        "study_name": dataset.study_name,
        "study_details": dataset.study_details,
        "source_name": dataset.source_name,
        "source_details": dataset.source_details
    } for dataset in datasets]

    # Renvoyer les données des enregistrements au format JSON
    return jsonify(dataset_data)

def getDatasetById(id):
    dataset = Dataset.query.filter_by(idDataset=id).first()
    if dataset:
        # Convertir l'objet Dataset en un dictionnaire
        dataset_data = {
            "idDataset": dataset.idDataset,
            "created_at": dataset.created_at,
            "nameDataset": dataset.nameDataset,
            "descriptionDataset": dataset.descriptionDataset,
            "typeDataset": dataset.typeDataset,
            "leads_name": dataset.leads_name,
            "study_name": dataset.study_name,
            "study_details": dataset.study_details,
            "source_name": dataset.source_name,
            "source_details": dataset.source_details
        }
        return jsonify(dataset_data)
    else:
        return jsonify({"error": "Dataset not found"}), 404

def convert_date(date_str):
    """Converts a date string from DD-MM-YYYY to a datetime object."""
    return datetime.strptime(date_str, "%d-%m-%Y")

def filter_data():
    start_date_str = request.args.get('start_date', '')
    end_date_str = request.args.get('end_date', '')
    search_term = request.args.get('search_term', '').lower()
    
    # Convertir les dates de début et de fin de chaînes en objets datetime
    start_date = convert_date(start_date_str) if start_date_str else None
    end_date = convert_date(end_date_str) if end_date_str else None

    # Construction de la requête de filtrage basée sur les paramètres
    query = Dataset.query
    if start_date:
        query = query.filter(Dataset.created_at >= start_date)
    if end_date:
        query = query.filter(Dataset.created_at <= end_date)
    if search_term:
        query = query.filter((Dataset.nameDataset.ilike(f'%{search_term}%')) |
                             (Dataset.descriptionDataset.ilike(f'%{search_term}%')) |
                             (Dataset.typeDataset.ilike(f'%{search_term}%')) |
                             (Dataset.leads_name.ilike(f'%{search_term}%')) |
                             (Dataset.study_name.ilike(f'%{search_term}%')) |
                             (Dataset.study_details.ilike(f'%{search_term}%')) |
                             (Dataset.source_name.ilike(f'%{search_term}%')) |
                             (Dataset.source_details.ilike(f'%{search_term}%')))

    # Exécution de la requête et récupération des résultats
    filtered_datasets = query.all()

    if filtered_datasets:
        # Convertir les résultats en une liste de dictionnaires
        dataset_data = [{
            "idDataset": dataset.idDataset,
            "created_at": dataset.created_at,
            "nameDataset": dataset.nameDataset,
            "descriptionDataset": dataset.descriptionDataset,
            "typeDataset": dataset.typeDataset,
            "leads_name": dataset.leads_name,
            "study_name": dataset.study_name,
            "study_details": dataset.study_details,
            "source_name": dataset.source_name,
            "source_details": dataset.source_details
        } for dataset in filtered_datasets]
        return jsonify(dataset_data)
    else:
        return jsonify({"error": "No datasets found matching the criteria"}), 404