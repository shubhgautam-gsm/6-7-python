import mysql.connector

try:
    # create connection and cursor objects
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="hvc_college")
    cursor = connection.cursor()

    # build a query
    query = "select * from bca"

    # execute query
    cursor.execute(query)

    # get result from executed cursor
    result = cursor.fetchall()
    #result=[(),(),()]
    #result = [( "majiv sheikh", "rajkot",7066947730)
    #         ,( "kajiv sheikh", "aajkot",7066947860),
    #         ( "sajiv sheikh", "najkot",7066947837)]
    
    #  row=[] overide   a=5 a=6 a=7  
     
    # run loop on result and print all the data
    for row in result:
        print(row)

    connection.commit()
    connection.close()
except Exception as err:
    connection.rollback()
    print("Error is ",err)
