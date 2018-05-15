# receives a path to the matrix file as an argument and calls Adjacent class
from termcolor import colored
import sys, os.path


class Adjacent:
	"""This class receives the path to a file containing a matrix and
		outputs the resulting groups of adjacencies in said matrix"""
	def __init__(self, fname):
		"""Method used to initialise attributes and call other necesary methods"""
		self.grid = self.read_from_file(filename=fname)
		# find size
		self.grid_y = len(self.grid)
		self.grid_x = len(self.grid[0])
		self.explored = []
		self.group = []
		self.find_adjacent()

	def explore_node(self, nx, ny):
		"""Method used to explore recursively a given node in the matrix

		:param nx: node x position (column)
		:param ny: node y position (line)

		"""
		if not [ny, nx] in self.explored:   # verify if has already been explored
			self.explored.append([ny, nx])  # add to explored nodes
			self.group.append([ny, nx])     # add to group

			if ny < self.grid_y-1:  # can be explored vertically

				if self.grid[ny+1][nx]:  # vertical adjacency
					self.explore_node(nx=nx, ny=ny + 1)

			if nx == 0:  # can only be explored front

				if self.grid[ny][nx+1]:  # horizontal adjacency front
					self.explore_node(nx=nx + 1, ny=ny)

			if 0 < nx < self.grid_x - 1:  # can be explored front and back

				if self.grid[ny][nx-1]:   # horizontal adjacency back
					self.explore_node(nx=nx - 1, ny=ny)

				if self.grid[ny][nx+1]:   # horizontal adjacency front
					self.explore_node(nx=nx + 1, ny=ny)

	def find_adjacent(self):
		"""Method used to iterate over the matrix nodes
			and explore the ones with value equal to 1"""
		for y in range(self.grid_y):
			for x in range(self.grid_x):
				if self.grid[y][x] and not [y, x] in self.explored:  # has value (one) and not explored
					self.explore_node(nx=x, ny=y)
					self.group.sort()
					if len(self.group) > 1:
						print(self.group)
					self.group = []

	def read_from_file(self, filename):
		"""Method used to read a 2D-matrix from a file

			:param filename: path to file
			:returns matrix read from file
		"""
		matrix = []
		with open(filename, 'r') as file:
			for line in file:
				line = line.strip()
				if '[' in line and ']' in line:
					lst = []
					for elem in line:
						if elem.isdigit():
							lst.append(int(elem))
					matrix.append(lst)
		return matrix


if __name__ == '__main__':

	if len(sys.argv) != 2:
		print(colored("USAGE: python3 challengeB.py <filename>", 'red'))
		exit(0)

	if os.path.isfile(sys.argv[1]):
		Adjacent(fname=sys.argv[1])
	else:
		print(colored("ERROR: file not found or is a directory", 'red'))

