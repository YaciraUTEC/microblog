#Aquí se le dice a SQLAchemy como conectarse la base de datos
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #coger nuestras variables de entorno (en .flaskenv) el URL de conexion para la base de datos
    #environ: variable de entorno
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')or\
         'postgresq1://postgres:UTEC@localhost:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False