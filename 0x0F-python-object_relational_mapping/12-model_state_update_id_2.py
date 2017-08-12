#!/usr/bin/python3
"""
changes the name of a State object from the selected db
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

    state = session.query(State).filter_by(id=2)[0]
    state.name = "New Mexico"
    session.commit()


if __name__ == "__main__":
    main()
