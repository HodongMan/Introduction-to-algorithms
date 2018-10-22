class BinaryAdd(object):

	def __init__(self):
		self._result = list()
	
	def add(self, list1, list2):
		carry = 0

		for index, item in enumerate(list1):
			self._result.append( ( item + list2[index] + carry ) % 2 )
			carry = ( item + list2[index] + carry ) // 2
			print(self._result[index], carry)

		self._result.append(carry)

	def printData(self):
		print(self._result)

ba = BinaryAdd()
ba.add([1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1])
ba.printData()
			
