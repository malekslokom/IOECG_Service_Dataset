class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgresql@localhost:5432/IOECG' #Window
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgresql@localhost:5433/IOECG'     #Mac
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVICE_PORT = 5001  
