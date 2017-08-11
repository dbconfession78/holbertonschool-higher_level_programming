#!/usr/bin/python3
""" injection-safe script that takes an state name as arg and lists
all cities of that state  """


def main():
    import MySQLdb
    import sys

    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_arg = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=passwd,
        db=db_name)

    cur = db.cursor()
    cur.execute(
        "SELECT name FROM cities  \
        WHERE state_id IN \
        (SELECT id FROM states \
        WHERE name LIKE \
        BINARY '{:s}')".format(state_arg))
    cities = cur.fetchall()
    print(", ".join(city[0] for city in cities))


if __name__ == "__main__":
    main()
