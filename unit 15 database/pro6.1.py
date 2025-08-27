import mysql.connector

try:
    # Connect to MySQL database
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="amazon2")
    cursor = connection.cursor()

    # Corrected SQL query
    m_column_query = "ALTER TABLE products MODIFY COLUMN ID INT(6) BEFORE category"

    cursor.execute(m_column_query)

    # Commit the changes
    connection.commit()

    # Close the connection
    connection.close()

    print("Column 'ID' added and positioned before 'category' successfully")

except mysql.connector.Error as err:
    print("Error:", err)
