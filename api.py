import json
from datetime import datetime
from flask import jsonify, request
from models.dataset import Dataset,db,DatasetsECG


from models import *
from database import db

def health():
    return jsonify({"status": "up"})

def getAll():
    # Récupérer tous les modèles depuis la base de données
    datasets = Dataset.query.all()
    # Convertir les données des enregistrements en un format JSON
    dataset_data = [{
  "id_dataset": dataset.id_dataset,
            "created_at": dataset.created_at,
            "name_dataset": dataset.name_dataset,
            "description_dataset": dataset.description_dataset,
            "type_dataset": dataset.type_dataset,
            "leads_name": dataset.leads_name,
            "study_name": dataset.study_name,
            "study_details": dataset.study_details,
            "source_name": dataset.source_name,
            "source_details": dataset.source_details
    } for dataset in datasets]

    # Renvoyer les données des enregistrements au format JSON
    return jsonify(dataset_data)

def getDatasetById(id_dataset):
    dataset = Dataset.query.filter_by(id_dataset=id_dataset).first()
    if dataset:
        # Convertir l'objet Dataset en un dictionnaire
        dataset_data = {
            "id_dataset": dataset.id_dataset,
            "created_at": dataset.created_at,
            "name_dataset": dataset.name_dataset,
            "description_dataset": dataset.description_dataset,
            "type_dataset": dataset.type_dataset,
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

def getDatasetsWithFilter():
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
        query = query.filter((Dataset.name_dataset.ilike(f'%{search_term}%')) |
                             (Dataset.description_dataset.ilike(f'%{search_term}%')) |
                             (Dataset.type_dataset.ilike(f'%{search_term}%')) |
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
            "id_dataset": dataset.id_dataset,
            "created_at": dataset.created_at.strftime("%d-%m-%Y"),
            "name_dataset": dataset.name_dataset,
            "description_dataset": dataset.description_dataset,
            "type_dataset": dataset.type_dataset,
            "leads_name": dataset.leads_name,
            "study_name": dataset.study_name,
            "study_details": dataset.study_details,
            "source_name": dataset.source_name,
            "source_details": dataset.source_details
        } for dataset in filtered_datasets]
        return jsonify(dataset_data)
    else:
        return jsonify({"error": "No datasets found matching the criteria"}), 404



def create_dataset():
    try:
        # Extract dataset name, description, and type from the request body
        data = request.json
        name = data.get('name')
        description = data.get('description')
        type_dataset = data.get('type_dataset')
        leads_name=  data.get('leads_name')
        study_details=  data.get('study_details')
        source_name = data.get('source_name')
        source_details  = data.get('source_details')
        study_name  = data.get('study_name')
        # Create a new dataset in the database
        new_dataset = Dataset(name_dataset=name, description_dataset=description, type_dataset=type_dataset,leads_name= leads_name,study_details=  study_details,source_name =source_name,source_details  =source_details,study_name  = study_name)
        db.session.add(new_dataset)
        db.session.commit()

        # Return the ID of the newly created dataset
        return jsonify({"id_dataset": new_dataset.id_dataset}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def associate_ecgs_with_dataset(dataset_id):
    try:
        # Extract list of selected ECGs from the request body
        data = request.json
        selected_ecgs = data.get('ecgs')
        print("selected_ecgs")
        print(selected_ecgs)
        # Associate selected ECGs with the dataset in the database
        for ecg_id in selected_ecgs:
            print(ecg_id)
            new_association = DatasetsECG(id_dataset=dataset_id, id_ecg=ecg_id)
            db.session.add(new_association)
        
        db.session.commit()

        return jsonify({"message": "ECGs associated with dataset successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def addDataset():
    data = request.json  
    print(data)
    name_dataset = data.get('name_dataset')
    created_at = data.get('created_at')
    description = data.get('description_dataset')
    type_dataset = "standard"
    study_name= data.get('study_name')
    source_name=data.get('source_name')
    # Ajout du nouveau Dataset
    new_dataset = Projet(name_dataset=name_dataset, created_at=created_at, description_dataset=description, type_dataset=type_dataset,
                              study_name=study_name,source_name=source_name)   

    # Ajouter dans la bdd
    db.session.add(new_dataset)
    try:
        # Valider et enregistrer les modifications dans la bdd
        db.session.commit()
        return jsonify({"message": "Dataset ajouté avec succès"}), 201
    except Exception as e:
        # Erreur, annuler les modifications et renvoyer un message d'erreur
        db.session.rollback()
        return jsonify({"error": str(e)}), 500