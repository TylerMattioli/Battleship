import sys
import http.client
import urllib
from urllib import parse
from bottle import get, run, request, response, route, template, Bottle


port = sys.argv[1]
file = sys.argv[2]

own_board = []
board = open(file)
for n in range(0,10):
	new_row = board.readline().strip('\n')
	own_board.append([])
	for ship in new_row:
		own_board[n].append(ship)

opponent_board = [['_' for n in range(0,10)] for m in range(0,10)]


bot = Bottle()


@bot.post('/')
def taking_fire():
	x = request.POST['x']
	y = request.POST['y']

	CLife = 5
	BLife = 4
	RLife = 3
	SLife = 3
	DLife = 1


	try:
		x=int(x)
		y=int(y)
	except ValueError:
		print("Values are not integers")
		ping.status = 400 #bad request
		return
	if x == '10' or y>=10 or x<0 or y<0:
		print("Values are greater than 10")
		ping.status = 404 #out of bounds
		return

	if opponent_board[x][y] == '_':
		opponent_board[x][y] = '<b><div style="color:blue">O</div></b>'
	else:
		opponent_board[x][y] = '<b><div style="color:red">X</div></b>'


	if own_board[x][y] == '_':
		own_board[x][y] = '<b><div style="color:blue">O</div></b>'
		return ('Hit = 0'.encode())
	elif own_board[x][y] == 'O' or own_board[x][y] == 'X':
		ping.status = 410
		return
	else:
		own_board[x][y] = '<b><div style="color:red">X</div></b>'

		if own_board[x][y] == 'C':
			CLife -= 1
		elif own_board[x][y] == 'B':
			BLife -= 1
		elif own_board[x][y] == 'R':
			RLife -= 1
		elif own_board[x][y] == 'S':
			SLife -= 1
		elif own_board[x][y] == 'D':
			DLife -= 1

		if CLife == 0:
			return ('Hit = 1 ' + 'Sunk C'.encode())
		elif BLife == 0:
			return ('Hit = 1 ' + 'Sunk B'.encode())
		elif RLife == 0:
			return ('Hit = 1 ' + 'Sunk R'.encode())
		elif SLife == 0:
			return ('Hit = 1 ' + 'Sunk S'.encode())
		elif DLife == 0:
			return ('Hit = 1 ' + 'Sunk D'.encode())
		else:
			return ('Hit = 1'.encode())


@bot.post('/return')
def sending_fire():
	x = request.POST['x']
	y = request.POST['y']

	if opponent_board[x][y] == '_':
		[x][y] = '<b><div style="color:blue">O</div></b>'
	else:
		opponent_board[x][y] = '<b><div style="color:red">X</div></b>'



@bot.get('/own_board.html')
def my_board():
	table = '<center>Your Board<table style="width75%;border: 1px solid black">'
	for n in range(0,10):
		table += str('<tr>')
		for m in range(0,10):
			table += str('<td>') + str(own_board[n][m]) + str('<td>')
		table += str('</tr>')
	table += str('</table></center>')
	return table

@bot.get('/opponent_board.html')
def opponentboard():
	table = '<center>Not Your Board<table style="width75%;border: 1px solid black">'
	for n in range(0,10):
		table += str('<tr>')
		for m in range(0,10):
			table += str('<td>') + str(opponent_board[n][m]) + str('<td>')
		table += str('</tr>')
	table += str('</table></center>')
	return table


run(bot, host='127.0.0.1', port=port)












