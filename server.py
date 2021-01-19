from flask import Flask, render_template
from flask_cors import CORS
import serial

# app = Flask(__name__)
app = Flask(__name__, static_url_path='')

CORS(app)

COMM = '/dev/ttyACM0'

ser = serial.Serial(COMM, 9600, timeout=0)


@app.route('/test_connection/', methods=['POST', 'GET'])
def test_connection():
    return "OK"


@app.route('/switch_device/on/', methods=['GET'])
def switch_device_on():
    print("Device Switched ON")
    try:
        ser.write(b"1")
        return "Device Switched ON"
    except:
        return "Device Not Found"


@app.route('/switch_device/off/', methods=['GET'])
def switch_device_off():
    print("Device Switched OFF")
    try:
        ser.write(b"0")
        return "Device Switched OF"
    except:
        return "Device Not Found"


@app.route("/")
def root():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
