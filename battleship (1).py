# Alex Rafkin and Paul Reich
# CS 111 Final Project
# battleship.py

from graphics import *
import random
import time

# This checks if you want to play the game, or if you have already played, if you want to play again.
def wantPlay():
	play = input('Would you like to play Battleship? (Y/N)')
	if play not in ['Y', 'y', 'N', 'n']:
		return wantPlay()
	return play

# This picks the level you want to play at.
def pickLevel(): 
	level = input('Do you want to play the easy, medium, hard, or impossible version? Warning: Impossible is very hard. (E/M/H/I)')
	if level not in ['E', 'e', 'M', 'm', 'H', 'h', 'I', 'i']:
		return pickLevel()
	return level
	
# This prints out the board.

winOpp = GraphWin('Battleship: Opponent Window', 500, 500)
winPlayer = GraphWin('Battleship: Player Window', 500, 500)
	
for win in [winPlayer, winOpp]:
	for i in range(0, 500, 50):
		gridLinesHo = Line(Point(i, 0), Point(i, 500))
		gridLinesHo.setWidth(2)
		gridLinesHo.draw(win)
		gridLinesVert = Line(Point(0, i), Point(500, i))
		gridLinesVert.setWidth(2)
		gridLinesVert.draw(win)

# Player will set their ships.
		
