import mysql.connector

try:
    # Connect to MySQL database
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="hvc_college")
    cursor = connection.cursor()

    # Step 1: Add the new column 'id' to the table (added at the end by default)
    # add_column_query = "ALTER TABLE bca ADD COLUMN email VARCHAR(100)"
    # cursor.execute(add_column_query)

    # Step 2: Modify column order to position 'id' before 'fname'
    cursor.execute("ALTER TABLE bca ADD COLUMN ID INT(6)")

    modify_column_order_query = "ALTER TABLE bca MODIFY COLUMN ID INT(10) AFTER ROLL"
    cursor.execute(modify_column_order_query)
    modify_column_order_query = "ALTER TABLE bca MODIFY COLUMN ROLL INT(10) AFTER ID"
    cursor.execute(modify_column_order_query)


    # Commit the changes
    connection.commit()

    # Close the connection
    connection.close()

    print("Column 'id' added and positioned before 'fname' successfully")

except mysql.connector.Error as err:
    print("Error:", err)
