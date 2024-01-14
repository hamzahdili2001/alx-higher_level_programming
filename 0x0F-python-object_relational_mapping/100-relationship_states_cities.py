#!/usr/bin/python3
"""script that creates the State “California”with the City
“San Francisco” from the database hbtn_0e_100_usa:
(100-relationship_states_cities.py)"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State("California")
    new_city = City("San Fransisco")
    new_city.state = new_state
    session.add_all([new_state, new_city])
    session.commit()
    session.close()
