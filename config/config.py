class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:0000@localhost:5432/IOECG'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:0000@localhost:5432/IOECG'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVICE_PORT = 5001  
