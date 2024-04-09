from database import db  

analyses_datasets = db.Table('analyses_datasets',
    db.Column('id_dataset', db.Integer, db.ForeignKey('datasets.id_dataset'), primary_key=True),
    db.Column('id_analysis', db.Integer, db.ForeignKey('analyses.id_analysis'), primary_key=True)
)

analyses_modeles = db.Table('analyses_modeles',
    db.Column('id_model_analysis', db.Integer, primary_key=True), 
    db.Column('id_model', db.Integer, db.ForeignKey('modele.id_model'), primary_key=True),
    db.Column('id_analysis', db.Integer, db.ForeignKey('analyses.id_analysis'), primary_key=True)
)


#datasets_rapport = db.Table('datasets_rapport',
#    db.Column('id_dataset', db.Integer, db.ForeignKey('datasets.id_dataset'), primary_key=True),
#    db.Column('id_rapport', db.Integer, db.ForeignKey('rapports.id_rapport'), primary_key=True)
#)

