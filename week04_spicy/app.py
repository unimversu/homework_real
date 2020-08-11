from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_orders():
    colordetail = request.form['colordetail_api']
    sizedetail = request.form['sizedetail_api']
    namedetail = request.form['namedetail_api']
    addetail = request.form['addetail_api']
    numdetail = request.form['numdetail_api']

    # 2. DB에 정보 삽입하기
    doc = {
        'colordetail': colordetail,
        'sizedetail': sizedetail,
        'namedetail': namedetail,
        'addetail': addetail,
        'numdetail': numdetail,
    }
    db.orders.insert_one(doc)
    # 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg': '주문해주셔서 감사합니다!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.orders.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)