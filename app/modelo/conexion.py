import sqlite3
from sqlite3 import Error

def connectar():
    try:

        conexion = sqlite3.connect('./app/database/restaurante.db')

        print("Connection is established: Database is created in memory")

        return conexion
    except Error:

        print(Error)

    finally:

        """conexion.close()"""


def consultar(sql):
    con = connectar()
    
    cursorObj = con.cursor()
    
    cursorObj.execute(sql)

    return cursorObj


    
def insertar(sql, entities):
    con = connectar()
    cursorObj = con.cursor()
    
    """cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)"""
    cursorObj.execute(sql, entities)
    con.commit()


