import os
import sqlite3
from sqlite3 import Error


cwd = os.getcwd() + 'database/CL_OC.sqlite'
print(cwd)
def create_connection(path):
    connection = None
    print(path)
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

# create_connection(cwd)