import MySQLdb as mdb
DB_QUERY = "SELECT * FROM Addr"


def connectToDB():
	db = mdb.connect("127.0.0.1", "root", "Ru30299008012061989", "DbMysql17", port=3306)
	with db:
		cur = db.cursor()
		cur.execute(DB_QUERY)
		print(cur.fetchone())

if __name__ == "__main__":
	connectToDB()