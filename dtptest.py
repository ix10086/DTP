import sqlite3

DATABASE = 'cpu.db'

with sqlite3.connect(DATABASE) as db:
    cursor = db.cursor()
    sql = 'SELECT * FROM cpu,'
    cursor.execute(sql)
    results = cursor.fetchall()