#!/usr/bin/python3

"""
A module to list all states from the database hbtn_0e_0_usa
where name starting with `N`
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """ a module that initailize the class

    """
    username: str = sys.argv[1]
    password: str = sys.argv[2]
    db_name: str = sys.argv[3]
    host: str = "localhost"
    port: int = 3306

    command: str = """
    SELECT *
    FROM states
    WHERE BINARY name LIKE 'N%'
    ORDER BY id
    """

    db = MySQLdb.connect(
        user=username,
        host=host,
        port=port,
        password=password,
        database=db_name,
    )
    cursor = db.cursor()

    cursor.execute(command)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
