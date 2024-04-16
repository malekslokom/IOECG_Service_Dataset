from database import db  

class Rapport(db.Model):
    __tablename__ = 'rapports'

    id_rapport = db.Column(db.Integer, primary_key=True)
    id_experience_rapport = db.Column(db.Integer, db.ForeignKey('experiences.id_experience'), nullable=False)
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=db.func.current_timestamp(), nullable=False)
    name_rapport = db.Column(db.String(), nullable=False)