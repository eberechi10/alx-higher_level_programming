#!/usr/bin/python3
"""
Module to list all `cities` in the `cities` table``.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    state_name = sys.argv[4]

    db = MySQLdb.connect(username, password, db=db_name)
    cursor = db.cursor()

    cursor.execute("SELECT c.name \
                 FROM cities c INNER JOIN states s \
                 ON c.state_id = s.id WHERE s.name = %s\
                 ORDER BY c.id", (state_name, ))
    rows_sel = cursor.fetchall()

    for idx in range(len(rows_sel)):
        print(rows_sel[idx][0], end=", " if idx + 1 < len(rows_sel) else "")
    print("")
