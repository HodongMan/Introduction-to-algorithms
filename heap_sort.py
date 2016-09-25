class Heap(object):

	def __init__(self, data = []):
		self._heap = data
		self.heap_size = len(data)
	def parent(self, i):
		return i // 2

	def left(self, i):
		return (2 * i) + 1

	def right(self, i):

		return (2 * i) + 2

	def max_heapify(self, i):
		l = self.left(i)
		r = self.right(i)
		if l < self.heap_size and self._heap[l] > self._heap[i]:
			largest = l
		else:
			largest = i
		if r < self.heap_size and self._heap[r] > self._heap[largest]:
			largest = r

		if largest != i:
			self._heap[i], self._heap[largest] = self._heap[largest], self._heap[i]
			self.max_heapify(largest)

	def build_max_heap(self):
		self.heap_size = len(self._heap)
		for i in range(self.heap_size // 2 - 1, -1, -1):
			self.max_heapify(i)

	def print_heap(self):
		print(self._heap)

	def heap_sort(self):
		self.build_max_heap()
		for i in range(len(self._heap) - 1, 0, -1):
			self._heap[0], self._heap[i] = self._heap[i], self._heap[0]
			self.heap_size -= 1
			self.max_heapify(0)

heap = Heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
heap.heap_sort()
heap.print_heap()