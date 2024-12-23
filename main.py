from DBMusic import DBMusic

db_manager = DBMusic("music.db")
db_manager.create_tables()

"""db_manager.add_music(2,
                    "музика",
                    "деякя інфа")"""
print(db_manager.get_music())