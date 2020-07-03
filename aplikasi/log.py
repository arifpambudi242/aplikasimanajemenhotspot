import logging


class Log:
	def __init__(self):
		self.log = logging
		self.log.basicConfig(format='[%(asctime)s] : %(message)s', datefmt='%d/%m/%Y %H:%M:%S', filename='mikhotman.log')

	def message(self, msg=None):
		self.log.warning(msg)


log = Log()