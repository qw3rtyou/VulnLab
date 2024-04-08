from flask import Flask, request, render_template_string, render_template
import os

app = Flask(__name__)
app.secret_key = os.getenv("FLAG")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ssti", methods=["GET", "POST"])
def ssti():
    result = None
    if request.method == "POST":
        payload = request.form["payload"]
        result = render_template_string(f"{payload}")
    return render_template("ssti.html", result=result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10004)
