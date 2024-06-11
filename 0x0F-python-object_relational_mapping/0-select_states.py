#!/usr/bin/python3
"""Get all the states inside from a given database"""
from MySQLdb import _mysql
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: <username> <password> <database name>")
        exit(1)

    db = _mysql.connect(host="localhost", port=3306, user="{}",
                        password="{}", database="{}"
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    db.query("""select id, name from states""")
    r = db.store_result()
    r.fetch_row()
