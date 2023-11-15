from flask import Flask, render_template
from datetime import datetime
from waitress import serve

app = Flask(__name__)

@app.route("/")
def index():
    X = "作者:黃俊翔<br>"
    X += "<a href=/mis>資管導論</a><br>"
    X += "<a href=/today>日期時間</a><br>"
    X += "<a href=/about>子青網頁</a><br>"
    return X

@app.route("/mis")
def course():
	return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html", datetime = str(now))

@app.route("/about")
def about():
    now = datetime.now()
    return render_template("about.html")

if __name__ == "__main__":
	#app.run()
    serve(app, host='0.0.0.0', port=80)