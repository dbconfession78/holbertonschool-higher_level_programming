#!/usr/bin/python3
"""
deletes all State objects w. a name containing the letter 'a' from selected db
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
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%'))
    for state in states:
        session.delete(state)
    session.commit()
    states = session.query(State)
    session.close()

if __name__ == "__main__":
    main()
