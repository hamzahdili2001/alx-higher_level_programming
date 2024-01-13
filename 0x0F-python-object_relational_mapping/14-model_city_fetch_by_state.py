#!/usr/bin/python3
""" Python file similar to model_state.py
named model_city.py that contains the class definition of a City."""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    state_cities = (
        session.query(City.id, City.name, State.name)
        .join(State)
        .order_by(City.id)
    )
    for state_city in state_cities:
        print(f"{state_city[2]}: ({state_city[0]})", state_city[1])
