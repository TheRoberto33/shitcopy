
import pyodbc

def init():
    DBfile = r"C:\Users\Heikki\PycharmProjects\JonneBotti\data\JonneBottiDatabase.mdb"
    global __cursor
    global __conn
    __conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb)};DBQ=" + DBfile + ";")
    __cursor = __conn.cursor()



def query(q):
    try:
        res = __cursor.execute(q)
    except pyodbc.Error:
        print("Error in SQL!")
        res = None
    return res

#TODO: Call somewhere
def close():
    __cursor.close
    __conn.close