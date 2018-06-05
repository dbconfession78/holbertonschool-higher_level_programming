#!/usr/bin/env python3
import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="Hyrenkosa1",
    db="test_db_1")

cur = db.cursor()

songs = ["Purple Haze", "All Along the Watch Tower", "Foxy Lady"]
for song in songs:
    cur.execute("INSERT INTO song (title) VALUES (\"{}\")".format(song))
    print("Auto Increment ID: {}".format(cur.lastrowid))

db.commit()

cur.execute("SELECT * FROM song WHERE id = {} or id = {}".format(1, 2))

numrows = cur.execute("SELECT * FROM song")
print("selected rows: {}".format(numrows))
print("select rows: {}".format(cur.rowcount))

cur.close()
db.close()
