from flask import Flask,jsonify
from book_flask import books
app =Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    sqls = "select * from book_infos limit 3"
    datas = books.Connect_DB('books').execute_many(sqls)
    # print('data',datas)
    # data = []
    # for temp in datas:
    #     data.append(temp)
    return jsonify(datas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1991, debug=True)