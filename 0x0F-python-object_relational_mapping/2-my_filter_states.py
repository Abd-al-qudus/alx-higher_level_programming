#!/usr/bin/python3
"""This module list all states from the sql database and
    prints out the states that matches the searched state"""
import sys
import MySQLdb
if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: <module> <username> <password> <database name> <search>")
    else:
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        cursor = db.cursor()
        cursor.execute("SELECT * from `states` WHERE name LIKE '{:s}' ORDER BY id ASC".format(sys.argv[4]))
        for state in cursor.fetchall():
            print(state)
        cursor.close()
        db.close()
