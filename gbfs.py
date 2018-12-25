from node import *
from driver import *
from queue import PriorityQueue

class PQ(PriorityQueue):
	def __init__(self):
		PriorityQueue.__init__(self)
		self.counter = 0
	def put(self, item, priority):
		PriorityQueue.put(self, (priority, self.counter, item))
		self.counter +=1  
	def get(self, *args, **kwargs):
		_, _, item = PriorityQueue.get(self, *args, **kwargs)
		return item
	def empty(self):
		return PriorityQueue.empty(self)

#Setting heuristic value based on the fact if a character in board is at the same position as goal
#Low heuristic value means higher priority
def greedyH(board, goal):
	size = len(board)
	hval = 0
	for i in range(size):
		if board[i] != "B":
			if board[i] != goal[i]:
				hval = hval +1
	return hval


def gbfs_solver(node, goal, filename):
	operator = []
	operator = setOpr()
	nodesexplored = 0
	nodesgenerated = 0   
	current = node
	current.setheuristic(greedyH(node.getboard(),goal))
	Q = PQ()
	Q.put(current, current.getheuristic())
	if testgoal(current.getboard(), goal):
		solution(current, filename)
		return True
	else:
		explored = dict()
		while(True):
			if Q.empty()== True:
				return False

			current = Q.get()
			explored[current.getnodeid()] = current.getboard()
			nodesexplored=nodesexplored+1
			if  (current.getboard() in explored.values()) == True:
				if testgoal(current.getboard(),goal):
					Solution(current, filename)
					printboard(current.getboard())
					print("Nodes generated ", nodesgenerated)
					print("Nodes explored ", nodesexplored)
					return True
			for i in range(4):
				if validmoves(current.getboard(), operator[i]):
					board = updateboard(current.getboard(), operator[i])
					child = Node(board)
					child.setparent(current)
					child.setoperator(operator[i])
					child.setheuristic(greedyH(board, goal))
					nodesgenerated=nodesgenerated+1
					if (child.getboard() in explored.values())==False:
						Q.put(child, child.getheuristic())
					#current = child

					



			





