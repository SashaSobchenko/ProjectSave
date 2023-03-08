import sqlite3

connection = sqlite3.connect("tablsa.sl3", 5)

cur = connection.cursor()
#cur.execute("CREATE TABLE first_table (name TEXT);")
cur.execute("INSERT INTO first_table (name) VALUES ('https://ru.wikipedia.org/wiki/%D0%92%D1%82%D0%BE%D1%80%D0%B0%D1%8F_%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%8F_%D0%B2%D0%BE%D0%B9%D0%BD%D0%B0');")
cur.execute("INSERT INTO first_table (name) VALUES ('https://ru.wikipedia.org/wiki/%D0%9A%D0%B8%D0%B5%D0%B2');")
cur.execute("INSERT INTO first_table (name) VALUES ('https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D0%B2%D0%B0%D1%8F_%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%8F_%D0%B2%D0%BE%D0%B9%D0%BD%D0%B0');")
connection.commit()
#cur.execute("DELETE FROM first_table WHERE rowid=4")
#connection.commit()
#cur.execute("SELECT rowid, name FROM first_table")
#connection.commit()
res = cur.fetchall()
print(res)
#cur.execute("DROP TABLE first_table")
#connection.commit()
#connection.close()
