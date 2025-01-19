from flask import *

from DBMusic import DBMusic

app = Flask("Music")
db_name = "music.db"
database = [
    (0,"We are the danger", "Цей рок для любителів", "Jay Maroni, Voelker Bros",1517737,'пісня','https://www.youtube.com/watch?v=Ze9UBqiha9g',"maxresdefault.jpg"),
    (0,"Daylight", "Цей рок був популярний в 2023р ", "гурт пісні: David Kushner, Rob Kirvan, Rick Hornby, Hayden Robert Hubers", 367276920, "пісня","https://www.youtube.com/watch?v=MoN9ql6Yymw","maxresdefault.jpg")
]


@app.route("/")
def index():
    db_manager = DBMusic(db_name)
    return render_template("index.html",musicals=database)

@app.route("/pop2025")
def mamoder():
    db_manager = DBMusic(db_name)
    return render_template("2025.html",musicals=database)

@app.route("/fongers")
def kerp():
    db_manager = DBMusic(db_name)
    return render_template("fonk.html",musicals=database)


app.run(port=8002)