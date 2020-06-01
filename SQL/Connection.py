import mysql.connector

connection = mysql.connector.connect(host='localhost', database='foofle_proj', user='root', password='kimiya')
if connection.is_connected():
    global cursor
    cursor = connection.cursor()
    record = cursor.fetchone()
    connection.commit()
