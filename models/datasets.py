from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Dataset(db.Model):
    __tablename__ = 'datasets'

    id_dataset = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=db.func.current_timestamp(), nullable=False)
    name_dataset = db.Column(db.String(), nullable=False)
    description_dataset = db.Column(db.Text, default=None)
    type_dataset = db.Column(db.String(), nullable=False)
    leads_name = db.Column(db.Text, nullable=False,default="")
    study_name = db.Column(db.String(), nullable=False,default="")
    study_details = db.Column(db.String(), default=None)
    source_name = db.Column(db.String(), nullable=False,default="")
    source_details = db.Column(db.String(), default=None)
    datasetsECG = db.relationship('DatasetsECG', backref='dataset')
    # Vérification de contrainte pour s'assurer que typeDataset est soit 'search_results' ou 'standard'
    __table_args__ = (
        CheckConstraint(type_dataset.in_(['search_results', 'standard']), name='check_type_dataset'),
    )
class Ecg(db.Model):
    __tablename__ = 'ecg'

    id_ecg = db.Column(db.Integer, primary_key=True)
    id_patient = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    filepath = db.Column(db.String, nullable=False)
    recording_started_at = db.Column(db.TIMESTAMP, nullable=False)
    recording_ended_at = db.Column(db.TIMESTAMP, nullable=False)
    recording_initial_sampling_rate = db.Column(db.Integer, nullable=False)
    recording_sampling_rate = db.Column(db.Integer, nullable=False)
    recording_duration = db.Column(db.Integer, nullable=False)
    protocol_details = db.Column(db.JSON)
    datasetsECG = db.relationship('DatasetsECG', backref='ecg')
# class DatasetsECG(db.Model):
#     __tablename__ = 'datasetsECG'

#     idDataset = db.Column(db.Integer, db.ForeignKey('datasets.id_dataset'), primary_key=True)
#     idECG = db.Column(db.Integer, db.ForeignKey('ecg.id_ecg'), primary_key=True)

#     # Define relationships with the Datasets and ECG tables
#     dataset = relationship("Dataset", backref="datasetsECG")
#     ecg = relationship("Ecg", backref="datasetsECG")


class DatasetsECG(db.Model):
    __tablename__ = 'datasets_ecg'

    id_dataset = db.Column(db.Integer, db.ForeignKey('datasets.id_dataset'), primary_key=True)
    id_ecg = db.Column(db.Integer, db.ForeignKey('ecg.id_ecg'), primary_key=True)

    # Define relationships with the Datasets and ECG tables
    # datasets = relationship("Dataset", backref="ecgs")
    # ecg = relationship("Ecg", backref="datasetsECG")
