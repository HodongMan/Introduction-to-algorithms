class BinaryAdd(object):

	def __init__(self):
		self._result = list()
	
	def add(self, list1, list2):
		self._result = [0]

		for index, item in enumerate(list1):
			self._result.append(item + list2[index])

		for i in range(len(self._result) -1, 0, -1):

			if self._result[i] > 1:
				self._result[i] -= 2
				self._result[i-1] += 1

	def printData(self):
		print(self._result)

ba = BinaryAdd()
ba.add([1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1])
ba.printData()
			
