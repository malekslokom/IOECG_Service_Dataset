from database import db  

class Analyse(db.Model):
    __tablename__ = 'analyses'

    id_analysis = db.Column(db.Integer, primary_key=True)
    id_project = db.Column(db.Integer, db.ForeignKey('projets.id_project'), nullable=False)
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=db.func.current_timestamp(), nullable=False)
    last_updated_at = db.Column(db.TIMESTAMP(timezone=True), default=db.func.current_timestamp(), nullable=False)
    name_analysis = db.Column(db.String(), nullable=False)
    description_analysis = db.Column(db.Text, default=None)
    created_by = db.Column(db.Text, nullable=False)