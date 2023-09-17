#!/usr/bin/python3
"""
Module to filter all states where it matches.
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
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    rows_sel = db_cursor.fetchall()

    for row in rows_sel:
        print(row)
