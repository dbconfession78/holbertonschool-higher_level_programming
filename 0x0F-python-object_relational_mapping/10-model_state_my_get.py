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

    engine = create_engine("mysql://{}:{}@localhost:3306/{}".format(
        username, passwd, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State.id).filter_by(name=state_arg)
    if query.first() is None:
        print("Not Found")
    else:
        print("{:d}".format(query[0].id))
    session.close()


if __name__ == "__main__":
    main()
