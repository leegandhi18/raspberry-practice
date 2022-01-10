# 문제 풀이10 
# Flask

# 라즈베리파이 GPIO 17 LED연결
# 라즈베리파이 GPIO 27 LED연결
# 라즈베리파이 GPIO 23 LED연결

# Web에서 제어 할 수 있는 버튼 4개 만들기(html)
# 1번 버튼 1번 LED on
# 2번 버튼 1번 LED off
# 3번 버튼 2번 LED on
# 4번 버튼 2번 LED off
from flask import Flask, render_template, request 
import RPi.GPIO as GPIO

LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
LED2 = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED2, GPIO.OUT)

app = Flask(__name__)

@app.route('/led_control')
def led_control():
    data =[]
    return render_template('led_test.html' , values= data)

@app.route('/led_control_act', methods=['GET'])
def led_control_act():
    data = []
    if request.method == 'GET':
        status = ''
        led = request.args["led"]
        if led == '1':
            GPIO.output(LED,True)
            print('led1 on')
            status = 'ON'
        elif led == '2':
            GPIO.output(LED,False)
            print('led1 off')
            status = 'OFF'
        elif led == '3':
            GPIO.output(LED2,False)
            print('led2 on')
            status = 'OFF'
        elif led == '4':
            GPIO.output(LED2,False)
            print('led2 off')
            status = 'OFF'
    return render_template('led_test.html', ret = status , values = data)

if __name__=='__main__':
    app.run(debug=True, port=80,host='0.0.0.0')
