import sqlite3

connection = sqlite3.connect("bob.sl3", 5)

cur = connection.cursor()
# cur.execute("CREATE TABLE first_table (name TEXT);")
# cur.execute("INSERT INTO first_table (name) VALUES ('Sasha');")
# cur.execute("INSERT INTO first_table (name) VALUES ('Anna');")
# cur.execute("INSERT INTO first_table (name) VALUES ('Kate');")
# connection.commit()
# cur.execute("DELETE FROM first_table WHERE rowid=3")
# connection.commit()
# cur.execute("SELECT rowid, name FROM first_table")
# connection.commit()
# res = cur.fetchall()
# print(res)
cur.execute("DROP TABLE first_table")
connection.commit()
connection.close()
