#!/usr/bin/python3
"""This script works like 7-fetch_all except that
    if only returns the first state"""

from model_state import Base, State
from sys import argv
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
        first = session.query(State).order_by(State.id).first()
        if first is not None:
            print(f"{first.id}: {first.name}")
        else:
            print("Nothing")
