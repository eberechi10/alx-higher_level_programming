#!/usr/bin/python3
"""
A module to list all states from the database hbtn_0e_0_usa
where name matches an argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """ A module to initialize the class

    """
    username: str = sys.argv[1]
    password: str = sys.argv[2]
    db_name: str = sys.argv[3]
    arg: str = sys.argv[4]
    host: str = "localhost"
    port: int = 3306

    command: str = """
    SELECT * FROM states
    WHERE BINARY name = %s
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

    cursor.execute(command, (arg,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
