#!/usr/bin/python3
"""
A module that creates State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""


import sys

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username: str = sys.argv[1]
    password: str = sys.argv[2]
    db_name: str = sys.argv[3]
    host: str = "localhost"
    port: int = 3306

    Session = sessionmaker()
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@{host}/{db_name}',
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)
    session = Session()

    c_state = State(name='California')
    sf_city = City(name='San Francisco', state=c_state)
    c_state.cities.append(sf_city)

    session.add(c_state)
    session.commit()
    session.close()
