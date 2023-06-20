#!/usr/bin/python3
""" lists all the cities in the datbase """


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            host="localhost",
            port=3306)
    c = db.cursor()
    c.execute("""SELECT `c`.`id`, `c`.`name`, `s`.`name`
                FROM `cities` as `c`
                INNER JOIN states as `s`
                ON `c`.`state_id` = `s`.`id`
                ORDER by `c`.`id`""")
    cities = c.fetchall()
    for city in cities:
        print(city)
    c.close()
    db.close()
