class SelectionSort(object):

	def __init__(self):

		self._data = list()

	def setData(self, data):

		self._data = data

	def printData(self):

		print(self._data)

	def sort(self):

		for index, item in enumerate(self._data):
			minimum_index = index
			j = index + 1

			while j < len(self._data):
				
				if self._data[j] < self._data[minimum_index]:
					minimum_index = j
				j+= 1

			self._data[index], self._data[minimum_index] = self._data[minimum_index], self._data[index]



			
se = SelectionSort()
se.setData([5, 3, 4, 2, 9, 6])
se.sort()
se.printData()
