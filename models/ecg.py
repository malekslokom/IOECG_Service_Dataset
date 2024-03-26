from database import db  
from sqlalchemy.dialects.postgresql.json import JSONB
class ECG(db.Model):
    __tablename__ = 'ecg'

    id_ecg = db.Column(db.Integer, primary_key=True)
    id_patient = db.Column(db.Integer, nullable=False)
    filepath = db.Column(db.String(), nullable=False)
    recording_started_at = db.Column(db.TIMESTAMP, nullable=False)
    recording_ended_at = db.Column(db.TIMESTAMP, nullable=False)
    recording_initial_sampling_rate = db.Column(db.Integer, nullable=False)
    recording_sampling_rate = db.Column(db.Integer, nullable=False)
    recording_duration = db.Column(db.Integer, nullable=False)
    protocol_details = db.Column(JSONB, default=lambda: {})