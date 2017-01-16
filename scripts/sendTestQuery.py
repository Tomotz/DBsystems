import MySQLdb as mdb
DB_QUERY = "SELECT * FROM Addresses"


def connectToDB():
	db = mdb.connect("127.0.0.1", "DbMysql17", "DbMysql17", "DbMysql17", port=19821)
	with db:
		cur = db.cursor()
		cur.execute(DB_QUERY)

if __name__ == "__main__":
	connectToDB()