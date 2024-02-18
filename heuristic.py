from collections import defaultdict
  
# This class represents a directed graph 
# using adjacency list representation
class Graph:
  
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices 
        self.possible_path_distance = []
        self.total_distance = 0
         
        # default dictionary to store graph
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph
    def addEdge(self, u, v, cost):
        self.graph[u].append([v, cost])
  
    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
    def printAllPathsUtil(self, u, d, visited, path):
 
        # Mark the current node as visited and store in path
        visited[u]= True
        path.append(u)
 
        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            print(path)
            if len(path) == 2:
              for k in self.graph[path[0]]:
                if k[0] == path[1]:
                  self.total_distance = k[1]
                  break
            self.possible_path_distance.append(self.total_distance)
            self.total_distance = 0
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i[0]]== False:
                    self.total_distance += i[1]
                    self.printAllPathsUtil(i[0], d, visited, path)
                     
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u]= False
  
  
    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):
 
        # Mark all the vertices as not visited
        visited =[False]*(self.V)
 
        # Create an array to store paths
        path = []
 
        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)
  
  
  
# Create a graph given in the above diagram
g = Graph(8)
g.addEdge(0, 1, 15)
g.addEdge(0, 2, 10)
g.addEdge(0, 3, 17)
g.addEdge(0, 6, 5)

g.addEdge(1, 0, 15)
g.addEdge(1, 3, 12)

g.addEdge(2, 0, 10)
g.addEdge(2, 6, 7)

g.addEdge(3, 0, 17)
g.addEdge(3, 1, 12)
g.addEdge(3, 4, 2)
g.addEdge(3, 5, 10)
g.addEdge(3, 7, 4)

g.addEdge(4, 3, 2)

g.addEdge(5, 3, 10)
g.addEdge(5, 6, 11)
g.addEdge(5, 7, 11)

g.addEdge(6, 0, 5)
g.addEdge(6, 2, 7)
g.addEdge(6, 7, 25)

g.addEdge(7, 3, 4)
g.addEdge(7, 5, 11)
g.addEdge(7, 6, 25)

d = 4
for s in range(8):  
  print ("Following are all different paths from % d to % d :" %(s, d))
  g.printAllPaths(s, d)
  avg_heuristic = round(sum(g.possible_path_distance) / len(g.possible_path_distance))
  print(f"Heuristic for h({s}) is {avg_heuristic}")
  g.total_distance = 0
  g.possible_path_distance.clear()
