#!/usr/bin/python3
"""task 5"""
if __name__ == '__main__':
    import MySQLdb
    import sys
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name LIKE BINARY %s \
            ORDER BY cities.id ASC", [sys.argv[4]])
    rows = cur.fetchall()

    flag = 0
    for row in rows:
        if flag != 0:
            print(", ", end="")
        print(row[0], end="")
        flag = 1
    print()
