from flask import Flask, render_template, request, redirect, url_for, flash

import bleach
import os
import requests
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


app = Flask(__name__)
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH")
FLAG = os.getenv("SECRET_KEY")
localhost = "http://localhost:10010/"


@app.route("/")
def index():
    return render_template("index.html")


def read_url(url, cookie={"name": "name", "value": "value"}):
    driver = None
    try:
        service = Service(executable_path=CHROMEDRIVER_PATH)

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(service=service, options=options)

        driver.implicitly_wait(3)
        driver.set_page_load_timeout(10)

        driver.get(localhost)
        driver.add_cookie(cookie)
        driver.get(url)

        time.sleep(3)

    except Exception as e:
        import sys
        print(e,file=sys.stderr)
        if driver:
            driver.quit()
        return False
    finally:
        if driver:
            driver.quit()
        return True


@app.route("/report", methods=["GET", "POST"])
def report():
    if request.method == "GET":
        return render_template("report.html")

    target_url = localhost + request.form["report_url"]

    if requests.get(target_url).status_code == 404:
        return render_template(
            "report.html", message="Invaild URL", localhost=localhost
        )

    cookie = {"name": "cookie", "value": FLAG}
    success = read_url(target_url, cookie)

    if success:
        message = f"Report success: {target_url}"
    else:
        message = f"Report failed: {target_url}"

    return render_template("report.html", message=message, localhost=localhost)


@app.route("/practice", methods=["GET"])
def practice():
    content = request.args.get("content")
    if not content:
        return render_template("practice.html")

    sanitized_content = bleach.clean(
        content,
        tags=["h1", "h2", "h3", "h4", "span", "a", "i", "b"],
        attributes=["id", "name", "href"],
        protocols=["http", "https", "javascript"],
    )
    return render_template("practice.html", content=sanitized_content)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10010, debug=True)
