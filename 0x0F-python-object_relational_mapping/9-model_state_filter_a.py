#!/usr/bin/python3
"""
prints all states that contain a lowercase 'a'
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

    engine = create_engine("mysql://{}:{}@localhost/{}".format(
        username, passwd, db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    a_states = session.query(State.id, State.name).filter(
        State.name.like("%a%"))

    for state in a_states:
        print("{}: {}".format(state[0], state[1]))

if __name__ == "__main__":
    main()
