""" Main to initialize the project """
from runSim import *



if __name__ == "__main__":
	print("We have 5 options to solve the RGB puzzle : \n")
	print("1. Breadth First Search \n")
	print("2. Depth First Search \n")
	print("3. Iterative Deepening Search \n")
	print("4. Greedy Best First Search \n")
	print("5. A* Search \n")
	print("Select Problem no.(1 -5) to solve or type 0 to exit :\n")
	problem = int(input())
	puzzle = input("Give the filename of the RGB puzzle you want to solve :\n")
	finalstate = input("Enter the filename to setup goalstate: \n")
	runSim(problem, puzzle, finalstate)
