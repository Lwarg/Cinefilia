import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Database",
    database = "cinefilia"
)

username = input ("Inserisci il tuo username: ")
password = input ("Inserisci la tua password: ")

mycursor = db.cursor()
mycursor.execute("INSERT INTO Utente (username,password) VALUES (%s,%s)",(username,password))
db.commit()
db.close()