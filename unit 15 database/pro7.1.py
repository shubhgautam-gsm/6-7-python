import mysql.connector
#STEP 3 ADD DATA IN TABLE FEILDS
try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="hvc_college")

    myCursor = connection.cursor()
    query = "INSERT INTO bca (Name,City,Contact) VALUES ( %s, %s,%s)"
    data = [( "majiv sheikh", "rajkot",7066947730)
            ,( "kajiv sheikh", "aajkot",7066947860),
            ( "sajiv sheikh", "najkot",7066947837)]
    
    myCursor.executemany(query, data)
    print("New Records Inserted")
    connection.commit()
    connection.close()
except Exception as err:
    if 'connection' in locals() and connection.is_connected():
        connection.rollback()
        connection.close()
    print("Error is ", err)
PERSON=''