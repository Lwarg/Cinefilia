import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Database",
    database = "cinefilia"
)

#Da usare solo una volta
mycursor = db.cursor()

mycursor.execute("CREATE TABLE Utente (username VARCHAR(20) PRIMARY KEY NOT NULL, password VARCHAR(20) NOT NULL)")
mycursor.execute("CREATE TABLE Film (user VARCHAR(20) PRIMARY KEY NOT NULL, Titolo VARCHAR(200) NOT NULL)")

db.close()