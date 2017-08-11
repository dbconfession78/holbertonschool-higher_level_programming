#!/usr/bin/python3
""" injection-safe script that takes an argument and displays
all values in the states table of selected db """


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
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s \
    ORDER BY id ASC",  (state_arg, ))
    state = cur.fetchone()
    while (state):
        print(state)
        state = cur.fetchone()

if __name__ == "__main__":
    main()
