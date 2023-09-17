#!/usr/bin/python3
"""
Module to filter all states starting with N.
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

"""
initialize database, get the states
"""

if __name__ == '__main__':
    db_con = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_con.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    rows_sel = db_cursor.fetchall()

    for row in rows_sel:
        print(row)
