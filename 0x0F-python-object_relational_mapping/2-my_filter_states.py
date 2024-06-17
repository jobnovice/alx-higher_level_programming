#!/usr/bin/python3
"""prints a particular state that matches the given name"""


import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: <user name> <password> <database name> <state name>")
        exit(1)
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE {}\
                ORDER BY id ASC".format(sys.argv[4]))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
