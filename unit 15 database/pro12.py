import mysql.connector

try:
    # create connection and cursor objects
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="hvc_college")
    cursor = connection.cursor()

    # build a query
    query = "select * from bca"

    # execute query
    cursor.execute(query)

    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())    
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())

    connection.commit()
    connection.close()
except Exception as err:
    connection.rollback()
    print("Error is ",err)
