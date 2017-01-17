from tauwebsite.tauwebsite.settings import LOCAL_DB_PASS
import MySQLdb as mdb


class DBUtils:
    db = mdb.connect("127.0.0.1", "root", LOCAL_DB_PASS, "DbMysql17", port=3306)

    @classmethod
    def get_user_by_uname(cls, username):
        with cls.db as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Users WHERE user_name=%s" % username)
            row = cursor.fetchone()

        return row