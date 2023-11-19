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
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states
    ON states.id = cities.state_id
    ORDER BY cities.id ASC
    """)

    for city in cur.fetchall():
        print(city)

    cur.close()
    db.close()
