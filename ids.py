from node import *
from driver import *

ne =0
ng =0 
def R_depthlsearch(node, depth, goal):
	global ne
	global ng
	operator = setOpr()
	if depth == 0:
		return node

	ne = ne+1
	if testgoal(node.getboard(), goal):
		return node
	else:
		for i in range(4):
			if validmoves(node.getboard(), operator[i]):
				board = updateboard(node.getboard(), operator[i])
				child = Node(board)
				child.setparent(node)
				child.setoperator(operator[i])
				ng=ng+1
				result = R_depthlsearch(child, depth-1, goal)
				if testgoal(result.getboard(),goal):
					return result
		return node

def ids_solver(node,  goal, filename):
	global ne
	global ng
	for i in range(1,100):
		result = R_depthlsearch(node, i, goal)
		print("At depth :", i)
		if testgoal(result.getboard(), goal):
			Solution(result, filename)
			printboard(result.getboard())
			print("Nodes generated  \n", ne)
			print("Nodes explored \n", ng)
			return True
	return False

