from flask import *

from DBMusic import DBMusic

app = Flask("Music")
database = [
    (0,"Daylight", "Ця пісня була популярна в 2023р ", "Виконавець пісні David Kushner, Rob Kirvan, Rick Hornby, Hayden Robert Hubers","Понад 367 276 920 переглядів", "пісня",  )
]


