#!/usr/bin/python3
"""This script list the states in the database using sqlalchemy"""

from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: <username> <password> <dbName>")
    else:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                               format(argv[1], argv[2], argv[3]),
                               pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        for state in session.query(State).order_by(State.id):
            print(f"{state.id}: {state.name}")
