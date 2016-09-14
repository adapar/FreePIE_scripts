def update():
	global gy
	global dy
	global y

	gy = tobiiEyeX.gazePointInPixelsY
	dy = gy - y
	y = gy

	mouse.deltaX = 0
	mouse.deltaY = dy
	
if starting:
	y = tobiiEyeX.gazePointInPixelsY
	gy = 0
	dy = 0
	
diagnostics.watch(tobiiEyeX.gazePointInPixelsY)
diagnostics.watch(y)
diagnostics.watch(gy)
diagnostics.watch(dy)
