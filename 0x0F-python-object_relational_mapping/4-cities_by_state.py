#!/usr/bin/python3

"""
A module to Lists all cities and their states
from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """ A module to initialize class

    """
    username: str = sys.argv[1]
    password: str = sys.argv[2]
    db_name: str = sys.argv[3]
    host: str = "localhost"
    port: int = 3306

    command: str = """
    SELECT c.id, c.name, s.name
    FROM cities AS c
    JOIN states AS s
    ON c.state_id = s.id
    ORDER BY c.id;
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
