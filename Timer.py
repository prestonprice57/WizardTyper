import time

class Timer(object):
	"""Simple timer class.  Allows for start and stop time and reporting of elapsed time"""
	def __init__(self):
		self.startTime = 0
		self.endTime = 0
		self.elapsedTime = 0

	def startTimer(self):
		self.startTime = time.time()

	def stopTimer(self):
		self.endTime = time.time()
		self.elapsedTime = self.endTime - self.startTime
