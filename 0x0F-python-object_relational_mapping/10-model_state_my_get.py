#!/usr/bin/python3
"""
prints the state's id
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    username = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    state_arg = argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(username, passwd, db_name))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = session.query(State).filter(State.name == state_arg).one()
        print("{}".format(state.id))
    except:
        print("Not found")
    session.close()

if __name__ == "__main__":
    main()
