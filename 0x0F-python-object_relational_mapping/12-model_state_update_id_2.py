#!/usr/bin/python3
"""This script changes a name id to 2 in the db"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.exc import SQLAlchemyError

if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: <username> <password> <dbName>")
    else:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                               format(argv[1], argv[2], argv[3]),
                               pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            filters = session.query(State).filter(State.id == 2).first()
            filters.name = "New Mexico"
            session.commit()
        except SQLAlchemyError as e:
            print(e)
