import json
import random
import time
from datetime import datetime

from flask import Flask, Response, render_template

app = Flask(__name__)
random.seed()  # Initialize the random number generator


@app.route('/')
def index():
    return render_template('chart_js.html')


@app.route('/chart-data')
def chart_data():
    def generate_random_data():
        while True:
            json_data = json.dumps(
                {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': random.random() * 100})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    return Response(generate_random_data(), mimetype='text/event-stream')

if __name__=='__main__':
    app.run(debug=True, port=80,host='0.0.0.0')
