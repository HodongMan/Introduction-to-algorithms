class InsertionSort(object):

	def __init__(self):
		self._data = list()

	def setData(self, data_list):
		self._data = data_list

	def sort(self):
		for j, item in enumerate(self._data):
			key = self._data[j]
			i = j - 1

			while i >= 0 and self._data[i] > key:
				self._data[i+1] = self._data[i]
				i -= 1

			self._data[i+1] = key

	def printData(self):
		print(self._data)

Is = InsertionSort()
Is.setData([5, 2, 4, 6, 1, 3])
Is.sort()
Is.printData()
