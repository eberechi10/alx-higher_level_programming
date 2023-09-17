#!/usr/bin/python3
"""
Module to list all cities.
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

"""
initialize database, get the states
"""
if __name__ == '__main__':
    db_con = db.connect(host="localhost", port=3306,
                            username=argv[1], password=argv[2], db=argv[3])
    db_cursor = db_con.cursor()

    db_cursor.execute(
        "SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")

    rows_sel = db_cursor.fetchall()

    for row in rows_sel:
        print(row)
