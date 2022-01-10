from flask import Flask, render_template, request
import RPi.GPIO as GPIO

LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

app = Flask(__name__)

@app.route('/led_control')
def led_control():
  data = []
  return render_template('led_control.html', values=data)

@app.route('/led_control_act', methods=['GET'])
def led_control_act():
  if request.method == 'GET':
    status = ''
    data = []
    led = request.args["led"]
    if led == '1':
      GPIO.output(LED, True)
      status = "ON"
      data=[1,0]
    else:
      GPIO.output(LED, False)
      status = "OFF"
      data=[0,1]
  return render_template('led_control.html', ret = status, values=data)

if __name__ == '__main__':
  app.run(debug=True, port=80, host='0.0.0.0')