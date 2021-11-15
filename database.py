import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Connection with Database
def database_connect():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='app',
        auth_plugin='mysql_native_password'
        )

# Reads and returs the content
def read_database(sql):
    my_database = database_connect()
    mycursor = my_database.cursor(dictionary=True)
    mycursor.execute(sql)
    content = mycursor.fetchall()
    mycursor.close()
    my_database.close()
    return content

# Action with multiple arguments
def write_database(sql, args):
    my_database = database_connect()
    mycursor = my_database.cursor(dictionary=True)
    mycursor.execute(sql,args)
    my_database.commit()
    mycursor.close()
    my_database.close()

# Single action with database
def action_database(sql):
    my_database = database_connect()
    mycursor = my_database.cursor(dictionary=True)
    mycursor.execute(sql)
    my_database.commit()
    mycursor.close()
    my_database.close()
