
from flask import Flask,render_template
from services.get_data import get_news
from flask_cors import CORS




app = Flask(__name__)
CORS(app) 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/news", methods=['GET'])
def get_data():
    return get_news()


@app.route("/docs")
def render_docs():
    return render_template("docs.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)