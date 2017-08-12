#!/usr/bin/python3
"""
prints the state's id
"""
import MySQLdb
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


def main():
    username = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    state_arg = argv[4]

    engine = create_engine("mysql://{}:{}@localhost/{}".format(
        username, passwd, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State.id).filter(
         State.name == state_arg)
    if state.first() is None:
        print("Not found")
    else:
        print(state[0].id)

if __name__ == "__main__":
    main()
