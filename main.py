import os
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def root():
    return render_template('index.html')


@app.route("/index.html")
def index():
    return render_template('index.html')


@app.route("/trainings.html")
def train():
    return render_template('trainings.html')


@app.route("/classes.html")
def _class():
    return render_template('classes.html')


@app.route("/shows.html")
def shows():
    return render_template('shows.html')


@app.route("/shortcodes.html")
def shortcodes():
    return render_template('shortcodes.html')


@app.route("/contact.html")
def contact():
    return render_template('contact.html')


@app.route("/name/<name>")
def _name(name):
    return f'Hi! {name}'


if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 8080)))
