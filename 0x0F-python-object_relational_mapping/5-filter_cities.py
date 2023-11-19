#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa

Usage: ./5-filter_cities.py<mysql username>
                            <mysql password>
                            <database name>
                            <state name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""
    SELECT cities.name, states.name
    FROM cities
    JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """)

    p = ", "\
        .join([city[0] for city in cur.fetchall() if city[1] == sys.argv[4]])
    print(p)

    cur.close()
    db.close()
