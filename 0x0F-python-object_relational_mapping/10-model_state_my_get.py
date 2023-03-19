#!/usr/bin/python3
"""This script works like 9 except that it returns
    the query where the state contains a searched name"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State

if __name__ == '__main__':
    if len(argv) != 5:
        print("Usage: <username> <password> <dbName> <search>")
    else:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                               format(argv[1], argv[2], argv[3]),
                               pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        search = session.query(State).order_by(State.id). \
            filter(State.name == argv[4])
        found = False
        for state in search:
            if state.name == argv[4]:
                print(f"{state.id}")
                found = True
        if not found:
            print("Not found")
