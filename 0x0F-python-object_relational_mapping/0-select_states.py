#!/usr/bin/python3
"""This module list all states from the sql database"""
import sys
import MySQLdb
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: <module> <username> <password> <database name>")
    else:
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        cursor = db.cursor()
        cursor.execute("SELECT * from `states`")
        for state in cursor.fetchall():
            print(state)
        cursor.close()
        db.close()
