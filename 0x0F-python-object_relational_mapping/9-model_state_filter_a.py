#!/usr/bin/python3
"""This script works like 8 except that it
    returns the queries where the state contains a"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State

if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: <username> <password> <dbName>")
    else:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                               format(argv[1], argv[2], argv[3]),
                               pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        states = session.query(State).order_by(State.id). \
            filter(State.name.contains("a"))
        for state in states:
            print(f"{state.id}: {state.name}")
