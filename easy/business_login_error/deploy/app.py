from flask import Flask, render_template, request, redirect, session, url_for
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 세션 보안을 위한 시크릿 키 설정

# 사용자가 가지고 있는 물품 목록을 세션에 저장
def add_item_to_inventory(item_name):
    if 'inventory' not in session:
        session['inventory'] = []
    if item_name == 'flag':
        item_name = os.getenv('FLAG')
    session['inventory'].append(item_name)

# 가게의 상품 목록
store_items = {
    'ice_cream': {'name': '아이스크림', 'price': 1000},
    'snack': {'name': '과자', 'price': 1500},
    'ramen': {'name': '라면', 'price': 2000},
    'flag': {'name': '플래그', 'price': 9999999}
}

# 사용자의 돈을 세션에 저장하고 처음 가입할 때 10000원을 지급
def initialize_user():
    if 'money' not in session:
        session['money'] = 10000

# 루트 경로: 로그인 폼 렌더링
@app.route('/', methods=['GET', 'POST'])
def login():
    initialize_user()  # 사용자 초기화
    if request.method == 'POST':
        # 폼에서 제출된 아이디 받기
        user_id = request.form['user_id']
        if user_id not in session:
            # 아이디가 세션에 없으면 추가
            session['user_id'] = user_id
            return redirect(url_for('main'))
        else:
            return "이미 로그인된 상태입니다."
    return render_template('login.html')

# 메인 페이지: 로그인 후 상점 이동
@app.route('/main')
def main():
    initialize_user()  # 사용자 초기화
    if 'user_id' in session:
        return render_template('main.html', items=store_items)
    else:
        return redirect(url_for('login'))

# 로그아웃: 세션 제거 후 로그인 페이지로 이동
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('money', None)
    return redirect(url_for('login'))

@app.route('/inventory')
def get_inventory():
    initialize_user()  # 사용자 초기화
    if 'user_id' in session:
        inventory = session.get('inventory', [])
        return render_template('inventory.html', inventory=inventory)
    else:
        return redirect(url_for('login'))

# 상점: 상품 목록 표시
@app.route('/store/<item_name>', methods=['POST'])
def buy_item(item_name):
    initialize_user()  # 사용자 초기화
    if 'user_id' in session:
        if item_name in store_items:
            item = store_items[item_name]
            quantity = int(request.form.get('quantity', 1))  # 수량 입력 받기
            total_price = item['price'] * quantity
            if session['money'] >= total_price:
                session['money'] -= total_price
                for _ in range(quantity):
                    add_item_to_inventory(item_name)  # 수량만큼 물품 추가
                message = f"{item['name']}을(를) {quantity}개 구매하였습니다. 남은 돈: {session['money']}원"
                return render_template('main.html', items=store_items, inventory=session.get('inventory', []), message=message)
            else:
                message = "돈이 부족합니다."
                return render_template('main.html', items=store_items, inventory=session.get('inventory', []), message=message)
        else:
            return "존재하지 않는 상품입니다."
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
