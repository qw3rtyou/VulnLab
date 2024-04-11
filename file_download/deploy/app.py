#!/usr/bin/env python3
import os
import subprocess
from flask import Flask, request, render_template

APP = Flask(__name__)
APP.secret_key = "**FAKEKEY**"


@APP.route("/")
def index():
    files = os.listdir("uploads")
    return render_template("index.html", files=files)


@APP.route("/read")
def read_memo():
    error = False
    data = b""

    filename = request.args.get("name", "")

    try:
        with open(f"uploads/{filename}", "rb") as f:
            data = f.read()
    except (IsADirectoryError, FileNotFoundError):
        error = True

    return render_template(
        "read.html",
        filename=filename,
        content=data.decode("utf-8"),
        error=error,
    )

@APP.route("/admin")
def admin():
    secret_key = request.args.get("key", "")
    if secret_key == APP.secret_key:
        try:
            result = subprocess.run(["./flag"], capture_output=True, text=True, check=True)
            msg = result.stdout
        except Exception as e:
            msg = f"Error.."
    else:
        msg = "You are not Admin"
    return render_template(
        "admin.html",
        msg=msg,
    )


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=8000)
