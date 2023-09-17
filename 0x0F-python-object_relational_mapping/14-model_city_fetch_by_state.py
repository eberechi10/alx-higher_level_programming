#!/usr/bin/python3
"""
A module to prints all Cities and states from the database hbtn_0e_14_usa.
"""

import sys

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base
from model_city import City

if __name__ == "__main__":
    """ initialize the cities and state for access

    """
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

    if cities := session.query(City).order_by(City.id):
        for city in cities:
            print(f'{city.state.name}: ({city.id}) {city.name}')
