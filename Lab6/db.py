import MySQLdb

db = MySQLdb.connect(
    host='localhost',
    user='dbuser',
    passwd='123',
    db='first',
    charset = 'utf8',
    use_unicode = True
);

c = db.cursor()
c.execute("INSERT INTO tovar (name, `desc`, cout) values ('Samsung note 7', 'Взрывная мощ', 45000.00)")
db.commit()

c.execute("SELECT * FROM tovar")

entries = c.fetchall()

for e in entries:
    print(e)

c.close()
db.close()
