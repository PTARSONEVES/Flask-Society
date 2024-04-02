import os
from dotenv import load_dotenv 

load_dotenv()

Download_PATH = 'wkhtmltopdf/bin/wkhtmltopdf.exe'
basedir = os.path.abspath(os.path.dirname(__file__))
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
Download_FOLDER = os.path.join(APP_ROOT, Download_PATH)


class BaseConfig(object):
    """Base configuration."""
    #DADOS DA EMPRESA

    EMPRESA_RSOC = 'S T Araujo'
    EMPRESA_NOMFAN = 'Society dos Amigos'
    EMPRESA_LOGRADOURO = 'Rua da Solidariedade'
    EMPRESA_NUMLOGR = '1'
    EMPRESA_COMPLEMENTO = 'Sitio Canoas'
    EMPRESA_BAIRRO = 'Nossa Senhora do Ó'
    EMPRESA_CODMUN = ''
    EMPRESA_CODUF = ''
    EMPRESA_CODPAIS = '55'

    #CONFIDENCIAL
#    SECRET_KEY = os.getenv('SECRET_KEY')
#    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT')
    SECRET_KEY = 'dev'
    SECURITY_PASSWORD_SALT = 'dev-two'
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    #BANCO DE DADOS
    TYPE_CONNECT = 'mysql'
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLITE - LOCALHOST
    SQLITE_CONNECT = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')
    #MYSQL_HOST = 'localhost'
    MYSQL_HOST = 'flask_society.mysql.dbaas.com.br'
    MYSQL_USER = 'flask_society'
    #MYSQL_USER = 'flask_loterias'
    MYSQL_PASS = 'Strol!ndi!1'
    #MYSQL_PASS = 'Strol!ndi!1'
    MYSQL_PORT = 3306
    MYSQL_DATABASE = 'flask_society'
    # DOCKER
    MYDOCKER_HOST = 'localhost'
    MYDOCKER_USER = 'root'
    MYDOCKER_PASS = 'strolandia'
    MYDOCKER_PORT = 3307
    MYDOCKER_DATABASE = 'docker_flask'
    #CORRESPONDENCIA
    MAIL_SERVER='email-ssl.com.br'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USE_SSL=True
    MAIL_DEFAULT_SENDER="ptarsoneves@squallo.net"
    MAIL_USERNAME='ptarsoneves@squallo.net'
    MAIL_PASSWORD='Pt@rso334@'


    #CORRESPONDENCIA

class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')
    DEBUG_TB_ENABLED = True


class TestingConfig(BaseConfig):
    """Testing configuration."""
    TESTING = True
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'
    DEBUG_TB_ENABLED = False
    STRIPE_SECRET_KEY = 'foo'
    STRIPE_PUBLISHABLE_KEY = 'bar'
