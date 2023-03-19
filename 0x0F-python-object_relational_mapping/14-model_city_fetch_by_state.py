#!/usr/bin/python3
"""This script prints out the content of the hbtn_0e_14_usa db"""

from model_state import Base, State
from sys import argv
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: <username> <password> <dbName>")
    else:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                               format(argv[1], argv[2], argv[3]),
                               pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        st_cty = session.query(State, City).\
            filter(State.id == City.state_id).all()
        for state, city in st_cty:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
