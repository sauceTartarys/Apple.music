import sqlite3


class DBMusic:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)