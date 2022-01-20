import sqlite3 as lite
import sys
con = lite.connect('dogs.db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS feeding")
    cur.execute("CREATE TABLE feeding(timestamp DATETIME, name TEXT, grams NUMERIC)")