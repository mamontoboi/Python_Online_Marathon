# Create a Python program to use the sqlite database named "q1.db".
# The query to the database should display information,
# as shown in the example below, including phrases: about the successful connection, the total number of records,
# the actual records, the record of closing the database. From the table of "customers" to deduce all records for
# which in a "grade" field of value more than 200 with sort ordering on id
#
# For example output:
#
# Connected to SQLite
# Total rows are:   2
# Printing each row
# Id:  3022
# Name:  Nik Rimando
# City:  Madrid
# Grade:  1000
# Seller:  6001
#
# Id:  3025
# Name:  Grem Zusisa
# City:  USA
# Grade:  2000
# Seller:  6002
#
# The SQLite connection is closed

import sqlite3

try:
    sql_connection = sqlite3.connect("q1.db")
    sql_cursor = sql_connection.cursor()
    print("Connected to SQLite")
    sql_query_count_all = """SELECT COUNT(*) FROM customers WHERE grade > 200;"""
    sql_cursor.execute(sql_query_count_all)
    num = sql_cursor.fetchone()
    print(f"Total rows are:   {num[0]}")

    sql_query_all = """SELECT * FROM customers WHERE grade > 200 ORDER BY id;"""
    sql_cursor.execute(sql_query_all)
    lst = sql_cursor.fetchall()
    print("Printing each row")
    for line in lst:
        print(f"Id:  {line[0]}\nName:  {line[1]}\nCity:  {line[2]}\nGrade:  {line[3]}\nSeller:  {line[4]}\n\n")

except sqlite3.Error as e:
    print(f"The following error has occurred: {e}")

finally:
    if sql_connection:
        print("The SQLite connection is closed")
        sql_connection.close()
