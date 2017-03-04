class QuickSort(object):

	def __init__(self, unorder = []):
		self._list = unorder
		self._size = len(unorder) - 1

	def quickSort(self):
		self.sorting(0, self._size)

	def sorting(self, start, end):
		if start < end:
			q = self.partition(start, end)
			self.sorting(start, q - 1)
			self.sorting(q + 1, end)

	def partition(self, start, end):
		x = self._list[end]
		i = start - 1
		for j in range(start, end):
			if self._list[j] <= x:
				i += 1
				self._list[i], self._list[j] = self._list[j], self._list[i]

		self._list[i + 1], self._list[end] = self._list[end], self._list[i + 1]
		return i + 1

	def print_list(self):
		print(self._list)



qs = QuickSort([2, 8, 7, 1, 3, 5, 6, 4])
qs.quickSort()
qs.print_list()
