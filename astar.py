from node import *
from driver import *

def greedyH(board, goal):
	size = len(board)
	hval = 0
	for i in range(size):
		if board[i] != "B":
			if board[i] != goal[i]:
				hval = hval +1
	return hval

def prioritylist(dic):
	return sorted(dic.items(), key=lambda kv: kv[0])

def astar_solver(node, goal, filename):
	operator = []
	operator = setOpr()
	nodesexplored = 0
	nodesgenerated = 0   
	current = node
	current.setheuristic(greedyH(node.getboard(),goal))
	PQ = dict()
	PQ[(current.getheuristic()+current.getcost())] = node
	if testgoal(current.getboard(), goal):
		solution(current, filename)
		return True
	else:
		explored = dict()
		count = 0
		while(True):
			if not PQ:
				return False
			PQlist = prioritylist(PQ)
			current = PQlist[0][1]
			del PQ[(current.getheuristic()+current.getcost())]
			explored[current.getnodeid()] = current.getboard()
			nodesexplored +=1

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
					cost = current.getcost()+1
					#f = current.getheuristic() + current.getcost()
					#child.setcost(cost)
					nodesgenerated=nodesgenerated+1
					if (child.getboard() in explored.values())==False:
						if (child in PQ.values())==False:
							PQ[(child.getheuristic()+child.getcost())] = child
						else:
							temp = child
							#if (temp.getheuristic()+temp.getcost()) <=f :
							if cost<temp.getcost():
								temp.setcost(cost)
								temp.setparent(current)
								temp.setheuristic(greedyH(board, goal))
								temp.setoperator(operator[i])
								del PQ[(child.getheuristic()+child.getcost())]
								PQ[(temp.getheuristic()+temp.getcost())] = temp
								print(count)
								count +=1




    