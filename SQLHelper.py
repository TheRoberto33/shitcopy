
import sqlite3

def init():
    global __cur
    global __conn
    __conn = sqlite3.connect("data/JonneBottiDatabase.db")
    __cur = __conn.cursor()


def query(q):
    try:
        res = __cur.execute(q)
    except sqlite3.Error as err:
        print("Error in SQL:")
        print(err)
    return __cur.fetchall()

def execcommit(query, par=()):
    try:
        __cur.execute(query, par)
        __conn.commit()
    except sqlite3.Error as err:
        print("Error in SQL:")
        print(err)




#TODO: Call somewhere
def close():
    __cur.close()
    __conn.close
