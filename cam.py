# -*- coding utf-8 -*-

import cv2
import time
import subprocess

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import *
from webcam_ui import Ui_MainWindow

#usb camera Inti
cam = cv2.VideoCapture(0)

#camera setting Init 
#focuse min = 0, max = 255, default = 20
#exposure min = 3, max = 2047, default = 250
focuse = 20
exposure = 250

#camera capture bool
cap = False

frame = cam.read()

#linux shll command USB cam dev focus auto stop value input

try:
	subprocess.check_call("v4l2-ctl -d /dev/video0 -c focus_auto=0",shell=True)
except subprocess.CalledProcessError as e:
    raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    
class MainWindow(Ui_MainWindow):
	
	def __init__(self, w):
		Ui_MainWindow.__init__(self)
		self.setupUi(w)

		#QTimer start webcam
		self.timer = QTimer(w)
		self.timer.timeout.connect(self.webcam)
		self.timer.start(1)

		#button click event
		self.capture.clicked.connect(self.captures)
		self.exposedDown.clicked.connect(self.exposurDowns)
		self.exposedUp.clicked.connect(self.exposurUps)
		self.focuseUp.clicked.connect(self.focusesUps)
		self.focuseDown.clicked.connect(self.focuseDowns)



	def webcam(self):
		#exposure & focuse setting 
		global exposure , focuse , frame

		#linux cam exposure & focuse set shell command str
		shellExposure = "v4l2-ctl -d /dev/video0 -c exposure_absolute=" + str(exposure)
		shellFocuse = "v4l2-ctl -d /dev/video0 -c focus_absolute=" + str(focuse)

		print(shellExposure)
		print(shellFocuse)

		
		#linux shll command focuse & exposure value input
		
		try:
			subprocess.check_call(shellFocuse,shell=True)
			subprocess.check_call(shellExposure,shell=True)
		except Exception as e:
			raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
		

		#usb webcam frame read variable
		ret, frame = cam.read()

		#usb webcam frame x, z, BGR 
		cv_h, cv_w, cv_color = frame.shape
		
		#video view size / usb webcam frame size
		scale_w = float(self.video.frameSize().width())		/ 	float(cv_w)
		scale_h = float(self.video.frameSize().height())	/ 	float(cv_h)
		scale = min([scale_w,scale_h])

		if scale == 0 :
			scale = 1

		#usb webcam frame resize & BGR -> RGB
		frame = cv2.resize(frame, None, fx = scale, fy = scale, interpolation = cv2.INTER_CUBIC)
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

		#resize webcam x, y, color
		height, width, color = frame.shape
		bytesPerLine = color * width

		#image Reverse
		frame = cv2.flip(frame,1)

		#QImage in resize webcam frame 
		qImg = QImage(frame.data ,width ,height , bytesPerLine,QImage.Format_RGB888)

		#video show usb webcam 
		self.video.setPixmap(QPixmap(qImg))

		# image save in saveimage  
		self.saveImage()


	# exposuer+ button click event
	def exposurUps(self):
		global exposure
		if exposure < 2047:
			exposure = exposure + 10
			print('exposure up')
		else:
			print('exposure value max')

		if exposure > 2047:
			exposure = 2047

	# exposuer- button click event
	def exposurDowns(self):
		global exposure
		if exposure > 3:
			exposure = exposure - 10
			print('exposure down')
		else: 
			print('exposure value min')

		if exposure < 3:
			exposure = 3

	# focuse+ button click event
	def focusesUps(self):
		global focuse
		if focuse < 255:
			focuse = focuse 	+ 5
			print('focuse up')
		else :
			print('focuse value max')

	# focuse- button click event
	def focuseDowns(self):
		global focuse
		if focuse > 0:
			focuse = focuse 	- 5
			print('focuse down')
		else :
			print('focuse value min')

	#capture button click event
	def captures(self):
		global cap

		#enable
		cap = True

	#image save
	def saveImage(self):
		global cap, frame
		if cap == True:
			#get time
			getTime = time.localtime()

			#BGR -> RGB
			frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

			#local & Image name (time year-mon-day hour:min:sec)
			local = "saveimage/" 
			img = "%04d-%02d-%02d %02d:%02d:%02d.jpg" % (getTime.tm_year, getTime.tm_mon, getTime.tm_mday, getTime.tm_hour, getTime.tm_min, getTime.tm_sec)

			#save local and name
			cv2.imwrite(local+img,frame)

			#enable
			cap = False



#main UI Open
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = MainWindow(w)
    w.show()
    sys.exit(app.exec_())

