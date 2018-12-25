from node import *
from driver import *


def bfs_solver(node, goal, filename):
	operator = []
	operator = setOpr()
	nodesexplored = 0
	nodesgenerated = 0   
	current = node
	Q = []
	Q.append(node)
	if testgoal(current.getboard(), goal):
		Solution(current, filename)
		return True
	else:
		explored = dict()
		while(True):
			if not Q:
				return False

			current = Q.pop(0)
			explored[current.getnodeid()] = current.getboard()
			nodesexplored=nodesexplored+1
			for i in range(4):
				if validmoves(current.getboard(), operator[i]):
					board = updateboard(current.getboard(), operator[i])
					child = Node(board)
					child.setparent(current)
					child.setoperator(operator[i])
					nodesgenerated=nodesgenerated+1
					
					if  (child.getboard() in explored.values()) != True:
						if testgoal(child.getboard(),goal):
							Solution(child, filename)
							printboard(child.getboard())
							print("Nodes generated  :", nodesgenerated)
							print("Nodes explored  :", nodesexplored)
							return True
						Q.append(child)

					



