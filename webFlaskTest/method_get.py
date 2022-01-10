from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/method', methods=['GET'])
def method():
  if request.method == 'GET':
    id = request.args["id"]
    password = request.args.get("password")
  return "get으로 전달된 데이터 ({},{})".format(id, password)

@app.route("/method_get", methods=['GET'])
def method_get():
  return render_template("method_get.html")

@app.route('/method_get_act', methods=['GET'])
def method_get_act():
  if request.method == 'GET':
    id_param = request.args["id"]
    password_param = request.args.get("password")
  return render_template("method_get.html", id=id_param, password=password_param)

@app.route('/')
def index():
  return render_template('test_html.html')

@app.route('/sub1')
def sub1():
  return 'SUB1 page'

@app.route('/sub2')
def sub2():
  return 'SUB2 page'

if __name__ == '__main__':
  app.run(debug=True, port=80, host='0.0.0.0')