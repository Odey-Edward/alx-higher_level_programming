#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa

Usage: ./4-cities_by_state.py <mysql username>
                            <mysql password>
                            <database name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""
    SELECT * FROM cities
    ORDER BY cities.id ASC
    """)

    for state in cur.fetchall():
        print(state)

    cur.close()
    db.close()
