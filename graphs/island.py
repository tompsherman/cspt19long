# def island_counter(island_matrix):
#     # keep track of the nodes that I have visited

#     # build the graph

#     # create an island counter and itialize it to zero

#     # keep traversing the graph, while we still have nodes that we have not visited
#     # walk though each cell in the matrix
#         # if that the current cell has not been visited
#             # check if it is a 1.
#                 # do some sort of a traversal marking each connected node as visited
#                 # increment the island counter by 1

#     pass

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

class Stack:
    def __init__(self):
        self.storage = []

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        return self.storage.pop()

    def size(self):
        return len(self.storage)

def get_neighbors(row, col, island_matrix):
    neighbors = []
    #check north:
    if row > 0 and island_matrix[row - 1][col] == 1:
        neighbors.append((row - 1, col))

    #check west:
    if col > 0 and island_matrix[row][col - 1] == 1:
        neighbors.append((row, col - 1))

    #check south:
    if row < len(island_matrix)-1 and island_matrix[row + 1][col] == 1:
        neighbors.append((row + 1, col))
    
    #check east:
    if col < len(island_matrix[0])-1 and island_matrix[row][col + 1] == 1:
        neighbors.append((row, col + 1))

    return neighbors

def dft(row, col, island_matrix, visited_matrix):
    # create an empty stack
    s = Stack()
    # push starting vertex on the stack (row, col)
    s.push((row, col))
    # while the stack is not empty
    while s.size() > 0:
        # pop the vertex off the stack
        v = s.pop()
        # extract the row and col
        row = v[0]
        col = v[1]
        # if the current element is not in visited 
        if not visited_matrix[row][col]:
            # set the element to visited
           visited_matrix[row][col] = True
           
           # iterate over the neighbors:
           for neighbor in get_neighbors(row, col, island_matrix):
                # push the neighbor on to the stack
                s.push(neighbor)

    # return the visited matrix to the caller
    return visited_matrix


def island_counter(islands):
    # create a visited matrix (2d list)
    visited = []
    # initialize the visited matrix with false's
    for i in range(len(islands)):
        visited.append([False] * len(islands[0]))
    # initialize an island_count to zero
    island_count = 0
    # walk through the matrix via a nested for loop
    # columns 
    for col in range(len(islands[0])):
        # rows
        for row in range(len(islands)):
            # check if matrix at current r & c are in visited (is it "true"?)
            if not visited[row][col]:
                # check if current element is a 1
                if islands[row][col] == 1:
                    # do a dft on the island_matrix, returning an updated copy of the visited matrix
                    visited = dft(row, col, islands, visited)
                    # increment the island_count
                    island_count +=1
                else:
                    visited[row][col] = True

    return island_count

print(island_counter(islands)) # returns 4

# 1.: what are verts and edges 
# 1s are vertices, n/s/w/e are edges