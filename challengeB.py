from termcolor import colored
class Adjacent:
	def __init__(self, grid):
		self.grid = grid
		# find size
		self.grid_y = len(self.grid)
		self.grid_x = len(self.grid[0])
		self.explored = []
		self.group = []
		self.find_adjacent()

	def explore_node(self, nx, ny):

		if not [ny, nx] in self.explored:   #verify if has already been explored
			self.explored.append([ny, nx])  #add to explored nodes
			self.group.append([ny, nx])     #add to group

			if ny <self.grid_y-1: #can be explored vertically

				if self.grid[ny+1][nx]:  #vertical adjacency
					self.explore_node(nx=nx, ny=ny + 1)


			if nx == 0: # can only be explored front

				if self.grid[ny][nx+1]:  #horizontal adjacency front
					self.explore_node(nx=nx + 1, ny=ny)

			if 0 < nx < self.grid_x - 1: #can be explored front and back

				if self.grid[ny][nx-1]:  #horizontal adjacency back
					self.explore_node(nx=nx - 1, ny=ny)

				if self.grid[ny][nx+1]:  #horizontal adjacency front
					self.explore_node(nx=nx + 1, ny=ny)



	def find_adjacent(self):
		# print grid formated
		#for y in range(self.grid_y):
		#	print(self.grid[y])

		for y in range(self.grid_y):
			for x in range(self.grid_x):
				if self.grid[y][x] and not [y, x] in self.explored: # has value (one) and not explored
					self.explore_node(nx=x, ny=y)
					self.group.sort()
					if len(self.group) > 1:
						print(self.group)
					self.group = []


if __name__ == '__main__':
	g = [[0, 0, 0, 1, 0, 0, 1, 1],
	     [0, 0, 1, 1, 1, 0, 1, 1],
	     [0, 0, 0, 0, 0, 0, 1, 0],
	     [0, 0, 0, 1, 0, 0, 1, 1],
	     [0, 0, 0, 1, 0, 0, 1, 1]]


	Adjacent(grid=g)