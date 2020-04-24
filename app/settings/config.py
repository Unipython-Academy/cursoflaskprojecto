import os

bdd = os.path.join(os.getcwd(), "Unipythontweet.sqlite").replace('\\', '/')

class Ajustes(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'flask-course'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(bdd)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 3

class ConexionMail(object):

    MAIL_SERVER= 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = '' #Tu gmail
    MAIL_PASSWORD = '' # Contraseña del gmail
    ADMINS = '' # Colocas el mismo gmail que pasaste en MAIL_USERNAME