from database import db  
class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=db.func.current_timestamp(), nullable=False)
    last_updated_at = db.Column(db.TIMESTAMP(timezone=True), default=db.func.current_timestamp(), nullable=False)
    dataset_id = db.Column(db.Integer, db.ForeignKey('datasets.id_dataset'), nullable=False)
    patient_original_id = db.Column(db.String(), nullable=False)
    age = db.Column(db.Integer)
    birth_date = db.Column(db.String())
    height = db.Column(db.String())
    weight = db.Column(db.String())
    sex = db.Column(db.Enum('Male', 'Female', 'Unknown', name='sex'), nullable=False)
    race = db.Column(db.String())
    observation = db.Column(db.Text)