#!/usr/bin/python3
"""
a script that deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    conn = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3])
            )
    Base.metadata.create_all(conn)
    session_maker = sessionmaker(bind=conn)
    session = session_maker()

    for state in session.query(State).all():
        if 'a' in state.name:
            session.delete(state)

    session.commit()
    session.close()
