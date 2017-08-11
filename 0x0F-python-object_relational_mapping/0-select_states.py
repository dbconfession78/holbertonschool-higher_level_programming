#!/usr/bin/env python3
# lists all the states from the db hbtn_0e_0_usa
import MySQLdb
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user="{}".format(username),
        password="{}".format(password),
        db="{}".format(db_name))

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    line = cur.fetchone()
    while (line):
        print(line)
        line = cur.fetchone()
#    states = cur.fetchall()
#     for (i, state) in enumerate(states):

if __name__ == "__main__":
    main()
