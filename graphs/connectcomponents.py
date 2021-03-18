# in a disjoint graph, groups of nodes on a graph are not connected to each other
# solved by breadth first search graph
#   has it been explored?
#       if NO:
#           -breadth first search
            # at end, all nodes connected
#       if YES:
#           - already in a connected component
            # skip it, go to next node
# Nodes = [0,1,2,3,4,5]

#  0       1 -- 3
# / \       
#4   5         2

"""
go to node 0 first, 
    do bft, 
    change toggle trigger (true / false, colors, etc.) from on to off, 
    go to next node
        repeat

Strongly connected components
    - analyzes direction of connections to understand strength between components

we cna use 

BFS or DFS algorithms can be used to find connected components

"""
