import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL connection details from command-line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # Execute the query to retrieve states
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows from the result set
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

