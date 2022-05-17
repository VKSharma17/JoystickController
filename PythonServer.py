
from flask import Flask, Response, request
import argparse
import time
import serial

app = Flask(__name__)

RCCarArduino = serial.Serial('COM9', 9600)


@app.after_request
def add_header(r):
	"""
	Add headers to both force latest IE rendering or Chrome Frame,
	and also to cache the rendered page for 10 minutes
	"""
	r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
	r.headers["Pragma"] = "no-cache"
	r.headers["Expires"] = "0"
	r.headers["Cache-Control"] = "public, max-age=0"
	return r

@app.route("/api", methods=['POST'])
def clicked():
	direction = int(request.get_data())
	print(f'Captured Click {direction}')
	if direction == 3:
		#Move RCCar Left
		print("Move RCCar Left")
		RCCarArduino.write(str.encode('a'))

	elif direction == 4:
		#Move RCCar Right
		print("Move RCCar Right")
		RCCarArduino.write(str.encode('d'))

	elif direction == 2:
		#Move RCCar Forward
		print("Move RCCar Forward")
		RCCarArduino.write(str.encode('w'))

	elif direction == 5:
		#Move RCCar Backward
		print("Move RCCar Backward")
		RCCarArduino.write(str.encode('s'))

	elif direction == 6:
		print("Resetting/Stopping")
		RCCarArduino.write(str.encode('r'))

	return "OK"

if __name__=="__main__":
	# socketio.run(app,host="0.0.0.0",port="3005",threaded=True)
	parser = argparse.ArgumentParser()
	parser.add_argument('-p','--port',type=int,default=5000, help="Running port")
	parser.add_argument("-H","--host",type=str,default='0.0.0.0', help="Address to broadcast")
	args = parser.parse_args()
	print("Starting server")
	app.run(host=args.host,port=args.port)
