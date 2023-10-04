# Assignment 2
# Ben Cimini, Blair Bowen, Stetson King




# BASIC GRAPH DATA STRUCTURE
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# DISCLAIMER: Basic components of class <Graph> were implemented with the help
# of ChatGPT. I've added thorough comments to demonstrate my learning.
# Additionally, you can find a brief summary beneath this section.

class Graph:
    cityDictionary = {
        "Arad": 366,
        "Bucharest": 0,
        "Craiova": 160,
        "Drobeta": 242,
        "Eforie": 161,
        "Fagaras": 176,
        "Giurgiu": 77,
        "Hirsova": 151,
        "Iasi": 226,
        "Lugoj": 244,
        "Mehadia": 241,
        "Neamt": 234,
        "Oradea": 380,
        "Pitesti": 100,
        "Rimnicu Vilcea": 193,
        "Sibiu": 253,
        "Timisoara": 329,
        "Urziceni": 80,
        "Vaslui": 199,
        "Zerind": 374
    }

    def __init__(self):
        """
        This constructor method initializes an empty graph.
        """
        self.graph = {} # <Graph> is implemented with a two-level dictionary.
                        # The outer level represents vertices; the inner level
                        # represents edges.


    def add_vertex(self, vertex):
        """
        This method adds a vertex to the graph.
        
        Parameters:
        - vertex: The vertex to be added.
        
        Returns:
        - none
        """
        if vertex not in self.graph:
            self.graph[vertex] = {} # Notice that vertices cannot be repeated
                                    # and that they are assigned an empty
                                    # dictionary on addition. That empty
                                    # dictionary will later contain edges.


    def add_edge(self, vertex1, vertex2, weight):
        """
        This method adds an edge between two vertices with a given weight.

        Parameters:
        - vertex1: The first vertex.
        - vertex2: The second vertex.
        - weight: The weight of the edge between vertex1 and vertex2.
        
        Returns:
        - none
        """
        if vertex1 in self.graph and vertex2 in self.graph:
            # Add a bidirectional edge from vertex1 to vertex2 with the given
            # weight. Implementation wise, this requires two edges. These lines
            # add key-value pairs to the inner dictionary of each vertex. The
            # pairs describe an adjacent vertex and the weight of the edge they
            # share.
            self.graph[vertex1][vertex2] = weight
            self.graph[vertex2][vertex1] = weight


    def get_vertices(self):
        """
        This method gets a list of all vertices in the graph.
        
        Parameters:
        - none

        Returns:
        - A list of vertices.
        """
        return list(self.graph.keys()) # The built-in function <list()> is used
                                       # get all keys in the outer dictionary.


    def get_edges(self):
        """
        This method gets a list of all edges in the graph along with their weights.
        
        Parameters:
        - none

        Returns:
        - A list of tuples representing edges and their weights.
        """
        # Initialize an empty list of edges.
        edges = []
        
        # Iterate over both outer and inner dictionaries. Avoid duplicate edges
        # by checking if vertex1 < vertex2. If so, that edge has already been
        # appended to the list. This consideration is taken because the graph is
        # undirected, which, as mentioned, requires each edge to be represented
        # twice in the data structure.
        for vertex1 in self.graph:
            for vertex2, weight in self.graph[vertex1].items():
                if vertex1 < vertex2:
                    edges.append((vertex1, vertex2, weight))

        return edges
    

    def get_neighbors(self, vertex):
        """
        This method gets a list of neighboring vertices of a given vertex.

        Parameters:
        - vertex: The vertex whose neighbors are to be found.
        
        Returns:
        - A list of neighboring vertices.
        """
        # The vertex must exist in order for it to have neighbors.
        if vertex in self.graph:
            return list(self.graph[vertex].keys()) # Again, the built-in
                                                   # function <list()> is used
                                                   # to compile all keys in a
                                                   # certain inner dictionary.
        else:
            return []
        

    def get_weight(self, vertex1, vertex2):
        """
        This method gets the weight of the edge between two vertices.

        Parameters:
        - vertex1: The first vertex.
        - vertex2: The second vertex.
        
        Returns:
        - The weight of the edge between vertex1 and vertex2.
        """
        # Both vertices must exist in order to have an edge between them.
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            return self.graph[vertex1][vertex2] # The weight can be indexed by
                                                # drilling down with two keys.
                                                # They combine to describe an
                                                # edge.
        else:
            # Return None if there is no edge between the vertices.
            return None
        

    def __str__(self):
        """
        This special method returns a string representation of the graph.

        Returns:
        - A string representation of the graph.
        """
        # This method is invoked with built-in functions <print()>, <str()>, and
        # <format()>. It captures the graph in a string of the format defined
        # below.
        result = ""
        for vertex in self.graph:
            neighbors = self.graph[vertex]
            result += f"{vertex}: {neighbors}\n"
        
        return result
    