hitspots = []
def placeS1():
	hv1 = input('Ship1 horizontal or vertical? (h/v)')
	if hv1 not in ['h','v']:
		print('Invalid input, please try again.')
		return placeS1()
	print('Please place top or left most end of ship')
	clickPoint = winPlayer.getMouse()
	r1 = (clickPoint.getX() // 50) + 1
	c1 = (clickPoint.getY() // 50) + 1
	if hv1 == 'v':
		ship1 = [[r1,c1], [r1,c1+1]]
		ship1drawn = Oval(Point((r1-1)*50, (c1-1)*50), (Point((r1*50), ((c1+1)*50))))
		if c1 > 9:
			print('This placement is invalid! Try again.')
			return placeS1()
	elif hv1 == 'h':
		ship1 = [[r1,c1], [r1+1,c1]]
		ship1drawn = Oval(Point((r1-1)*50, (c1-1)*50), (Point(((r1+1)*50), (c1*50))))
		if r1 > 9:
			print('This placement is invalid! Try again.')
			return placeS1()
	ship1drawn.setFill('gray')
	ship1drawn.draw(winPlayer)
	for spot in ship1:
		hitspots.append(spot)

def placeS2():
	hv2 = input('Ship2 horizontal or vertical? (h/v)')
	if hv2 not in ['h','v']:
		print('Invalid input, please try again.')
		return placeS2()
	print('Please place top or left most end of ship')
	clickPoint = winPlayer.getMouse()
	r2 = (clickPoint.getX() // 50) + 1
	c2 = (clickPoint.getY() // 50) + 1
	if hv2 == 'v':
		ship2 = [[r2,c2], [r2,c2+1], [r2,c2+2]]
		ship2drawn = Oval(Point((r2-1)*50, (c2-1)*50), (Point((r2*50), ((c2+2)*50))))
		if c2 > 8:
			print('This placement is invalid! Try again.')
			return placeS2()
	elif hv2 == 'h':
		ship2 = [[r2,c2], [r2+1,c2], [r2+2,c2]]
		ship2drawn = Oval(Point((r2-1)*50, (c2-1)*50), (Point(((r2+2)*50), (c2*50))))
		if r2 > 8:
			print('This placement is invalid! Try again.')
			return placeS2()
	for spot in ship2:
		if spot in hitspots:
			print('This placement is invalid! Try again.')
			return placeS2()		
	ship2drawn.setFill('gray')
	ship2drawn.draw(winPlayer)
	for spot in ship2:
		hitspots.append(spot)

def placeS3():
	hv3 = input('Ship3 horizontal or vertical? (h/v)')
	if hv3 not in ['h','v']:
		print('Invalid input, please try again.')
		return placeS3()
	print('Please place top or left most end of ship')
	clickPoint = winPlayer.getMouse()
	r3 = (clickPoint.getX() // 50) + 1
	c3 = (clickPoint.getY() // 50) + 1
	if hv3 == 'v':
		ship3 = [[r3,c3], [r3,c3+1], [r3,c3+2]]
		ship3drawn = Oval(Point((r3-1)*50, (c3-1)*50), (Point((r3*50), ((c3+2)*50))))
		if c3 > 8:
			print('This placement is invalid! Try again.')
			return placeS3()
	elif hv3 == 'h':
		ship3 = [[r3,c3], [r3+1,c3], [r3+2,c3]]
		ship3drawn = Oval(Point((r3-1)*50, (c3-1)*50), (Point(((r3+2)*50), (c3*50))))
		if r3 > 8:
			print('This placement is invalid! Try again.')
			return placeS3()
	for spot in ship3:
		if spot in hitspots:
			print('This placement is invalid! Try again.')
			return placeS3()
	ship3drawn.setFill('gray')
	ship3drawn.draw(winPlayer)
	for spot in ship3:
		hitspots.append(spot)
	
def placeS4():
	hv4 = input('Ship4 horizontal or vertical? (h/v)')
	if hv4 not in ['h','v']:
		print('Invalid input, please try again.')
		return placeS4()
	print('Please place top or left most end of ship')
	clickPoint = winPlayer.getMouse()
	r4 = (clickPoint.getX() // 50) + 1
	c4 = (clickPoint.getY() // 50) + 1
	if hv4 == 'v':
		ship4 = [[r4,c4], [r4,c4+1], [r4,c4+2], [r4, c4+3]]
		ship4drawn = Oval(Point((r4-1)*50, (c4-1)*50), (Point((r4*50), ((c4+3)*50))))
		if c4 > 7:
			print('This placement is invalid! Try again.')
			return placeS4()
	elif hv4 == 'h':
		ship4 = [[r4,c4], [r4+1,c4], [r4+2,c4], [r4+3,c4]]
		ship4drawn = Oval(Point((r4-1)*50, (c4-1)*50), (Point(((r4+3)*50), (c4*50))))
		if r4 > 7:
			print('This placement is invalid! Try again.')
			return placeS4()
	for spot in ship4:
		if spot in hitspots:
			print('This placement is invalid! Try again.')
			return placeS4()
	ship4drawn.setFill('gray')
	ship4drawn.draw(winPlayer)
	for spot in ship4:
		hitspots.append(spot)	
	
def placeS5():
	hv5 = input('Ship5 horizontal or vertical? (h/v)')
	if hv5 not in ['h','v']:
		print('Invalid input, please try again.')
		return placeS5()
	print('Please place top or left most end of ship')
	clickPoint = winPlayer.getMouse()
	r5 = (clickPoint.getX() // 50) + 1
	c5 = (clickPoint.getY() // 50) + 1
	if hv5 == 'v':
		ship5 = [[r5,c5], [r5,c5+1], [r5,c5+2], [r5, c5+3], [r5, c5+4]]
		ship5drawn = Oval(Point((r5-1)*50, (c5-1)*50), (Point((r5*50), ((c5+4)*50))))
		if c5 > 6:
			print('This placement is invalid! Try again.')
			return placeS5()
	elif hv5 == 'h':
		ship5 = [[r5,c5], [r5+1,c5], [r5+2,c5], [r5+3,c5], [r5+4,c5]]
		ship5drawn = Oval(Point((r5-1)*50, (c5-1)*50), (Point(((r5+4)*50), (c5*50))))
		if r5 > 6:
			print('This placement is invalid! Try again.')
			return placeS5()
	for spot in ship5:
		if spot in hitspots:
			print('This placement is invalid! Try again.')
			return placeS5()
	ship5drawn.setFill('gray')
	ship5drawn.draw(winPlayer)
	for spot in ship5:
		hitspots.append(spot)	

# The computer will set its ships now.

hitspotsC = []
shipListComp = []
r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def placeCS1():
	hv1 = random.sample(['h','v'],1)[0]
	r1 = random.sample(r,1)[0]
	c1 = random.sample(c,1)[0]
	if hv1 == 'v':
		CS1 = [[r1,c1], [r1,c1+1]]
		if c1 > 9:
			return placeCS1()
	elif hv1 == 'h':
		CS1 = [[r1,c1], [r1+1,c1]]
		if r1 > 9:
			return placeCS1()
	for spot in CS1:
		hitspotsC.append(spot)
	shipListComp.append(CS1)

def placeCS2():
	hv2 = random.sample(['h','v'],1)[0]
	r2 = random.sample(r,1)[0]
	c2 = random.sample(c,1)[0]
	if hv2 == 'v':
		CS2 = [[r2,c2], [r2,c2+1], [r2,c2+2]]
		if c2 > 8:
			return placeCS2()
	elif hv2 == 'h':
		CS2 = [[r2,c2], [r2+1,c2], [r2+2,c2]]
		if r2 > 8:
			return placeCS2()
	for spot in CS2:
		if spot in hitspotsC:
			return placeCS2()		
	for spot in CS2:
		hitspotsC.append(spot)
	shipListComp.append(CS2)

def placeCS3():
	hv3 = random.sample(['h','v'],1)[0]
	r3 = random.sample(r,1)[0]
	c3 = random.sample(c,1)[0]
	if hv3 == 'v':
		CS3 = [[r3,c3], [r3,c3+1], [r3,c3+2]]
		if c3 > 8:
			return placeCS3()
	elif hv3 == 'h':
		CS3 = [[r3,c3], [r3+1,c3], [r3+2,c3]]
		if r3 > 8:
			return placeCS3()
	for spot in CS3:
		if spot in hitspotsC:
			return placeCS3()
	for spot in CS3:
		hitspotsC.append(spot)
	shipListComp.append(CS3)
	
def placeCS4():
	hv4 = random.sample(['h','v'],1)[0]
	r4 = random.sample(r,1)[0]
	c4 = random.sample(c,1)[0]
	if hv4 == 'v':
		CS4 = [[r4,c4], [r4,c4+1], [r4,c4+2], [r4, c4+3]]
		if c4 > 7:
			return placeCS4()
	elif hv4 == 'h':
		CS4 = [[r4,c4], [r4+1,c4], [r4+2,c4], [r4+3,c4]]
		if r4 > 7:
			return placeCS4()
	for spot in CS4:
		if spot in hitspotsC:
			return placeCS4()
	for spot in CS4:
		hitspotsC.append(spot)	
	shipListComp.append(CS4)
	
def placeCS5():
	hv5 = random.sample(['h','v'],1)[0]
	r5 = random.sample(r,1)[0]
	c5 = random.sample(c,1)[0]
	if hv5 == 'v':
		CS5 = [[r5,c5], [r5,c5+1], [r5,c5+2], [r5, c5+3], [r5, c5+4]]
		if c5 > 6:
			return placeCS5()
	elif hv5 == 'h':
		CS5 = [[r5,c5], [r5+1,c5], [r5+2,c5], [r5+3,c5], [r5+4,c5]]
		if r5 > 6:
			return placeCS5()
	for spot in CS5:
		if spot in hitspotsC:
			return placeCS5()
	for spot in CS5:
		hitspotsC.append(spot)
	shipListComp.append(CS5)

# Player will take the first shot.

hitListPlayer = []
missListPlayer = []
shotListPlayer = []
def playerShot():
	print('Click where you want to shoot!')
	clickPoint = winOpp.getMouse()
	shot = [(clickPoint.getX() // 50) + 1,(clickPoint.getY() // 50) + 1]
	if shot in shotListPlayer:
		print('This is an invalid shot! Try again.')
		return playerShot()	
	elif shot in hitspotsC:
		hitListPlayer.append(shot)
		shotListPlayer.append(shot)
		print('You got a hit!')
		row = shot[0]
		column = shot[1]
		hit = Circle(Point(((row-1)*50) + 25, ((column-1)*50) + 25), 20)
		hit.setFill('red')
		hit.setWidth(2)
		hit.draw(winOpp)
	else:
		missListPlayer.append(shot)
		shotListPlayer.append(shot)
		print('You missed!')
		row = shot[0]
		column = shot[1]
		miss = Circle(Point(((row-1)*50) + 25, ((column-1)*50) + 25), 20)
		miss.setFill('blue')
		miss.setWidth(2)
		miss.draw(winOpp)	

# Computer shooting.

# Easy Version.

shotListComp = []
hitListComp = []
missListComp = []

def comptakeshot():
	allspots = []
	for row in r:
		for col in c:
			allspots.append([row, col])
	for spot in shotListComp:
		allspots.remove(spot)
	compShot = random.sample(allspots, 1)[0]
	shotListComp.append(compShot)
	return compShot
	
def compShot():
	shot = comptakeshot() 	
	if shot in hitspots:
		hitListComp.append(shot)
		print('The Computer got a hit!')
		row = shot[0]
		column = shot[1]
		hit = Circle(Point(((row-1)*50) + 25, ((column-1)*50) + 25), 20)
		hit.setFill('red')
		hit.setWidth(2)
		hit.draw(winPlayer)
	else:
		missListComp.append(shot)
		print('The Computer missed!')
		row = shot[0]
		column = shot[1]
		miss = Circle(Point(((row-1)*50) + 25, ((column-1)*50) + 25), 20)
		miss.setFill('blue')
		miss.setWidth(2)
		miss.draw(winPlayer)
		
# Medium Version - If the computer gets a hit, it will then shoot in the four spaces that surround it (If they are open). It will also get a hit regardless every 8th turn.

def compbettershot():
	AImoves = [[shotListComp[-1][0] + 1, shotListComp[-1][1]], [shotListComp[-1][0] - 1, shotListComp[-1][1]], \
	[shotListComp[-1][0], shotListComp[-1][1] + 1], [shotListComp[-1][0], shotListComp[-1][1] - 1]]
	compShot = random.sample(AImoves, 1)[0]
	x = 0
	for shot in AImoves:
		if shot in shotListComp:
			x += 1
	if x == 4:
		compShot = comptakeshot()	
	elif (compShot[0] > 10) or (compShot[0] < 1) or (compShot[1] > 10) or (compShot[1] < 1) or (compShot in shotListComp):
		compShot = compbettershot()
	else:
		shotListComp.append(compShot)
	return compShot
	
def directHit():
	compHitsLeft = []
	for shot in hitspots:
		if shot not in shotListComp:
			compHitsLeft.append(shot)
	compShot = random.sample(compHitsLeft, 1)[0]	
	shotListComp.append(compShot)
	hitListComp.append(compShot)
	return compShot
	
def compShotM():
	if ((len(shotListComp) + 1) % 8) == 0:
		shotH = directHit()
		print('The Computer got a hit!')
		row = shotH[0]
		column = shotH[1]
		hit = Circle(Point(((row-1)*50) + 25, ((column-1)*50) + 25), 20)
		hit.setFill('red')
		hit.setWidth(2)
		hit.draw(winPlayer)
	elif (len(shotListComp) > 0) and (len(hitListComp) > 0) and (shotListComp[-1] == hitListComp[-1]):
		shotH = compbettershot()
		if shotH in hitspots:
			hitListComp.append(shotH)
			print('The Computer got a hit!')
			row = shotH[0]
			column = shotH[1]
			hit = Circle(Point(((row-1)*50) + 25, ((column-1)*50) + 25), 20)
			hit.setFill('red')
			hit.setWidth(2)
			hit.draw(winPlayer)
		else:
			missListComp.append(shotH)
			print('The Computer missed!')
			row = shotH[0]
			column = shotH[1]
			miss = Circle(Point(((row-1)*50) + 25, ((column-1)*50) + 25), 20)
			miss.setFill('blue')
			miss.setWidth(2)
			miss.draw(winPlayer)		
	else:
		shot = comptakeshot() 	
		if shot in hitspots:
			hitListComp.append(shot)
			print('The Computer got a hit!')
			row = shot[0]
			column = shot[1]
			hit = Circle(Point(((row-1)*50) + 25, ((column-1)*50) + 25), 20)
			hit.setFill('red')
			hit.setWidth(2)
			hit.draw(winPlayer)
		else:
			missListComp.append(shot)
			print('The Computer missed!')
			row = shot[0]
			column = shot[1]
			miss = Circle(Point(((row-1)*50) + 25, ((column-1)*50) + 25), 20)
			miss.setFill('blue')
			miss.setWidth(2)
			miss.draw(winPlayer)

# Hard Version - If the computer gets a hit, it will then shoot in the four spaces that surround it (If they are open). It will also get a hit regardless every 5th turn.

def compShotH():
	if ((len(shotListComp) + 1) % 5) == 0:
		shotH = directHit()
		print('The Computer got a hit!')
		row = shotH[0]
		column = shotH[1]
		hit = Circle(Point(((row-1)*50) + 25, ((column-1)*50) + 25), 20)
		hit.setFill('red')
		hit.setWidth(2)
		hit.draw(winPlayer)
	elif (len(shotListComp) > 0) and (len(hitListComp) > 0) and (shotListComp[-1] == hitListComp[-1]):
		shotH = compbettershot()
		if shotH in hitspots:
			hitListComp.append(shotH)
			print('The Computer got a hit!')
			row = shotH[0]
			column = shotH[1]
			hit = Circle(Point(((row-1)*50) + 25, ((column-1)*50) + 25), 20)
			hit.setFill('red')
			hit.setWidth(2)
			hit.draw(winPlayer)
		else:
			missListComp.append(shotH)
			print('The Computer missed!')
			row = shotH[0]
			column = shotH[1]
			miss = Circle(Point(((row-1)*50) + 25, ((column-1)*50) + 25), 20)
			miss.setFill('blue')
			miss.setWidth(2)
			miss.draw(winPlayer)		
	else:
		shot = comptakeshot() 	
		if shot in hitspots:
			hitListComp.append(shot)
			print('The Computer got a hit!')
			row = shot[0]
			column = shot[1]
			hit = Circle(Point(((row-1)*50) + 25, ((column-1)*50) + 25), 20)
			hit.setFill('red')
			hit.setWidth(2)
			hit.draw(winPlayer)
		else:
			missListComp.append(shot)
			print('The Computer missed!')
			row = shot[0]
			column = shot[1]
			miss = Circle(Point(((row-1)*50) + 25, ((column-1)*50) + 25), 20)
			miss.setFill('blue')
			miss.setWidth(2)
			miss.draw(winPlayer)
			
# Impossible Version - If the computer gets a hit, it will then shoot in the four spaces that surround it (If they are open). It will also get a hit regardless every 3rd turn.
	
def compShotI():
	if ((len(shotListComp) + 1) % 3) == 0:
		shotH = directHit()
		print('The Computer got a hit!')
		row = shotH[0]
		column = shotH[1]
		hit = Circle(Point(((row-1)*50) + 25, ((column-1)*50) + 25), 20)
		hit.setFill('red')
		hit.setWidth(2)
		hit.draw(winPlayer)
	elif (len(shotListComp) > 0) and (len(hitListComp) > 0) and (shotListComp[-1] == hitListComp[-1]):
		shotH = compbettershot()
		if shotH in hitspots:
			hitListComp.append(shotH)
			print('The Computer got a hit!')
			row = shotH[0]
			column = shotH[1]
			hit = Circle(Point(((row-1)*50) + 25, ((column-1)*50) + 25), 20)
			hit.setFill('red')
			hit.setWidth(2)
			hit.draw(winPlayer)
		else:
			missListComp.append(shotH)
			print('The Computer missed!')
			row = shotH[0]
			column = shotH[1]
			miss = Circle(Point(((row-1)*50) + 25, ((column-1)*50) + 25), 20)
			miss.setFill('blue')
			miss.setWidth(2)
			miss.draw(winPlayer)		
	else:
		shot = comptakeshot() 	
		if shot in hitspots:
			hitListComp.append(shot)
			print('The Computer got a hit!')
			row = shot[0]
			column = shot[1]
			hit = Circle(Point(((row-1)*50) + 25, ((column-1)*50) + 25), 20)
			hit.setFill('red')
			hit.setWidth(2)
			hit.draw(winPlayer)
		else:
			missListComp.append(shot)
			print('The Computer missed!')
			row = shot[0]
			column = shot[1]
			miss = Circle(Point(((row-1)*50) + 25, ((column-1)*50) + 25), 20)
			miss.setFill('blue')
			miss.setWidth(2)
			miss.draw(winPlayer)
						
# This will check if any of the Computer's ships have sank.

def shipCheck():
	for ship in shipListComp:
		x = 0
		for spot in ship:
			if spot not in hitListPlayer:
				x += 1
		if x == 0:
			print('You have sunk ComputerShip{}!'.format(shipListComp.index(ship) + 1))
			CSdrawn = Oval(Point((ship[0][0]-1)*50,(ship[0][1]-1)*50), Point((ship[-1][0])*50, (ship[-1][1])*50))
			CSdrawn.setFill('gray')
			CSdrawn.draw(winOpp)
			for spot in ship:
				hit = Circle(Point(((spot[0]-1)*50) + 25, ((spot[1]-1)*50) + 25), 20)
				hit.setFill('red')
				hit.setWidth(2)
				hit.draw(winOpp)
		
# This will determine the winner, and if there is no winner, will return 'No Winner'.

def getWinner():
	if len(hitspotsC) == len(hitListPlayer):
		return 'Player'
	elif len(hitListComp) == len(hitspots):
		return 'Computer'
	else:
		return 'No Winner'
		
# These are the main functions, which will run the easy version or harder version of the game depending on input.		
		
def Easy():
	print('Place your ships!')
	print('Place ship1 (length 2)')
	placeS1()
	print('Place ship2 (length 3)')
	placeS2()
	print('Place ship3 (length 3)')
	placeS3()
	print('Place ship4 (length 4)')
	placeS4()
	print('Place ship5 (length 5)')
	placeS5()
	print('You have placed your ships!')
	placeCS1()
	placeCS2()
	placeCS3()
	placeCS4()
	placeCS5()
	print('The computer has placed its ships!')
	while getWinner() == 'No Winner':
		playerShot()
		shipCheck()
		if getWinner() == 'No Winner':
			time.sleep(.5)
			compShot()
	if getWinner() == 'Player':
		print('You sank all of the Computer\'s ships!')
		print('You Win!!')
	else:
		print('The Computer sank all of your ships!')
		print('You Lose... :(')
		
	input('Hit Enter to quit')

def Medium():
	print('Place your ships! (In Player Window)')
	print('Place ship1 (length 2)')
	placeS1()
	print('Place ship2 (length 3)')
	placeS2()
	print('Place ship3 (length 3)')
	placeS3()
	print('Place ship4 (length 4)')
	placeS4()
	print('Place ship5 (length 5)')
	placeS5()
	print('You have placed your ships!')
	placeCS1()
	placeCS2()
	placeCS3()
	placeCS4()
	placeCS5()
	print('The computer has placed its ships!')
	while getWinner() == 'No Winner':
		playerShot()
		shipCheck()
		if getWinner() == 'No Winner':
			time.sleep(.5)
			compShotM()
	if getWinner() == 'Player':
		print('You sank all of the Computer\'s ships!')
		print('You Win!!')
	else:
		print('The Computer sank all of your ships!')
		print('You Lose... :(')
		
	input('Hit Enter to quit')
	
def Hard():
	print('Place your ships! (In Player Window)')
	print('Place ship1 (length 2)')
	placeS1()
	print('Place ship2 (length 3)')
	placeS2()
	print('Place ship3 (length 3)')
	placeS3()
	print('Place ship4 (length 4)')
	placeS4()
	print('Place ship5 (length 5)')
	placeS5()
	print('You have placed your ships!')
	placeCS1()
	placeCS2()
	placeCS3()
	placeCS4()
	placeCS5()
	print('The computer has placed its ships!')
	while getWinner() == 'No Winner':
		playerShot()
		shipCheck()
		if getWinner() == 'No Winner':
			time.sleep(.5)
			compShotH()
	if getWinner() == 'Player':
		print('You sank all of the Computer\'s ships!')
		print('You Win!!')
	else:
		print('The Computer sank all of your ships!')
		print('You Lose... :(')
		
	input('Hit Enter to quit')

def Impossible():
	print('Place your ships! (In Player Window)')
	print('Place ship1 (length 2)')
	placeS1()
	print('Place ship2 (length 3)')
	placeS2()
	print('Place ship3 (length 3)')
	placeS3()
	print('Place ship4 (length 4)')
	placeS4()
	print('Place ship5 (length 5)')
	placeS5()
	print('You have placed your ships!')
	placeCS1()
	placeCS2()
	placeCS3()
	placeCS4()
	placeCS5()
	print('The computer has placed its ships!')
	while getWinner() == 'No Winner':
		playerShot()
		shipCheck()
		if getWinner() == 'No Winner':
			time.sleep(.5)
			compShotI()
	if getWinner() == 'Player':
		print('You sank all of the Computer\'s ships!')
		print('You Win!!')
	else:
		print('The Computer sank all of your ships!')
		print('You Lose... :(')
		
	input('Hit Enter to quit')
			
# Now to run the game.	

def main():
	if wantPlay() in ['Y', 'y']:
		level = pickLevel()
		if level in ['E', 'e']:
			Easy()
		elif level in ['M', 'm']:
			Medium()
		elif level in ['H', 'h']:
			Hard()
		elif level in ['I', 'i']:	
			Impossible()
		print('I hope you enjoyed the game! Thanks for playing!')
	else: 
		print('Thanks anyway!')
		
main()