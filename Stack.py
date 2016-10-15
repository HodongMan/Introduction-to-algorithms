class Stack(object):

	def __init__(self):
		self._stack = []

	def StackEmpty(self):
		if len(self._stack) == 0:
			return True
		return False

	def Push(self, item):
		self._stack.append(item)

	def Pop(self):
		if self.StackEmpty():
			raise
		return self._stack.pop()
