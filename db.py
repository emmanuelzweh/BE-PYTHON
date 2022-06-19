import sqlite3 as sql

#database connection and creation
# conn = sql.connect("Customers.db")
# myCursor = conn.cursor()

def insertStudent(matricule,nom,prenom,numero_pa, numero_tutor,photo):
    conn = sql.connect("gnote_base.db")
    myCursor = conn.cursor()
    myCursor.executemany('INSERT INTO Etudiant VALUES (?, ?, ?, ?, ?, ?);',matricule,nom,prenom,numero_pa,numero_pa,photo)
    conn.commit()
    conn.close



conn.close()