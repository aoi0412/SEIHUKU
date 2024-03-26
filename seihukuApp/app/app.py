#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template

#Flaskオブジェクトの生成
app = Flask(__name__)


#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    return "Hello World"


#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/iida")
def iida():
    return render_template("iida.html")

@app.route("/nagai")
def nagai():
    return render_template("nagai.html")

#おまじない
if __name__ == "__main__":
    app.run(debug=True)
