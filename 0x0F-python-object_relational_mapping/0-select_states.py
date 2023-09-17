#!/usr/bin/python3

"""
module to list all states from the
database "hbtn_0e_0_usa".
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    connect to the database
    """
    db_con = MySQLdb.connect(
        host = "localhost", 
        username=argv[1],
        port = 3306,
        password = argv[2],
        db_name = argv[3])

    db_cursor = db_con.cursor()

    db_cursor.execute("SELECT * FROM states")

    rows_sel = db_cursor.fetchall()

    for row in rows_sel:
        print(row)
