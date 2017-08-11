#!/usr/bin/python3
""" lists all the states from the db hbtn_0e_0_usa """


def main():
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="{}".format(username),
        password="{}".format(password),
        db="{}".format(db_name))

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    line = cur.fetchone()
    while (line):
        print(line)
        line = cur.fetchone()

if __name__ == "__main__":
    main()
