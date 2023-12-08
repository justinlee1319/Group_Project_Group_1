from flask import Flask, render_template
import sqlite3
import pathlib

base_path = pathlib.Path().cwd()
db_name = "twitch_data.db"
db_path= base_path /'database'/ db_name


app = Flask(__name__)

@app.route("/")
def index():
    return render_template ("index_fillin.html")

@app.route("/about")
def about():
    return render_template ("about.html")

@app.route("/data")
def data():
    con=sqlite3.connect(db_path)
    cursor=con.cursor()
    twitch_data=cursor.execute(" select * from twitch_data " ).fetchmany(10)
    con.close()
    return render_template ("data_table_fillin.html", twitch_data=twitch_data)

if __name__== "__main__":
    app.run(debug=True)

