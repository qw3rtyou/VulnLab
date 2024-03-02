from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/hello')
def hello():
    name = request.args.get('name', 'World')
    # 사용자 입력을 템플릿에 바로 사용하여 SSTI 실습 환경 제공
    greeting = render_template_string(f'<h1>Hello, {name}!</h1>')
    return render_template_string('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SSTI Lab</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
<div class="container mt-5">
    ...
    <div class="mt-3">
        <h3>Greeting Result:</h3>
        <div class="alert alert-success" role="alert">
            ''' + greeting + '''
        </div>
    </div>
</div>
</body>
</html>''', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10004)