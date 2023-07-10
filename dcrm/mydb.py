import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'abcd1234'

)

cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE db")

print("Done!")
