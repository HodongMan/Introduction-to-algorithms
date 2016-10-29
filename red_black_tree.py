class Node(object):

	def __init__(self, data = None):
		self.parent = None
		self.left = None
		self.right = None
		self.data = data
		self.color = None


class RedBlackTree(object):

	def __init__(self):
		self.root = None
	
	def LeftRotate(self, node):
		y = node.right
		node.right = y.left
		if y.left is not None:
			y.left.parent = node
		y.parent = node.parent
		if node.parent is None:
			self.root = y
		elif node == node.parent.left:
			node.parent.left = y
		else:
			node.parent.left = y
		y.left = node
		node.parent = y

	def RBInsert(self, node):
		y = None
		x = self.root

		while x is not None:
			y = x
			if node.value < x.value:
				x = x.left
			else:
				x = x.right
		
		node.parent = y
		if y is None:
			self.root = Node
		elif node.key < y.key:
			y.left = node
		else:
			y.right = node

		node.left = None
		node.right = None
		node.color = "RED"

		self.RBInsertFixup(node)

	def RBInsertFixup(self, node):
		while node.parent.color == "RED":
			if node.parent == node.parent.parent.left:
				y = node.parent.parent.right
				if y.color == "RED":
					node.parent.color = "BLACK"
					y.color == "RED"
					node.parent.parent.color = "RED"
					node = node.parent.parent

				elif node == node.parent.right:
					node = node.parent
					self.LeftRotete(node)
				node.parent.color = "BLACK"
				node.parent.parent.color = "RED"
				self.RightRotate(node.parent.parent)
			else:
				pass
		self.root.color = "BLACK"

