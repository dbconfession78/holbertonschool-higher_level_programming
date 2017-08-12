#!/usr/bin/python3
# prints all 'City' objects from selected db


def main():
    """
    entry point for model_city_fetch_by_state script
    """
    from sys import argv
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    user = argv[1]
    passwd = argv[2]
    db_name = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        user, passwd, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City).join(City).order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))

if __name__ == "__main__":
    main()
