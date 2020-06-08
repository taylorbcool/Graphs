"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        
        else:
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)

        # keep track of visited nodes
        visited = set()

        while q.size() > 0:
            v = q.dequeue()

            if v not in visited:
                print(v)
                visited.add(v)

                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:
            v = s.pop()

            if v not in visited:
                print(v)
                visited.add(v)

                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = {starting_vertex}

        def dft_print(starting_vertex):
            print(starting_vertex)
            for v in self.get_neighbors(starting_vertex):
                if v not in visited:
                    visited.add(v)
                    dft_print(v)

        dft_print(starting_vertex)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breadth-first order.
        """
        # sources is a dict for lookup purposes
        sources = {starting_vertex: None}
        # rest of code looks mostly the same except for adding nodes to sources dict
        visited = {starting_vertex}
        q = Queue()
        q.enqueue(starting_vertex)

        while q.size() > 0:
            current = q.dequeue()
            # if current is destination, break loop
            if current == destination_vertex:
                break
            for v in self.get_neighbors(current):
                if v not in visited:
                    sources[v] = current
                    q.enqueue(v)
                    visited.add(v)
        
        route = [destination_vertex]
        source = sources[destination_vertex]
        # this loop quickly orders the route from sources
        while source:
            route.insert(0, source)
            source = sources[source]
        return route

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        sources = {starting_vertex: None}
        visited = {starting_vertex}
        stack = Stack()
        stack.push(starting_vertex)

        while stack.size() > 0:
            current = stack.pop()
            if current == destination_vertex:
                break
            for v in self.get_neighbors(current):
                if v not in visited:
                    sources[v] = current
                    stack.push(v)
                    visited.add(v)
        
        route = [destination_vertex]
        source = sources[destination_vertex]
        # this loop quickly orders the route from sources
        while source:
            route.insert(0, source)
            source = sources[source]
        return route

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # create set and list for visited and route
        visited = {starting_vertex}
        route = []

        # define search function
        def search(starting_vertex, destination_vertex):
            # base case, if current is what we're looking for, add it to the route and start building route instead of visited
            if starting_vertex == destination_vertex:
                route.insert(0, starting_vertex)
                return True
            # if current isn't what we're looking for, add it to route and visited, try again with the next node
            for v in self.get_neighbors(starting_vertex):
                if v not in visited:
                    visited.add(v)
                    # this recursively shortens route to the shortest path
                    # by checking for an edge between the current vertex and the 
                    # destination
                    if search(v, destination_vertex):
                        route.insert(0, starting_vertex)
                        return True
        
        search(starting_vertex, destination_vertex)
        return route

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
