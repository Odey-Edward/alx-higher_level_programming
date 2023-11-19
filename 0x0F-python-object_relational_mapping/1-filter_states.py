#!/usr/bin/python3
"""
A script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa

Usage: ./1-filter_states.py <mysql username>
                            <mysql password>
                            <database name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""
    SELECT * FROM states
    WHERE name LIKE 'N%'
    ORDER BY id
    """)

    for state in cur.fetchall():
        print(state)

    cur.close()
    db.close()
