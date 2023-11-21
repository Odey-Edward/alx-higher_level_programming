#!/usr/bin/python3
"""
a script that creates the State “California” with
the City “San Francisco” from the database
"""
from sqlalchemy import create_engine
from sys import argv
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy.orm import sessionmaker

conn = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(argv[1], argv[2], argv[3], pool_pre_ping=True)
)

Base.metadata.create_all(conn)
Session = sessionmaker(bind=conn)
session = Session()

stateObj = State(name='California')
cityObj = City(name='San Francisco', state=stateObj)

session.add(stateObj)
session.add(cityObj)
session.commit()

session.close()
