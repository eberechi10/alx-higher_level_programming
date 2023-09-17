#!/usr/bin/python3

"""
A module that List all states from the database
hbtn_0e_0_usa where name is the same

"""
import sys
import MySQLdb

if __name__ == "__main__":
    """ A module to initialize state class
    """
    username: str = sys.argv[1]
    password: str = sys.argv[2]
    db_name: str = sys.argv[3]
    arg: str = sys.argv[4]
    host: str = "localhost"
    port: int = 3306

    command: str = """
    SELECT *
    FROM states
    WHERE BINARY name = '{}'
    ORDER BY id
    """.format(arg)

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
