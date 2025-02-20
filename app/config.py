import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Mysql%402942@localhost/weather_db_1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
