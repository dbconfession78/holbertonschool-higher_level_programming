#!/usr/bin/python3
"""
add's the State object 'Lousiana' to the db
"""
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

    new_state = State(name="Louisiana")
    session.add_all([new_state])
    session.commit()
    states = session.query(State)
    for state in states:
        print("{}: {}".format(state.id, state.name))

if __name__ == "__main__":
    main()
