from sqlalchemy import CheckConstraint
from database import db  

class Modele(db.Model):
    __tablename__ = 'modeles'

    id_model = db.Column(db.Integer, primary_key=True)
    type_model = db.Column(db.String(), nullable=False)

    __table_args__ = (
        CheckConstraint("type_model IN ('Classification', 'Régression', 'Visualisation')", name='check_typeModel'),
    )