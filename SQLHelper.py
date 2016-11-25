import sqlite3




connection = sqlite3.connect("data/JonneBottiDatabase.db")
cursor = connection.cursor()



def query(q, par=()):
    try:
        res = cursor.execute(q, par)
    except sqlite3.Error as err:
        print("Error in SQL:")
        print(err)
    return cursor.fetchall()

def execcommit(query, par=()):
    try:
        cursor.execute(query, par)
        connection.commit()
    except sqlite3.Error as err:
        print("Error in SQL:")
        print(err)




#TODO: Call somewhere
def close():
    cursor.close()
    connection.close()
