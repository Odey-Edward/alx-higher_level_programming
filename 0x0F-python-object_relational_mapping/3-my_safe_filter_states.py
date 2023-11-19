#!/usr/bin/python3
"""
A script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
safe from MySQL injections!

Usage: ./2-filter_states.py <mysql username>
                            <mysql password>
                            <database name>
                            <state name searched>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""
    SELECT * FROM states
    ORDER BY id ASC
    """)

    for state in cur.fetchall():
        if state[1] == sys.argv[4]:
            print(state)

    cur.close()
    db.close()
