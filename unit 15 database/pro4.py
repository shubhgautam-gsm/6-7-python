import mysql.connector
#STEP 1 CREATE DATABSE AND CONNECT TO MYSQL
try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="")
    print("Database Connected")
    myCursor = connection.cursor()
    query = "create database Amazon2"
    result = myCursor.execute(query)
    print("Database Created")

    connection.close()
except Exception as err:
    print("Error is ",err)