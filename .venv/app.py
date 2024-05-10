from services.get_data import get_news
from flask import Flask,render_template

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/news", methods=['GET'])
def get_data():
    return get_news()

@app.route("/doc")
def render_docs():
    return render_template("docs.html")



if __name__ == "__main__":
    app.run(debug=True)

