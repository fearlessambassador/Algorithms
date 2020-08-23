from collections import defaultdict 

class Graph:
    """ Graph class to extract required variables,
    and to build the graph list.
    
    Arguments:
    r (list): the raw graph given with the assignment.
    """

    # Constructor.
    def __init__(self, r):
        self.raw_graph = r
        self.rows_nr = len(r) # row number.
        self.graph = defaultdict(list) 
        self.diags = []
        self.row_count = 0
        self.diag_count = 0
        self.sort_count = 0

    def extract_diagonals(self):
        """ A recursive method to iterate over the
        values from the raw data.
        """

        # Break it at the end.
        if self.diag_count >= self.rows_nr:
            return

        diag = self.get_diagonal(self.raw_graph[self.diag_count])
        self.diags.append(diag)
        self.diag_count += 1

        return self.extract_diagonals()
        
    def get_diagonal(self, row: list, c: int = 0):
        """ A recursive method to extract the diagonal (node)
        values from the raw data row by row.

        Parameters:
        row (list): A row from the raw data.
        c (int): column count in the row.

        Returns:
        int: the value of the diagonal.
        """

        # The value is integer.
        if type(row[c]) is int:
            return row[c]

        return self.get_diagonal(row, c+1)

    def iterate_rows(self): 
        """ A recursive method to iterate over the rows. """  

        # Break it at the end.
        if self.row_count >= self.rows_nr:
            return

        self.iterate_cols(self.raw_graph[self.row_count])
        self.row_count += 1

        return self.iterate_rows()
           
    def iterate_cols(self, row: list):
        """ A  method to iterate over the columns in the given row. 
        
        Parameters:
        row (list): A row from the raw data.
        """  

        node_val = None
        col_count = 0
        for col in row:
            
            if type(col) is int:
                node_val = col
            elif col == True:
                self.graph[node_val].append(self.diags[col_count])

            col_count += 1

    def sort_nodes(self):
        """ Sort the vertice lists recursively."""

        if self.sort_count == self.row_count:
            return

        key = self.diags[self.sort_count]
        if len(self.graph[key]) > 1:
            self.graph[key].sort(reverse=True)

        self.sort_count += 1
        self.sort_nodes()       