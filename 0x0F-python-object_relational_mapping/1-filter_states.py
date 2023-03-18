#!/usr/bin/python3
"""This module list all states from the sql database and
    prints out the states starting with N"""
import sys
import MySQLdb
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: <module> <username> <password> <database name>")
    else:
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        cursor = db.cursor()
        cursor.execute("SELECT * from `states` ORDER BY id")
        s_table = [state for state in cursor.fetchall() if state[1].startswith('N')]
        for states in s_table:
            print(states)
        cursor.close()
        db.close()
