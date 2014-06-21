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

from SimpleCV import Camera, Display, Image

# init camera
cam = Camera()

# init display
display = Display()

# capture an Image
img = cam.getImage()

# show picture on the scren
img.save(display)