# SUMMARY: The key takeaway from <Graph> is that it's represented with a
# two-level dictionary. The outermost keys are vertices, each having an inner
# dictionary as their corresponding value. In them, the key-value pairs are
# edges - given as <other vertex: weight>.




# SEARCH ALGORITHMS AND THEIR HELPER METHODS
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# DISCLAIMER: Some of the methods below were implemented with the help of
# ChatGPT - and are marked as such. As before, those methods contain thorough
# comments and a summary beneath them.

    def BFS(self, start, goal):
        """
        This method performs a breadth-first search on the graph, from a start
        vertex to a goal vertex.
        
        Parameters:
        - start: The vertex where searching begins.
        - goal: The vertex where searching concludes.
        
        Returns:
        - visited: A list of vertices visited from start to goal.
        - cost: The sum of edge weight between traversed vertices.
        """
        # Initialize two lists with the start vertex: <visited> and <queue>.
        # <visited> will form our path; <queue> will hold vertices to maybe
        # visit, pending evaluation.
        visited = [start]
        queue = [start]
        
        cost = 0 # Sum of <weight> from edges traversed.
        
        # Search while <queue> isn't empty. In other words, search while some
        # reachable vertices from <current> haven't been evaluated.
        while queue:
            # Pop a vertex from the front of <queue> for evaluation.
            current = queue.pop(0)
            
            # Evaluation entails checking the neighbors (adjacents) of a vertex.
            # Unvisited neighbors are added to both lists, marking that they've
            # been visited but require evaluation themselves.
            for neighbor, weight in self.graph[current].items():
                if neighbor not in visited: # Didn't use <get_neighbors()>
                                            # because of the need for fully-
                                            # represented edges.
                    visited.append(neighbor)
                    queue.append(neighbor)
                    
                    # Sum <weight>.
                    cost += weight
                    
                    # Check if the goal vertex was visited. If so, return.
                    if neighbor == goal:
                        return (visited, weight)
        
        return ([], 0) # This line executing means the goal vertex was never
                       # visited.


    def AStar(self, start, goal):
        # Create a list to store nodes to be expanded.
        open_list = [(start, 0)]  # Each element is a tuple (vertex, estimated_cost).
        
        # Create dictionaries to track the cost to reach each node and its parent.
        cost_to_reach = {start: 0}
        parent = {start: None}
        
        while open_list:
            # Sort the open list by estimated total cost (f(x)).
            open_list.sort(key=lambda x: x[1])
            
            # Get the vertex with the lowest estimated total cost.
            current, _ = open_list.pop(0)
            
            # If the current node is the goal, reconstruct the path and return it.
            if current == goal:
                path = [current]
                while parent[current]:
                    path.insert(0, parent[current])
                    current = parent[current]
                
                # Calculate the total weight of the path.
                total_weight = sum(self.graph[path[i]][path[i + 1]] for i in range(len(path) - 1))
                
                return (path, total_weight)
            
            # Explore neighbors of the current node.
            for neighbor, weight in self.graph[current].items():
                # Calculate the tentative cost to reach the neighbor.
                tentative_cost = cost_to_reach[current] + weight
                
                # If the neighbor has not been visited or the new path is shorter,
                # update the cost and set the parent.
                if neighbor not in cost_to_reach or tentative_cost < cost_to_reach[neighbor]:
                    cost_to_reach[neighbor] = tentative_cost
                    parent[neighbor] = current
                    
                    # Calculate the estimated total cost (f(x)).
                    estimated_cost = tentative_cost + self.cityDictionary[neighbor]
                    
                    # Add the neighbor to the open list with its estimated cost.
                    open_list.append((neighbor, estimated_cost))
        
        # If the open list becomes empty and the goal is not reached, there is no path.
        return ([], 0)

