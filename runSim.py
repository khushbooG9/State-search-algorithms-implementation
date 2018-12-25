
from bfs import *
from dfs import *
from ids import *
from gbfs import *
from astar import *
from datetime import datetime as dt
from driver import *
#import sys

def runSim(option, initial, final):
	goal = setgoalboard(str(final))
	init = setinitialboard(str(initial))
	print("The puzzle to solve is :")
	printboard(init.getboard())
	print("The goal to reach is")
	printboard(goal)
	if option == 1:
		start = dt.now()
		bfs_solver(init, goal, "BFS-sol.txt")
		end = dt.now()
		time = end - start
		print("Time to run the BFS solver :", time)
	elif option==2:
		start = dt.now()
		dfs_solver(init, goal, "DFS-sol.txt")
		end = dt.now()
		time = end - start
		print("Time to run the DFS solver :", time)
	elif option==3:
		start = dt.now()
		ids_solver(init, goal, "IDS-sol.txt")
		end = dt.now()
		time = end - start
		print("Time to run the IDS solver :", time)
	elif option==4:
		start = dt.now()
		gbfs_solver(init, goal, "GBFS-sol.txt")
		end = dt.now()
		time = end - start
		print("Time to run the GBFS solver :", time)
	elif option==5:
		start = dt.now()
		astar_solver(init, goal, "ASTAR-sol.txt")
		end = dt.now()
		time = end - start
		print("Time to run the ASTAR solver :", time)
	elif option==0:
		sys.exit()
	else:
		print(" Wrong choice!!")

