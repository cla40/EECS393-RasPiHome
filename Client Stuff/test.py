import sqlite3

createDB = sqlite3.connect("myDatabase")

query = createDB.cursor()
query.execute('SELECT SQLITE_VERSION() ')
data = query.fetchone()
print "SQLite version: %s" % data 
#print(query.fecthone())
query.execute("SELECT name FROM sqlite_master WHERE type='table';")
#print(query.fecthone())
data = query.fetchall()
print "TABLES: %s" % data
bID = 1
building = query.execute('SELECT * FROM piServer_building WHERE id = %s' % bID)
data = query.fetchall()
print "Building: %s" % data
