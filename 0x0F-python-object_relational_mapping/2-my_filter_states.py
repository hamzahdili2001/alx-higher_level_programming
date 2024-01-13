#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

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
    query = """
    SELECT * FROM states
    WHERE BINARY `name`='{query}'
    ORDER BY id ASC
    """
    cur.execute(query.format(query=sys.argv[4]))
    result = cur.fetchall()

    for i in result:
        print(i)

    cur.close()
    c.close()
