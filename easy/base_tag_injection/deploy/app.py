from flask import Flask, render_template, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
import secrets

import os
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

app = Flask(__name__)

MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
SECRET_KEY = os.getenv("ADMIN_SECRET_KEY")
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH")
localhost = "http://localhost:10006"

app.secret_key = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(64), nullable=False)
    title = db.Column(db.String(64), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.content}')"

nonce = secrets.token_hex(16)

#SCP설정
@app.after_request
def set_csp(response): 
    response.headers['Content-Security-Policy'] = f"script-src 'nonce-{nonce}'"
    return response

@app.route('/')
def index():
    posts = Post.query.all()
    global nonce
    nonce = secrets.token_hex(16)
    return render_template('index.html', posts=posts, nonce=nonce)

@app.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'POST':
        content = request.form['content']
        title = request.form['title']
        password = request.form['password']
        if len(password) < 4:
            return "비밀번호는 4자 이상이어야 합니다."
        post = Post(content=content, password=password, title=title)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('write.html')

@app.route('/post/<int:id>', methods=['GET', 'POST'])
def view_post(id):
    post = Post.query.get_or_404(id)
    global nonce
    if '127.0.0.1' == request.remote_addr: #if admin bot
        
        nonce = secrets.token_hex(16)
        return render_template('post.html', post=post, nonce=nonce)
    
    if request.method == 'POST':
        nonce = secrets.token_hex(16)

        password = request.form['password']
        if password == post.password:
            return render_template('post.html', post=post,nonce=nonce)
        else:
            return "비밀번호가 일치하지 않습니다."
    return render_template('view_post.html', post=post)

@app.route('/delete/<int:id>')
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))

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


@app.route("/admin/<int:post_id>", methods=["GET", "POST"])
def admin(post_id):
    target_url = localhost + f"/post/{post_id}"

    if requests.get(target_url).status_code == 404:
        message = f"Unvalid Post ID"
        posts = Post.query.all()
        return render_template("index.html", posts=posts, message=message)

    cookie = {"name": "cookie", "value": SECRET_KEY}
    success = read_url(target_url, cookie)

    if success:
        message = f"Bot activated successfully and visited: {target_url}"
    else:
        message = f"Bot activation failed: {target_url}"

    posts = Post.query.all()
    return render_template("index.html", posts=posts, message=message)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10006, debug=True)