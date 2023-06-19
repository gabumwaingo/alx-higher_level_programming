#!/usr/bin/python3
# lists all staes starting with letter N in ascending order

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cs = db.cursor()
    cs.execute("SELECT * FROM `states` WHERE name LIKE 'N%' ORDER BY id ASC")
    states = cs.fetchall()
    for state in states:
        print(state)

    cs.close()
    db.close()
