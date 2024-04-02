import sqlite3
import click, os, mysql.connector as connector
import pymysql.cursors

from datetime import datetime
from werkzeug.security import generate_password_hash
from sqlalchemy import create_engine, text
from flask import current_app, g
#from dotenv import load_dotenv

#load_dotenv()

def connection():
    try:
        c = pymysql.connect(
            host=current_app.config["MYSQL_HOST"],
            user=current_app.config["MYSQL_USER"],
            passwd=current_app.config["MYSQL_PASS"],
            database=current_app.config["MYSQL_DATABASE"],
            port=current_app.config["MYSQL_PORT"],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return c
    except:
        print('Erro de Conexão')
        exit(1)

def dockerconnect():
    try:
        c = pymysql.connect(
            host=current_app.config["MYDOCKER_HOST"],
            user=current_app.config["MYDOCKER_USER"],
            passwd=current_app.config["MYDOCKER_PASS"],
            database=current_app.config["MYDOCKER_DATABASE"],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return c
    except:
        print('Erro de Conexão')
        exit(1)


def get_db():
    typeconnect = current_app.config["TYPE_CONNECT"]
    print('Tipo de conexão: ',typeconnect)
    if 'db' not in g:
        if typeconnect == 'sqlite':
            g.db = sqlite3.connect(
                current_app.config['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES
            )
            g.db.row_factory = sqlite3.Row
            print('USANDO SQLITE')
        if typeconnect == 'mysql':
            try:
                g.db = connection().cursor()
                print('USANDO MYSQL')
            except:
                print('FALHA NA CONEXÃO')
        if typeconnect == 'mydocker':
            try:
               g.db = dockerconnect().cursor()
               print('USANDO MYDOCKER')
            except:
               print('FALHA NA CONEXÃO')
    return g.db

def close_db(e=None):
    db = g.pop('db',None)

    if db is not None:
        db.close()
#        cnx.close()

def init_db():
    typeconnect = os.getenv('TYPE_CONNECT')
    db = get_db()

    if typeconnect == 'sqlite':
        with current_app.open_resource('database\schemas\initsqlite.sql') as f:
            db.executescript(f.read().decode('utf8'))

    if typeconnect == 'mysql':
        with current_app.open_resource('database\schemas\initmysql.sql') as f:
            for x in f:
                query = x[0:len(x)-2]
                db.execute(query)
        f.close()

def atualiza_lf():
    typeconnect = current_app.config["TYPE_CONNECT"]
    db = get_db()
    if typeconnect == 'mysql':
        with current_app.open_resource('database\schemas\lfatualiza.sql') as f:
            for x in f:
                query = x[0:len(x)-2]
                db.execute(query)
        f.close()

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    click.echo('Limpando o Banco de Dados e criando as tabelas básicas')
    init_db()
    click.echo('database inicializado.')

@click.command('atualiza-lf')
def atualiza_lf_command():
    """Atualizando resultados"""
    click.echo('Atualizando a tabela de resultados')
    atualiza_lf()
    click.echo('Resultados atualizados')

def atualiza_lf_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(atualiza_lf_command)

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

