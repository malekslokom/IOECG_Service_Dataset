from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
db = SQLAlchemy()

class Dataset(db.Model):
    __tablename__ = 'datasets'

    idDataset = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=db.func.current_timestamp(), nullable=False)
    nameDataset = db.Column(db.String(), nullable=False)
    descriptionDataset = db.Column(db.Text, default=None)
    typeDataset = db.Column(db.String(), nullable=False)
    leads_name = db.Column(db.Text, nullable=False)
    study_name = db.Column(db.String(), nullable=False)
    study_details = db.Column(db.String(), default=None)
    source_name = db.Column(db.String(), nullable=False)
    source_details = db.Column(db.String(), default=None)

    # Vérification de contrainte pour s'assurer que typeDataset est soit 'search_results' ou 'standard'
    __table_args__ = (
        CheckConstraint(typeDataset.in_(['search_results', 'standard']), name='check_type_dataset'),
    )