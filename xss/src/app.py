from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
import requests

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_HOST = os.getenv('MYSQL_HOST')
SECRET_KEY = os.getenv('ADMIN_SECRET_KEY')
CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')
localhost = "http://localhost:10002"

app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.content}')"
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/board')
def board():
    posts = Post.query.all()
    message = request.args.get('message', None)
    return render_template('board.html', posts=posts, message=message)


@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('board'))
    return render_template('add_post.html')

@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        return redirect(url_for('board'))
    return render_template('edit_post.html', post=post)

@app.route('/delete/<int:post_id>', methods=['GET'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('board'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['search']
        posts = Post.query.filter(Post.title.contains(search_term) | Post.content.contains(search_term)).all()
        return render_template('search.html', posts=posts)
    return render_template('search.html')

@app.route('/admin/<int:post_id>', methods=['GET', 'POST'])
def admin(post_id):
    bot_url = "http://proxy:80/report"
    
    cookie = {"name": "cookie", "value": SECRET_KEY}
    data = {"name": "url", "value": localhost + f"/post/{post_id}"}

    success = requests.post(bot_url, data=data)
    
    if success:
        message = f"Bot activated successfully and visited: {bot_url}"
    else:
        message = f"Bot activation failed: {bot_url}"
    
    posts = Post.query.all()
    return render_template('board.html', posts=posts, message=message)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10002, debug=True)