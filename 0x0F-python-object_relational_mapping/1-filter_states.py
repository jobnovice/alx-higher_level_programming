#!/usr/bin/python3
"""lists all states that start with the letter N"""

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: <username> <password> <database name>")
        exit(1)

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%'\
                 ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
