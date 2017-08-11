#!/usr/bin/python3
"""
prints the first State objcet from the selected db
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

    f_state = session.query(State.id, State.name).first()
    if (f_state is None):
        print("Nothing")
    else:
        print("{:d}: {:s}".format(f_state[0], f_state[1]))

if __name__ == "__main__":
    main()
