import mysql.connector

#STEP 2 CREATE TABLE IN DATABASE alratv_app
try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="amazon2")

    myCursor = connection.cursor()
    query = "CREATE TABLE products ( category VARCHAR(12) ,pro_name VARCHAR(15), price int(6))"
    result = myCursor.execute(query)
    print("Table Created")

    connection.close()
except Exception as err:
    print("Error is ", err)



