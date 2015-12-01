from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def get_place_holder():
    return render_template("holder.html")


if __name__ == '__main__':
        app.run()
