#!/usr/bin/python3
"""Lists all states"""

import MySQLdb
import sys

def list_states(username, password, db_name):
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query to select all states
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the query
    states = cur.fetchall()

    # Print the states
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
