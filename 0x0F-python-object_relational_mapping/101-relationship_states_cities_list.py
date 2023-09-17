#!/usr/bin/python3

"""
A module to list all State objects, and their City objects,
from database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
     """ a module to initializ
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

    if states := session.query(State).order_by(State.id):
        for state in states:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"    {city.id}: {city.name}")

    session.close()
