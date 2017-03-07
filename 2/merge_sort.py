import sys

class MergeSort(object):

	def __init__(self):
		
		self._data = list()

	def setData(self, data):
		
		self._data = data
	
	def printData(self):

		print(self._data)

	def merge(self, p, q, r):

		n1 = q - p
		n2 = r - q

		Larray = self._data[p:p+n1]
		Rarray = self._data[q:q+n2]

		Larray.append(sys.maxsize)
		Rarray.append(sys.maxsize)

		i, j = 0, 0
		
		
		for k in range(p, r):
			if Larray[i] <= Rarray[j]:
				self._data[k] = Larray[i]
				i += 1
			else:
				self._data[k] = Rarray[j]
				j += 1
		"""
		self.printData()
		"""
	def mergeSort(self, p, r):
		if p < r:
			q = (p + r) // 2
			
			self.mergeSort(p, q)
			self.mergeSort(q + 1, r)
			
			self.merge(p, q, r)

	def sort(self):
		self.mergeSort(0, len(self._data))




ms = MergeSort()
ms.setData([5, 2, 4, 7, 1, 3, 2, 6])
ms.sort()
ms.printData()
