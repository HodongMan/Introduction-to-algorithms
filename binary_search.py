class Node(object):

	def __init__(self, data):
		self._parent = None
		self._left = None
		self._right = None
		self._data = data

	@property
	def parent(self):
		return self._parent

	@parent.setter
	def parent(self, p):
		self._parent = p

	@property
	def left(self):
		return self._left

	@left.setter
	def left(self, l):
		self._left = l

	@property
	def right(self):
		return self._right

	@right.setter
	def right(self, r):
		self._right = r

	@property
	def data(self):
		return self._data
	
	@data.setter
	def data(self, value):
		self._data = value


class BinaryTree(object):

	def __init__(self, root = None):
		self._root = None

	def InorderTreeWalk(self, x):
		if x is not None:
			self.InorderTreeWalk(x.left)
			print(x)
			self.InroderTreeWalk(x.right)
		
	def InorderTreeStart(self):
		self.InorderTreeWalk(self._root)

	def TreeSearchStart(self, value):
		self.TreeSearch(self, x, value)

	def TreeSearch(self, x, value):
		if x is None or x.data is value:
			return x
		if value < x.data:
			return self.TreeSearch(x.left, value)
		return self.TreeSearch(x.right, value)

	def FindTreeMinimum(self):
		self.TreeMinimum(self, x)

	def TreeMinimum(self, x):
		while x.left is not None:
			x = x.left
		return x

	def FindTreeMaximum(self):
		self.TreeMaximum(self, x)

	def TreeMaximum(self, x):
		while x.right is not None:
			x = x.right
		return x



if __name__ == "__main__":
	bt = BinaryTree()
