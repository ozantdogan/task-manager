import configparser

config = configparser.ConfigParser()
config.read('config.ini')

import psycopg2
import os
import time

#Database configuration information
#
while True:
    try:
        DB_NAME = config.get('database', 'name')
        DB_USER = config.get('database', 'user')
        DB_PASSWORD = config.get('database', 'password')
        DB_HOST = config.get('database', 'host')
        DB_PORT = config.get('database', 'port')
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        if result[0] == 1:
            print("Connected to database successfully.")
            time.sleep(0.25)
            break
    except Exception as e:
        os.system("cls")
        time.sleep(0.5)
        print()
        print("Please enter the database configuration:")
        DB_NAME = input("Database name: ")
        DB_USER = input("Database user: ")
        DB_PASSWORD = input("Database password: ")
        DB_HOST = input("Database host: ")
        DB_PORT = input("Database port: ")
        config.set('database', 'name', DB_NAME)
        config.set('database', 'user', DB_USER)
        config.set('database', 'password', DB_PASSWORD)
        config.set('database', 'host', DB_HOST)
        config.set('database', 'port', DB_PORT)
        with open('config.ini', 'w') as config_file:
            config.write(config_file)
    

#Completed task status
#
COMPLETED = '☑️'
NOT_COMPLETED = '🔳'

#Commands
#
CLEAR = "-clr"
ALL = "-a"