from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
# def hello():
  # return 'Hello Flask'
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