if keyboard.getPressed(Key.Q):
	cursor.posX = 100
	cursor.posY = 100
elif keyboard.getPressed(Key.P):
	cursor.posX = 1000
	cursor.posY = 100
elif keyboard.getPressed(Key.Z):
	cursor.posX = 1000
	cursor.posY = 700
elif keyboard.getPressed(Key.M):
	cursor.posX = 100
	cursor.posY = 700
		
if starting:
	cursor.posX = 456
	cursor.posY = 654
	
diagnostics.watch(cursor.posX)
diagnostics.watch(cursor.posY)
