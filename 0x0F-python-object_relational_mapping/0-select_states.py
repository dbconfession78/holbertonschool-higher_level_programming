#!/usr/bin/env python3
""" lists all the states from the db hbtn_0e_0_usa """


if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=passwd,
        db=db_name)

    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY states.id ASC""")

    line = cur.fetchone()
    while (line):
        print(line)
        line = cur.fetchone()
