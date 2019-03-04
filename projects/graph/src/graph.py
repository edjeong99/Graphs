"""
Simple graph implementation
init
"""


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return (len(self.queue))


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return (len(self.stack))


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist")

    def bft(self, starting_vertex_id):
        # Create an empty queue
        q = Queue()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Queue
        q.enqueue(starting_vertex_id)
        # While the queue is not empty....
        while q.size() > 0:
            # Dequeue the first node from the queue
            v = q.dequeue()
            # If that node has not been visted...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then, put all of it's children into the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

    def bfs(self, starting_vertex_id, query):
        # Create an empty queue
        q = Queue()
        # Create an empty set of visited vertices
        visited = set()

        # create a list for path for each vertex
        path = []

        # Put the starting vertex in our Queue
        q.enqueue(starting_vertex_id)
        # assign path for this vertex
        path.append(starting_vertex_id)
        q.enqueue(path)

        while q.size() > 0:

            # get next item and path for that item in queue
            v = q.dequeue()
            path = q.dequeue()

            if v not in visited:
                if v == query:
                    return path  # if match, return path

                visited.add(v)  # add vertex to visited
            # check all neighbor of current vortex
                for neighbor in self.vertices[v]:
                    temp = path[:]
                    q.enqueue(neighbor)
                    temp.append(neighbor)
                    q.enqueue(temp)

    def dft(self, starting_vertex_id):
        # Create an empty stack
        s = Stack()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Stack
        s.push(starting_vertex_id)
        # While the stack is not empty....
        while s.size() > 0:
            # Pop the top node from the stack
            v = s.pop()
            # If that node has not been visted...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then, put all of it's children into the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex_id, visited=None):
        # initialize visited set
        if visited is None:
            visited = set()

        print(starting_vertex_id)  # print current vertex
        visited.add(starting_vertex_id)  # add current veretext to visited

        # Then, put all of it's children into the stack
        for neighbor in self.vertices[starting_vertex_id]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def dfs(self, starting_vertex_id, query):
        # Create an empty queue
        s = Stack()
        # Create an empty set of visited vertices
        visited = set()

        # create a list for path for each vertex
        path = []

        # Put the starting vertex in our Queue
        s.push(starting_vertex_id)
        # assign path for this vertex
        path.append(starting_vertex_id)
        s.push(path)

        while s.size() > 0:

            # get next item and path for that item in queue
            path = s.pop()
            v = s.pop()

            if v not in visited:
                if v == query:
                    return path  # if match, return path

                visited.add(v)  # add vertex to visited
            # check all neighbor of current vortex
                for neighbor in self.vertices[v]:
                    temp = path[:]
                    s.push(neighbor)
                    temp.append(neighbor)
                    s.push(temp)


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')

graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('0', '4')
graph.add_edge('1', '7')
graph.add_edge('1', '4')
graph.add_edge('5', '3')
graph.add_edge('5', '6')


print(graph.vertices)
print("end of vertices")

#print(graph.bfs('0', '7'))
print(graph.dfs('3', '1'))
