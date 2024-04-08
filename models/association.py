from database import db  

analyses_datasets = db.Table('analyses_datasets',
    db.Column('id_dataset', db.Integer, db.ForeignKey('datasets.id_dataset'), primary_key=True),
    db.Column('id_analysis', db.Integer, db.ForeignKey('analyses.id_analysis'), primary_key=True)
)

# datasets_ecg = db.Table('datasets_ecg',
#     db.Column('id_dataset', db.Integer, db.ForeignKey('datasets.id_dataset'), primary_key=True),
#     db.Column('id_ecg', db.Integer, db.ForeignKey('ecg.id_ecg'), primary_key=True)
# )

datasets_rapport = db.Table('datasets_rapport',
    db.Column('id_dataset', db.Integer, db.ForeignKey('datasets.id_dataset'), primary_key=True),
    db.Column('id_rapport', db.Integer, db.ForeignKey('rapports.id_rapport'), primary_key=True)
)

modeles_rapport = db.Table('modeles_rapport',
    db.Column('id_model', db.Integer, db.ForeignKey('modeles.id_model'), primary_key=True),
    db.Column('id_rapport', db.Integer, db.ForeignKey('rapports.id_rapport'), primary_key=True)
)