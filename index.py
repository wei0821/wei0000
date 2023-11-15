from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    X = "作者:林威呈<br>"
    X += "<a href=/about>我的個人簡介</a><br>"
    X += "<a href=/today>職涯測驗結果</a><br>"
    X += "<a href=/account>MIS相關工作介紹</a><br>"
    return X

@app.route("/about")
def course():
    return render_template("about.html")
    
app.route("/today")
def about():
    return render_template("today.html")

@app.route("/account")
def today():
    return render_template("account.html")

@
if __name__ == "__main__":
	app.run()