
from graph import Graph       

class DFS(Graph):
    """ Depth first graph search.

    Arguments:
    raw_graph (list): the raw graph given with the assignment.

    """

    # Constructor.
    def __init__(self, raw_graph: list): 
        Graph.__init__(self, raw_graph)
        self.result = []

    def dfs_util(self, v: int): 
        """ A method to recursively process
        all not visited vertices/ nodes.

        Parameters:
        v (int): Vertice.

        """

        # Set the current node to visited.
        self.visited[v] = True

        # Append the node to the result list.
        self.result.append(v)
        
        # Iterate over the sub lists.
        for i in self.graph[v]: 
            if self.visited[i] == False:
                self.dfs_util(i) 

    def dfs(self, v: int): 
        """ A method for depth-first traversal.
        
        Parameters:
        v (int): the node.
        """
        
        # Set all nodes/ vertices as not visited.
        self.visited = [False] * (max(self.diags) + 1)

        # Sort.
        self.sort_nodes()
        
        # Call the recursive utility function.
        self.dfs_util(v) 


    def get_result(self) -> str:
        """ Create a formatted string of the result.

        Returns:
        string: A formatted string of the result.
        """

        return ", ".join( str(x) for x in self.result)


graph = [
    [1, True, False, True, False, True, False, False],
    [False, 4, True, False, False, False, False, False],
    [False, False, 2, False, False, False, False, False],
    [False, False, False, 6, True, False, False, False],
    [False, False, False, False, 9, False, False, False],
    [False, False, False, False, False, 3, True, False],
    [False, False, False, False, False, False, 10, True],
    [False, False, False, False, False, False, False, 7]
]
g = DFS(graph) 
g.extract_diagonals()
g.iterate_rows()
g.dfs(1) 
result = g.get_result()

print(result)

# Result example:
# 1, 6, 9, 4, 2, 3, 10, 7