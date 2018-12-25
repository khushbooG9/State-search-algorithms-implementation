import math as m
from node import *
import copy as cp
import sys 

def setgoalboard(filename):
	try:
		ifile = open(filename, "r")
		goalboard =[]
		for line in ifile:
			line = line.split()
			for c in line:
				goalboard.append(c)
		ifile.close()
		return goalboard
	except FileNotFoundError:
		print("You have given wrong goal file. It doesnt exist.")
		sys.exit(0)

def setinitialboard(filename):
	try:
		ifile = open(filename, "r")
		fboard = []
		for line in ifile:
			line = line.split()
			for c in line:
				fboard.append(c)
		ifile.close()
		newnode = Node(fboard)
		return newnode
	except FileNotFoundError:
		print("You have given wrong problem file. It doesnt exist.")
		sys.exit(0)

def printboard(board):
		
	size = len(board)
	lines = m.sqrt(size)
	for i in range(size):
		print(board[i], end=" ")
		if((i+1)%lines == 0):
			print(" \n")
	print(" \n")

def setOpr():
	Opr = list()
	Opr.append("Up")
	Opr.append("Down")
	Opr.append("Left")
	Opr.append("Right")
	return Opr

def testgoal(board, goal):
	return board.__eq__(goal)

def Solution(temp, filename):
	if (temp.getparent()==None) or (temp.getnodeid() == 1):
		print("Initial board is actually the Goal board \n")

	else:
		oper = str()
		i = 0
		current = cp.deepcopy(temp)
		print("Printing solution to file")
		while(current.getparent() != None):
			o = current.getoperator()

			oper = oper + o[0]
			current = current.getparent()

		output = str(oper[::-1])
		with open(filename, "w") as sol_file:
			for o in output:
				sol_file.write(o + "\n")
                
def lookBlank(board):
	size = len(board)
	l = m.sqrt(size)
	loc = []
	row =0
	col = 0
	for i in range(size):
		col = i%l
		if board[i] == "B":
			loc.append(int(row))
			loc.append(int(col))
			break
		if ((i+1)%l) == 0:
			row = row+1
	#print(loc)
	return loc

def updateboard(board, oper):
	childboard = cp.deepcopy(board)
	loc = lookBlank(board)
	size = len(board)
	l = m.sqrt(size)
	t = []
	if oper == "Up":
		t = childboard[int((loc[0]*l)+loc[1])]
		childboard[int((loc[0]*l)+loc[1])] = board[int((loc[0]*l)+(loc[1]-l))]
		childboard[int((loc[0]*l)+(loc[1]-l))] = t

	elif oper == "Down":
		t = childboard[int((loc[0]*l)+loc[1])]
		childboard[int((loc[0]*l)+loc[1])] = board[int((loc[0]*l)+(loc[1]+l))]
		childboard[int((loc[0]*l)+(loc[1]+l))] = t

	elif oper == "Left":
		t = childboard[int((loc[0]*l)+loc[1])]
		childboard[int((loc[0]*l)+loc[1])] = board[int((loc[0]*l)+(loc[1]-1))]
		childboard[int((loc[0]*l)+(loc[1]-1))] = t

	else:
		t = childboard[int((loc[0]*l)+loc[1])]
		childboard[int((loc[0]*l)+loc[1])] = board[int((loc[0]*l)+(loc[1]+1))]
		childboard[int((loc[0]*l)+(loc[1]+1))] = t

	return childboard


def validmoves(board, oper):
	loc = list()
	loc = lookBlank(board)
	size = len(board)
	l = m.sqrt(size)

	if oper == "Up":
		if loc[0] == 0:
			return False
		else:
			return True

	elif oper == "Down":
		if loc[0] == (l-1):
			return False
		else:
			return True

	elif oper == "Left":
		if loc[1] == 0:
			return False
		else:
			return True

	else:
		if loc[1] == (l-1):
			return False
		else:
			return True








	

