#!/usr/bin/python3
"""
A script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    conn = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]),
            pool_pre_ping=True
            )

    Session = sessionmaker(bind=conn)
    session = Session()

    state = session.query(State).filter_by(name=argv[4]).\
        order_by(State.id).first()

    if state is None:
        print('Not found')
    else:
        print("{}".format(state.id))

    session.close()
