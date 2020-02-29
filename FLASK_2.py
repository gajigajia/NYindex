from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)


# 아니 이렇게 한다면 지금 HTML을 두페이지 만들겠다는 것이잖아요?^^
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index_jan', methods=['GET'])
def index_jan():
    return render_template('table_jan.html')

'''@app.route('/index_feb', methods=['GET'])
def index_feb():
    return render_template('table_feb.html')'''


# 1월로 들어가면 GET요청을 가져와서 1월꺼를 보여줘....... 우선은 그냥 여기 들어가면 다 보여주는걸로 하자
@app.route('/database', methods=['GET'])
def database():
    # DB import를 여기다 해야한다
    client = MongoClient('localhost', 27017)

    index = client.dbsparta.indice.find({},{'_id':0})
    rawdata = []

    for item in index:
        rawdata.append(item)
    temp_data = str(rawdata)
    # FLASK는 list형은 불러오지 않으므로 jsonify를 사용하여 dict형으로 해야함. type(data)하면 data가 무슨 데이터타입인지 보여줌
    print(rawdata)
    return jsonify(rawdata)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
