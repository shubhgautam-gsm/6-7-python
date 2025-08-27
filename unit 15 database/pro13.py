import mysql.connector

try:
    # create connection and cursor objects
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="hvc_college")
    cursor = connection.cursor()

    # build a query
    query = "update bca set Name = 'majin Kuu' where Roll = '8'"

    # execute query
    cursor.execute(query)
    print(cursor.rowcount,"Records Updated")

    connection.commit()
    connection.close()
except Exception as err:
    connection.rollback()
    print("Error is ",err)
