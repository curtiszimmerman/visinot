#!/usr/bin/python
"""Visinot is VISItor NOTification using a camera source, SimpleCV/OpenCV, and Twilio or AWS SNS.
"""
##
# @project Visinot
# VISItor NOTification system using a camera source, SimpleCV/OpenCV, and Twilio or AWS SNS.
# @file visinot.py
# Primary application driver.
# @author curtis zimmerman
# @contact software@curtisz.com
# @license GPLv3
# @version 0.0.1a

##
# @plan take picture every half second, compare to LAST image taken, and compare to image from
# one minute ago (or ten minutes or one hour). notify via curl on difference. the reference 
# image from one/ten/sixty minutes prior is to prevent very slow-moving people from taking 
# advantage of error margin (like is possible with most motion detection, to move very slowly
# and fool the sensor since its reference image doesn't change enough to trigger it)

__version__ = "0.0.1a"

def notify( image ):
	return 0

def main():
	from SimpleCV import Camera, Color, Display, Image
	import time

	# initialize camera

	# while forever:
	#	img = cam.getImage()
	#	timestamp
	#	if (no reference.timestamp):
	#		reference.image = this.image
	#	if (no last.image):
	# 
	#	if (this.timestamp - ten minutes) is greater than reference.timestamp:
	#		reference.image = this.image
	#		last.image = this.image
	#	time.sleep(0.4)

	# init camera with forced dimensions
	cam = Camera(0, {"width": 640, "height": 480})
	# live camera view
	#cam.live()


	winsize = (640, 480)
	# init display
	display = Display(winsize)

	# capture an Image
	#img = cam.getImage()
	# draw text on image at x, y
	#img.drawText("-=< FOO TEST >=-", 60, 20)
	img = Image(winsize)
	img.save(display)

	print "i launched a winder!"
	# get logo
	#Image("logo").save(display)
	# show image on the scren
	#img.save(display)
	# show image in browser
	#img.show(type="browser")

	# do not close right away
	while not display.isDone():
		#if display.mouseLeft:
		#	img.dl().circle((display.mouseX, display.mouseY), 4, Color.BLUE, filled=True)
		#	img.save(display)
		#	img.save("painting.png")
		#time.sleep(0.1)
		x = random.randint(0,640)
		y = random.randint(0,480)
		img = cam.getImage()
		img.drawText(time.ctime(time.time()), x, y)
		img.save(display)
		img.save("thing.png")
		time.sleep(1)

if __name__ == "__main__":
	main()