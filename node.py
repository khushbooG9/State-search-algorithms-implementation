

class Node:
	nodeid = 0

	def __init__(self, board):
		global nodeid
		self.RGBBoard = board
		self.operator = None
		self.parent = None
		self.next = None
		Node.nodeid+=1
		self.cost = 0

	def __eq__(self, temp):
		return isinstance(temp, Node) and self.RGBBoard == temp.getboard()

	def __ne__(self, temp):
		return not self.__eq__(temp)

	def setparent(self, p):
		self.parent = p

	def getparent(self):
		return self.parent

	def setnext(self, n):
		self.next = n

	def getnext(self):
		return self.next

	def setoperator(self, o):
		self.operator = o

	def getoperator(self):
		return self.operator

	def setcost(self, c):
		self.cost = c

	def getcost(self):
		return self.cost

	def setheuristic(self, h):
		self.Hval = h

	def getheuristic(self):
		return self.Hval

	def getboard(self):
		return self.RGBBoard

	def getnodeid(self):
		return self.nodeid

	def __hash__(self):
		
		return __hash__(str(self.RGBBoard))





