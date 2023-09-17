#!/usr/bin/python3

"""
A module to list all City objects from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    """ A module to initialize the class cities

    """
    username: str = sys.argv[1]
    password: str = sys.argv[2]
    db_name: str = sys.argv[3]
    host: str = "localhost"
    port: int = 3306

    Session = sessionmaker()
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@{host}:{port}/{db_name}",
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)
    session = Session()

    if cities := session.query(City).order_by(City.id):
        for city in cities:
            print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()
