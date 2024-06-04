from flask import (
    Flask,
    g,
    render_template,
    request,
    session,
)
from datetime import datetime
import uuid
import os

app = Flask(__name__)
app.secret_key = "5uperSTR00oooongK3y"


@app.before_request
def check_session():
    if "user_id" not in session:
        session["user_id"] = str(uuid.uuid4())

    g.user_id = session["user_id"]

    user_log_path = os.path.join("log", g.user_id)

    if not os.path.exists(user_log_path):
        os.makedirs(user_log_path)

    log_request()


def log_request():
    logid = request.args.get("name", "default")
    user_log_path = os.path.join("log", g.user_id)
    log_file = os.path.join(user_log_path, logid)

    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} - {request.method} {request.path}\n")


@app.route("/", methods=["GET"])
def main():
    user_log_path = os.path.join("log", g.user_id)
    logs = os.listdir(user_log_path)
    return render_template("index.html", logs=logs)


@app.route("/zip", methods=["GET"])
def zip():
    user_log_path = os.path.join("log", g.user_id)

    try:
        os.system(f"cd {user_log_path} && tar -czvf out.tar.gz *")
    except Exception as e:
        return f"Error : {e}", 500

    logs = os.listdir(user_log_path)
    return render_template("index.html", logs=logs)


@app.route("/init", methods=["GET"])
def init():
    user_log_path = os.path.join("log", g.user_id)

    try:
        os.system(f"rm -rf {user_log_path}/*")
    except Exception as e:
        return f"Error : {e}", 500

    logs = os.listdir(user_log_path)
    return render_template("index.html", logs=logs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, threaded=True)
