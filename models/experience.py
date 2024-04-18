from sqlalchemy import CheckConstraint
from database import db 
from sqlalchemy.dialects.postgresql.json import JSONB


class Experience(db.Model):
    __tablename__ = 'experiences'

    id_experience = db.Column(db.Integer, primary_key=True)
    name_experience = db.Column(db.String)
    models = db.Column(db.ARRAY(db.Integer), nullable=False)
    datasets = db.Column(db.ARRAY(db.Integer), nullable=False)
    nom_machine = db.Column(db.String())
    nb_gpu = db.Column(db.Integer)
    nb_processeurs = db.Column(db.Integer)
    heure_lancement = db.Column(db.TIMESTAMP(timezone=True), default=db.func.current_timestamp(), nullable=False)
    heure_fin_prevu = db.Column(db.TIMESTAMP(timezone=True), default=db.func.current_timestamp())
    statut = db.Column(db.String(), nullable=False)
    resultat_prediction  = db.Column(JSONB, default=lambda: {})

    __table_args__ = (
        CheckConstraint(statut.in_(['En cours', 'Terminé']), name='check_statut'),
    )
