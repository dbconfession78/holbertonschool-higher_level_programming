#!/usr/bin/python3
""" lists all states starting with 'N' from the selected db"""


def main():
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
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    n_state = cur.fetchone()
    while(n_state):
        print(n_state)
        n_state = cur.fetchone()

if __name__ == "__main__":
    main()
