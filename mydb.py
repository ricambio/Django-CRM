import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='lambrettavespaape83'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All done!")
