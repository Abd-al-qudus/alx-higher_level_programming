#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities \
        JOIN states ON cities.state_id = states.id \
        WHERE states.name LIKE %s ORDER BY cities.id ASC"
    search = sys.argv[4]
    cursor.execute(query, [search])
    for row in cursor.fetchall():
        print(f"{row}")
    db.close()
