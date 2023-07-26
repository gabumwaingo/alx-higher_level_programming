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
    c.execute("""SELECT `c`.`name`
                FROM cities as `c`
                INNER JOIN states as `s`
                ON `c`.`state_id` = `s`.`id`
                WHERE `s`.`name` = %s
                ORDER by `c`.`id`""", (state,))
    cities = c.fetchall()
    city_names = [city[0] for city in cities]
    output = ', '.join(city_names)
    print(output)
    c.close()
    db.close()
