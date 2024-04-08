from database import db  
from sqlalchemy import CheckConstraint

class Projet(db.Model):
    __tablename__ = 'projets'

    id_project = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=db.func.current_timestamp(), nullable=False)
    name_project = db.Column(db.String(), nullable=False)
    description_project = db.Column(db.Text, default=None)
    created_by = db.Column(db.Text, nullable=False)
    type_project = db.Column(db.String(), nullable=False)

    analyses = db.relationship('Analyse', backref='projet', lazy=True)
      # Vérification de contrainte pour s'assurer que typeDataset est soit 'search_results' ou 'standard'
    __table_args__ = (
        CheckConstraint(type_project.in_(['classification', 'standard']), name='type_project_check'),
    )