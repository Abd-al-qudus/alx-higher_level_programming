#!/usr/bin/python3
"""This script add a name to the city db"""
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
            row = State(name="Louisiana")
            session.add(row)
            session.commit()
            print(row.id)
        except SQLAlchemyError as e:
            print(e)
        finally:
            session.close()
