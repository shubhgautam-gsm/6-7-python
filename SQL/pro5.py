import mysql.connector

try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="",
    database="mayur_store")

    myCursor = connection.cursor()
    query = "create table studybook (bookid int auto_increment primary key, bookname varchar(128)," \
            " price varchar(25))"
    result = myCursor.execute(query)
    print("Table Created")
    connection.close()
except Exception as err:
    print("Error is ",err)