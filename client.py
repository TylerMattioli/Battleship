import sys
import urllib
import http.client

IP = sys.argv[1]
port = sys.argv[2]
y = sys.argv[3]
x = sys.argv[4]

#Post example on https://docs.python.org/2.4/lib/httplib-examples.html
connection = http.client.HTTPConnection(IP, port)
parameters = urllib.parse.urlencode({'x':x, 'y':y})
headers = {"Content-type": "application/x-www-form-urlencoded", "Content-length": "7"}
connection.request("POST", "", parameters, headers)
ping = connection.getresponse()
print ("Ping")
print (ping.status, ping.reason)
board = str(ping.read())
print (board)




for ship in board:
	if ship == '0':
		print ("Miss")
		parameters = urllib.parse.urlencode({'x':x, 'y':y, 'hit': '0'})
	if ship == '1':
		print ("Hit")
		parameters = urllib.parse.urlencode({'x':x, 'y':y, 'hit': '0'})
	if ship == 'C':
		print ("Carrier sunk")
	if ship == 'B':
		print ("Battleship sunk")
	if ship == 'R':
		print ("Cruiser sunk")
	if ship == 'S':
		print ("Submarine sunk")
	if ship == 'D':
		print ("Destroyer sunk")

connection.request("POST", "/return", parameters, headers)
connection.close