class Node(object):

	def __init__(self, data, next_node = None):
		self._data = data
		self._next = next_node

	@property
	def next(self):
		return self._next

	@next.setter
	def next(self, next_node):
		self._next = next_node

	@property
	def data(self):
		return self._data

	@data.setter
	def data(self, value):
		self._data = value

class LinkedList(object):

	def __init__(self, node = None):
		self._head = node
		
	def ListInsert(self, item):
		item.next = self._head
		self._head = item

	def ListDelete(self, value):
		del_node = self.ListSearch(value)

		if del_node == None:
			raise
		else:

	def ListSearch(self, value):
		Node = self._head

		while Node:
			if Node.value == value:
				return Node
			Node = Node.next

		return None

linekd_list = LinkedList()