import sqlite3


class DB_Connect:
    def __init__(self, db_name: str):
        self.con = sqlite3.connect(db_name)

    def close(self):
        self.con.close()
