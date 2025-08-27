import mysql.connector
#STEP 3 ADD DATA IN TABLE FEILDS
try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="amazon2")

    myCursor = connection.cursor()
# INSERT INTO flats (bhk,floor,price) VALUES ("3BHK",6,"70000000RS")
    query = "INSERT INTO products (category,pro_name,price) VALUES (%s, %s ,%s)"
    data = ("mobile","nokia1300",1500)
    
    myCursor.execute(query, data)
    print("New Records Inserted")
    connection.commit()
    connection.close()
except Exception as err:
    if 'connection' in locals() and connection.is_connected():
        connection.rollback()
        connection.close()
    print("Error is ", err)
PERSON=''