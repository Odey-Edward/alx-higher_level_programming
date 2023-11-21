#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    conn = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]),
            pool_pre_ping=True
            )

    session_maker = sessionmaker(bind=conn)
    session = session_maker()

    for city, state in session.query(City, State).\
        filter(State.id == City.state_id).\
            order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
