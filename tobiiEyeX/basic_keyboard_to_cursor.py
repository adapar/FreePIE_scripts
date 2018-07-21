#if keyboard.getPressed(Key.Q):
#	mouse.normalizedX = 0.1
#	mouse.normalizedY = 0.1
#elif keyboard.getPressed(Key.P):
#	mouse.normalizedX = 0.9
#	mouse.normalizedY = 0.1
#elif keyboard.getPressed(Key.Z):
#	mouse.normalizedX = 0.9
#	mouse.normalizedY = 0.9
#elif keyboard.getPressed(Key.M):
#	mouse.normalizedX = 0.1
#	mouse.normalizedY = 0.9
def update():
	global left
	
	diagnostics.debug("moving")
	diagnostics.debug(left)
	
	if left:
		mouse.deltaX = 10
	
	left = False
	
if starting:
	#mouse.normalizedX = 0.5
	#mouse.normalizedY = 0.5
	cursor.posX = 800
	cursor.posY = 700
	left = False

if keyboard.getPressed(Key.M):
	left = True
	
diagnostics.watch(mouse.normalizedX)
diagnostics.watch(mouse.normalizedY)
diagnostics.watch(mouse.deltaX)
diagnostics.watch(mouse.deltaY)
diagnostics.watch(cursor.posX)
diagnostics.watch(cursor.posY)
