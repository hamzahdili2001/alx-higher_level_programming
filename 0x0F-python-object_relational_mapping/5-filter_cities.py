#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""


import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    c = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db,
        charset="utf8",
    )

    cur = c.cursor()
    query = """SELECT name FROM cities
        WHERE state_id = ( SELECT id FROM states WHERE name = %s);"""
    cur.execute(query, (sys.argv[4],))
    result = cur.fetchall()

    for i, s in enumerate(result):
        if i:
            print(", ", end="")
        print(s[0], end="")
    print()

    cur.close()
    c.close()
