#!/usr/bin/python3
"""
A script that changes the name of a State
object from the database hbtn_0e_6_usa
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

    state = session.query(State).filter_by(id=2).first()
    state.name = 'New Mexico'
    session.commit()
    session.close()
