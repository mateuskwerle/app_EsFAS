# backend/config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'd2a1b9c8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0'
    # Substitua a linha antiga da URI do SQLite por esta nova
    # Detalhes do seu banco de dados MySQL
    #db_username = 'esfasBM'  # Substitua pelo seu username do PythonAnywhere
    #db_password = 'eF!sYWtDN8bucLm' # Substitua pela senha que você criou no Passo 1
    #db_host = 'esfasBM.mysql.pythonanywhere-services.com'
    #db_name = 'esfasBM$default'
    #SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{db_username}:{db_password}@{db_host}/{db_name}'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'escola.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BABEL_DEFAULT_LOCALE = 'pt_BR'

    @staticmethod
    def init_app(app):
        """
        Executa verificações de configuração depois que a app foi criada.
        Isso evita erros durante a importação em ambientes de teste.
        """
        if not app.config.get("SECRET_KEY") and not app.testing:
            raise ValueError("No SECRET_KEY set for Flask application. Set the SECRET_KEY environment variable.")