import certifi
import urllib3
import time
import sys
import Adafruit_DHT

# start rasp config
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
    print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
    sys.exit(1)

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
# end rasp config

http = urllib3.PoolManager(
cert_reqs = 'CERT_REQUIRED', # Force certificate check.
ca_certs = certifi.where(),  # Path to the Certifi bundle.
)

url = 'https://iotmmsi321817trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/435c2d3f-2fd9-44bd-ba7b-c3b8e4db4cb1'

headers = urllib3.util.make_headers()
# use with authentication
# please insert correct OAuth token
headers['Authorization'] = 'Bearer ' + '2258823ae3603d4d56f847bd5f1f0ae'
headers['Content-Type'] = 'application/json;charset=utf-8'

# c = "99"


# print c
# body='{"mode":"async", "messageType":"da567028aba7d298d521", "messages":[{"sensor1":"test_rest_call_py","timestamp":1475500886}]}'
# body='{"mode":"async", "messageType":"da567028aba7d298d521", "messages":[{"sensor1": "'+c+'" ,"timestamp":1475500886}]}'
# print body

# print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))


# try:
# 	r = http.urlopen('POST', url, body=body, headers=headers)
# 	print(r.status)
# 	print(r.data)
# except urllib3.exceptions.SSLError as e:
# 	print e
#  var c

while True:
	c = "b411012"
	# t = '{0:0.1f}*'.format(temperature)
	if humidity is not None and temperature is not None:
		#####
		temp = '{0:0.1f}*C'.format(temperature)
		body = '{"mode":"async", "messageType":"da567028aba7d298d521", "messages":[{"sensor1":"' + temp + '" ,"timestamp":1475500886}]}'
		try:
			r = http.urlopen('POST', url, body=body, headers=headers)
			print(r.status)
			print(r.data)
		except urllib3.exceptions.SSLError as e:
			print e
		time.sleep(5)
	else:
		print ('failed to get reading')
		sys.exit(1)

	# body = '{"mode":"async", "messageType":"da567028aba7d298d521", "messages":[{"sensor1":"'+c+'" ,"timestamp":1475500886}]}'
    #
	# try:
	# 	r = http.urlopen('POST', url, body=body, headers=headers)
	# 	print(r.status)
	# 	print(r.data)
	# except urllib3.exceptions.SSLError as e:
	# 	print e
	# time.sleep(5)
