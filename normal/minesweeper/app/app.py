import os
import urllib

from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

app = Flask(__name__, static_folder="static")
app.secret_key = os.urandom(32)

try:
    FLAG = open("./flag.txt", "r").read()
except:
    FLAG = "FLAG"


def admin(
    url,
    cookie={"name": "FLAG", "value": FLAG},
):
    cookie.update({"domain": "127.0.0.1"})

    try:
        options = webdriver.ChromeOptions()
        for _ in [
            "headless",
            "window-size=1920x1080",
            "disable-gpu",
            "no-sandbox",
            "disable-dev-shm-usage",
        ]:
            options.add_argument(_)
        service = Service(executable_path=r"/usr/bin/chromedriver")
        driver = webdriver.Chrome(
            service=service,
            options=options,
        )
        driver.implicitly_wait(3)
        driver.set_page_load_timeout(3)
        driver.get("http://127.0.0.1:8000/favicon.ico")
        driver.add_cookie(cookie)
        driver.refresh()
        driver.get(url)
    except Exception as e:
        print(e)
        driver.quit()
        return False
    driver.quit()
    return True


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/report", methods=["GET", "POST"])
def report():
    if request.method == "GET":
        return render_template("report.html")

    elif request.method == "POST":
        url = "http://127.0.0.1:8000/" + request.form.get("url", None)
        admin(url)

        return "OKAY :)"


app.run(host="0.0.0.0", port=8000)
