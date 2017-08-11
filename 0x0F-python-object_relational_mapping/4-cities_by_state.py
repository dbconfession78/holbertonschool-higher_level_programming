#!/usr/bin/python3
""" lists all cities from the selected db  """


def main():
    import MySQLdb
    import sys

    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
#    state_arg = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=passwd,
        db=db_name)

    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name \
        FROM cities \
        JOIN states ON cities.state_id = states.id \
        ORDER BY cities.id ASC")

    city = cur.fetchone()
    while (city):
        print(city)
        city = cur.fetchone()

if __name__ == "__main__":
    main()
