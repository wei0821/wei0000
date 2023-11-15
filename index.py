from flask import Flask, render_template

app = Flask(name)

@app.route("/")
def index():
    X = "作者:資管二A 林威呈<br>"
    X += "<a href=/about>我的個人簡介</a><br>"
    X += "<a href=/account>MIS相關工介紹</a><br>"
    X += "<a href=/today>職涯測驗結果</a><br>"
    return X

@app.route("/about")
def course():
    return render_template("about.html")

@app.route("/account")
def account():
    return render_template("account.html")

@app.route("/today")
def today():
    return render_template("today.html")


#if name == "main":
    #app.run()