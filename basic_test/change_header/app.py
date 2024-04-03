from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def home():
    user_agent = request.headers.get('User-Agent')
    cookie = request.cookies.get('cookie')
    proxy_header = request.headers.get('Proxy')

    if user_agent != 'bot':
        return jsonify({'message': 'bot이 아닙니다!'}), 403
    elif cookie != 'So sweat cookie~':
        return jsonify({'message': '쿠키가 올바르지 않습니다!'}), 403
    elif proxy_header != 'is fun~':
        return jsonify({'message': '만족하지 않습니다!'}), 403
    else:
        return jsonify({'message': '성공! 수고하셨습니다 :)'}), 200

@app.route('/hint')
def hint():
    return jsonify({
        1: 'User-Agent 헤더를 "bot"으로 설정하세요!',
        2: '쿠키에 "So sweat cookie~" 값을 설정하세요!',
        3: '새로운 헤더로 "Proxy: is fun~"를 설정하세요!',
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

