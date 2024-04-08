from database import db  
class ECGLead(db.Model):
    __tablename__ = 'ecg_leads'

    id_ecg_lead = db.Column(db.Integer, primary_key=True)
    ecg_id = db.Column(db.Integer, db.ForeignKey('ecg.id_ecg'), nullable=False)
    patient_id = db.Column(db.Integer, nullable=False)
    dataset_id = db.Column(db.Integer, db.ForeignKey('datasets.id_dataset'), nullable=False)
    lead_i = db.Column(db.ARRAY(db.Float))
    lead_ii = db.Column(db.ARRAY(db.Float))
    lead_iii = db.Column(db.ARRAY(db.Float))
    lead_avr = db.Column(db.ARRAY(db.Float))
    lead_avf = db.Column(db.ARRAY(db.Float))
    lead_avl = db.Column(db.ARRAY(db.Float))
    lead_v1 = db.Column(db.ARRAY(db.Float))
    lead_v2 = db.Column(db.ARRAY(db.Float))
    lead_v3 = db.Column(db.ARRAY(db.Float))
    lead_v4 = db.Column(db.ARRAY(db.Float))
    lead_v5 = db.Column(db.ARRAY(db.Float))
    lead_v6 = db.Column(db.ARRAY(db.Float))
    lead_x = db.Column(db.ARRAY(db.Float))
    lead_y = db.Column(db.ARRAY(db.Float))
    lead_z = db.Column(db.ARRAY(db.Float))
    lead_es = db.Column(db.ARRAY(db.Float))
    lead_as = db.Column(db.ARRAY(db.Float))
    lead_ai = db.Column(db.ARRAY(db.Float))