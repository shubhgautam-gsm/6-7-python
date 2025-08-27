import mysql.connector

try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="hvc_college")
    connection.autocommit = True
    myCursor = connection.cursor()

    query = "INSERT INTO bca (Name,City,Contact) VALUES ( %s, %s,%s)"
    data = [( "majiv sheikh", "rajkot",7066947730)
            ,( "kajiv sheikh", "aajkot",7066947860),
            ( "sajiv sheikh", "najkot",7066947837)]

    myCursor.executemany(query, data)
    print(myCursor.rowcount, "New Record(s) Created")

    # Retrieve the last inserted row ID (lastrowid)
    last_row_id = myCursor.lastrowid
    if last_row_id is not None:
        print("Last Inserted Row ID:", last_row_id)

    connection.commit()
    connection.close()

except mysql.connector.Error as err:
    print("Error:", err)
