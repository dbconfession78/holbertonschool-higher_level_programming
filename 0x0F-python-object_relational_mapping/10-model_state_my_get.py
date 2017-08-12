#!/usr/bin/python3
"""
prints the state's id
"""
import MySQLdb
from sys import argv, exit
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


def main():
    username = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    state_arg = argv[4]

    if (len(argv) != 5):
        print("USAGE: ./10-model_state_my_get.py <username> <password> \
        <database name>")
        exit(1)

    try:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                               format(username, passwd, db_name))
    except Exception as e:
        print(e)
        exit(1)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = session.query(State).filter(State.name == state_arg).one()
        print("{:d}".format(state.id))
    else:
        print("Not Found")
    session.close()

if __name__ == "__main__":
    main()
