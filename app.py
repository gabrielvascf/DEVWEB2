from flask import Flask, render_template
from jinja2.exceptions import TemplateNotFound

app = Flask("__name__")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/<filename>")
def templates(filename):
    try:
        return render_template(f"{filename}.html")
    except TemplateNotFound:
        return "Página não encontrada", 404

if __name__ == '__main__':
    app.run(debug=True)