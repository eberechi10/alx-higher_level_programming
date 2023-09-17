#!/usr/bin/python3

"""
  a module to List all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """ initialize list of states

    """
    username: str = sys.argv[1]
    password: str = sys.argv[2]
    db_name: str = sys.argv[3]
    host: str = "localhost"
    port: int = 3306
    statement: str = """SELECT * FROM states ORDER BY id"""

    db = MySQLdb.connect(
        user=username,
        host=host,
        port=port,
        password=password,
        database=db_name,
    )
    cursor = db.cursor()

    cursor.execute(statement)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
