from flask import Flask, render_template
from time import sleep
import os

flag = os.getenv("FLAG")
app = Flask(__name__)

counter = 0


@app.route("/increase")
def increase():
    global counter

    if counter < 15:
        sleep(0.1)
        counter += 1
        return render_template("index.html", counter=counter, message="Increased++")
    elif counter > 15:
        return render_template(
            "index.html", counter=counter, message="Success!!\t" + flag
        )
    else:
        return render_template("index.html", counter=counter, message="Denied##")


@app.route("/reset")
def reset():
    global counter
    counter = 0
    return render_template("index.html", counter=counter)


@app.route("/")
def index():
    global counter
    return render_template("index.html", counter=counter)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, threaded=True)
