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
			print(x.data)
			self.InorderTreeWalk(x.right)
		
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
	
	def TreeSuccessor(self, x):
		if x.right is not None:
			return self.TreeMinimum(x.right)
		y = x.parent
		while y is not None and x == y.right:
			x = y
			y = y.parent
		return y

	def TreeInsert(self, z):
		y = None
		x = self._root
		while x is not None:
			y = x
			if z.data < x.data:
				x = x.left
			else:
				x = x.right
		z.p = y
		if y == None:
			self._root = z
		elif z.data < y.data:
			y.left = z
		else:
			y.right = z
	
	def Translate(self, x, y):
		if x.parent is None:
			self._root = y
		elif x == x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y
		if y is not None:
			y.parent = x.parent

	def TreeDelete(self, z):
		if z.left is None:
			self.Translate(z, z.right)
		elif z.right is None:
			self.Translate(z, z.left)
		else:
			y = self.TreeMinimum(z.right)
			if y.p is not z:
				self.Translate(y, y.right)
				y.right = z.right
				y.right.paret = y
			self.Translate(z, y)
			y.left = z.left
			y.left.parent = y



if __name__ == "__main__":
	bt = BinaryTree()
	bt.TreeInsert(Node(1))
	bt.TreeInsert(Node(2))
	bt.InorderTreeStart()
