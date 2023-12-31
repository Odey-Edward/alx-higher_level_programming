#!/usr/bin/python3
"""
a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
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

    session_maker = sessionmaker(bind=conn)
    session = session_maker()

    obj = State(name="Louisiana")
    session.add(obj)
    session.commit()

    print(obj.id)

    session.close()
