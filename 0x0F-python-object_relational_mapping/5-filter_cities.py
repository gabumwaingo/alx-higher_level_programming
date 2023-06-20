#!/usr/bin/python3
""" lists all the cities of a state argument from the stdin. """

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
    state = sys.argv[4]
    c.execute("""SELECT *
                FROM cities as `c`
                INNER JOIN states as `s`
                ON `c`.`state_id` = `s`.`id`
                WHERE `s`.`name` = %s
                ORDER by `c`.`id`""", (state,))
    cities = c.fetchall()
    for city in cities:
        print(city)
    c.close()
    db.close()
