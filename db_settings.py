from configparser import ConfigParser
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app_settings import *
from models import Base
import messages
from getpass import getpass
import messages
import time
import os

config = ConfigParser()
config.read('config.ini')

db_values = {
    'db_name' : "",
    'db_user' : "",
    'db_password' : "",
    'db_host' : "",
    'db_port' : ""
}

def initiliaze_db():
    db_values.update({
        'db_name' : config.get('database', 'name'),
        'db_user' : config.get('database', 'user'),
        'db_password' : config.get('database', 'password'),
        'db_host' : config.get('database', 'host'),
        'db_port' : config.get('database', 'port')
    })

def connect_db():
    initiliaze_db()
    try:
        DB_USER = db_values.get('db_user')
        DB_PASSWORD = db_values.get('db_password')
        DB_HOST = db_values.get('db_host')
        DB_PORT = db_values.get('db_port')
        DB_NAME = db_values.get('db_name')
        engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        if session.query(text('1')).first():
            print(messages.CONNECTED_TO_DATABASE_MESSAGE)
            time.sleep(0.5)
            return session
    except Exception as e:
        os.system("cls")
        print(messages.DATABASE_CONNECTION_ERROR, e)
        time.sleep(0.5)
        set_db()

def set_db():
    print(messages.ENTER_DATABASE_CONFIGURATION)
    db_name = input(messages.ENTER_DATABASE_NAME)
    db_user = input(messages.ENTER_DATABASE_USER)
    db_password = getpass(messages.ENTER_DATABASE_PASSWORD)
    db_host = input(messages.ENTER_DATABASE_HOST)
    db_port = input(messages.ENTER_DATABASE_PORT)

    config.set('database', 'name', db_name)
    config.set('database', 'user', db_user)
    config.set('database', 'password', db_password)
    config.set('database', 'host', db_host)
    config.set('database', 'port', db_port)
    
    with open('config.ini', 'w') as config_file:
        config.write(config_file)
    