# DRIVER
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    g = Graph()
    
    # Add all vertices.
    g.add_vertex("Arad")
    g.add_vertex("Bucharest")
    g.add_vertex("Craiova")
    g.add_vertex("Drobeta")
    g.add_vertex("Eforie")
    g.add_vertex("Fagaras")
    g.add_vertex("Giurgiu")
    g.add_vertex("Hirsova")
    g.add_vertex("Iasi")
    g.add_vertex("Lugoj")
    g.add_vertex("Mehadia")
    g.add_vertex("Neamt")
    g.add_vertex("Oradea")
    g.add_vertex("Pitesti")
    g.add_vertex("Rimnicu Vilcea")
    g.add_vertex("Sibiu")
    g.add_vertex("Timisoara")
    g.add_vertex("Urziceni")
    g.add_vertex("Vaslui")
    g.add_vertex("Zerind")
    
    # Add edges with Arad.
    g.add_edge("Arad", "Zerind", 75)
    g.add_edge("Arad", "Sibiu", 140)
    g.add_edge("Arad", "Timisoara", 118)
    
    # Add edges with Bucharest that don't already exist.
    g.add_edge("Bucharest", "Fagaras", 211)
    g.add_edge("Bucharest", "Pitesti", 101)
    g.add_edge("Bucharest", "Giurgiu", 90)
    g.add_edge("Bucharest", "Urziceni", 85)
    
    # Add edges with Craiova that don't already exist.
    g.add_edge("Craiova", "Drobeta", 120)
    g.add_edge("Craiova", "Rimnicu Vilcea", 146)
    g.add_edge("Craiova", "Pitesti", 138)
    
    # Add edges with Drobeta that don't already exist.
    g.add_edge("Drobeta", "Mehadia", 75)
    
    # Add edges with Eforie that don't already exist.
    g.add_edge("Eforie", "Hirsova", 86)
    
    # Add edges with Fagaras that don't already exist.
    g.add_edge("Fagaras", "Sibiu", 99)
    
    # Add edges with Giurgiu that don't already exist.
    # NONE
    
    # Add edges with Hirsova that don't already exist.
    g.add_edge("Hirsova", "Urziceni", 98)
    
    # Add edges with Iasi that don't already exist.
    g.add_edge("Iasi", "Neamt", 87)
    g.add_edge("Iasi", "Vaslui", 92)
    
    # Add edges with Lugoj that don't already exist.
    g.add_edge("Lugoj", "Timisoara", 111)
    g.add_edge("Lugoj", "Mehadia", 70)
    
    # Add edges with Mehadia that don't already exist.
    # NONE
    
    # Add edges with Neamt that don't already exist.
    # NONE
    
    # Add edges with Oradea that don't already exist.
    g.add_edge("Oradea", "Zerind", 71)
    g.add_edge("Oradea", "Sibiu", 151)
    
    # Add edges with Pitesti that don't already exist.
    g.add_edge("Pitesti", "Rimnicu Vilcea", 97)
    
    # Add edges with Rimnicu Vilcea that don't already exist.
    g.add_edge("Rimnicu Vilcea", "Sibiu", 80)
    
    # Add edges with Sibiu that don't already exist.
    # NONE
    
    # Add edges with Timisoara that don't already exist.
    # NONE
    
    # Add edges with Urziceni that don't already exist.
    g.add_edge("Urziceni", "Vaslui", 142)
    
    # Add edges with Vaslui that don't already exist.
    # NONE
    
    # Add edges with Zerind that don't already exist.
    # NONE
    
    print(g)
    
    
    
    
# TESTING
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
    print("")
    print("")

    # BFS
    BFS_result = g.BFS("Oradea", "Bucharest")
    print(BFS_result)

    # AStar
    AStar_result = g.AStar("Oradea", "Bucharest")
    print(AStar_result)
    AStar_result = g.AStar("Timisoara", "Bucharest")
    print(AStar_result)
    AStar_result = g.AStar("Neamt", "Bucharest")
    print(AStar_result)
