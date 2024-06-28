from flask import Flask, request, make_response, render_template
from urllib import parse
import os
import sys
from bs4 import BeautifulSoup

secret_flag = os.getenv('FLAG')

app = Flask(__name__)

import requests

def check_for_alert_function_in_url(url,data):
    response = requests.post(url,data=data)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        script_tags = soup.find_all('script')
        for script_tag in script_tags:
            script_content = script_tag.string
            if script_content and 'alert(' in script_content:
                return True
        return False
    else:
        print("err",sys.stderr)
        return False
    


@app.route('/report', methods=['GET','POST'])
def report():
    if request.method == "POST":

        header = request.form["header"]
        user_input = request.form["value"]

        if check_for_alert_function_in_url("http://localhost",{"header":header,"value":user_input}):
            response = make_response(f'{secret_flag}')
            return response
        return make_response(f'Nice try!')

    return render_template("index.html")

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":

        header = request.form["header"]
        user_input = request.form["value"]


        response = make_response(f'I\'t is very good day to walk out. Power thourgh!!!!')

        response.headers.set(header, user_input)

        return response

    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)