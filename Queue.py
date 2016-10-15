class Queue(object):

	def __init__(self):
		self._queue = []

	def Enqueue(self, item):
		self._queue.append(item):

	def Dequeue(self):
		return self.queue.pop(0)