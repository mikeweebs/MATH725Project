class Graph:

    def __init__(self, numVertices, showErr=True):
        # All methods in this package assume that you are constructing a connected, simple graph
        # The methods will not allow you to create parallel edges or loops

        self.numVertices = numVertices # stores how many vertices are in the graph
        self.numEdges = 0              # stores number of edges in the graph
        self.showErr = showErr         # bool that decides if errors are displayed to terminal or just canceled

        d = {}
        for i in range(1,numVertices+1):
            d[str(i)] = []                  # dictionary where the keys are vertices and the values are a list of
                                            # vertices that are adjacent to the key vertex

        self.vertices = d


    def __str__(self):
        string = f"Object: Graph\n\n"
        string += 'Vertex:\t\tAdjacency List'
        for key in self.vertices.keys():
            string += f'\n{key}\t\t{self.vertices[key]}'

        return string


    def areAdjacent(self,a,b):
        # Tells if vertices a and b are adjacent

        try:
            return (a in self.vertices[b]) and (b in self.vertices[a])
        except:
            if self.showErr:
                print(f"Invalid vertex/vertices: {a}, {b}")
            return False


    def isVertex(self,a):
        # finds if vertex a is a vertex in the graph

        try:
            return a in self.vertices.keys()
        except:
            if self.showErr:
                print(f"Invalid vertex: {a}")


    def addEdge(self,a,b):
        # add an edge between a and b if one does not already exist

        if a == b:
            if self.showErr:
                print("Vertices must not be equal")

        elif a not in self.vertices.keys():
            if self.showErr:
                print(f"Invalid vertex: {a}")

        elif b not in self.vertices.keys():
            if self.showErr:
                print(f"Invalid vertex: {b}")

        elif self.areAdjacent(a,b):
            if self.showErr:
                print(f"edge ({a},{b}) already exists")

        else:
            self.vertices[a].append(b)
            self.vertices[a].sort()
            self.vertices[b].append(a)
            self.vertices[b].sort()

            self.numEdges += 1


    def removeEdge(self,a,b):
        # remove an edge between a and b if it exists

        if self.areAdjacent(a,b):
            self.vertices[a].remove(b)
            self.vertices[b].remove(a)

            self.numEdges -= 1

        else:
            if self.showErr:
                print(f"Invalid edge ({a},{b})")


    def vertexDegree(self,a):
        # report how many edges are adjacent to a

        if self.isVertex(a):
            return len(self.vertices[a])
        else:
            if self.showErr:
                print(f"Invalid vertex: {a}")


    def isEulerian(self):
        # returns True is the graph is Eulerian

        numEven = 0

        for v in self.vertices.keys():
            if (self.vertexDegree(v) % 2) == 0:
                numEven += 1

        return numEven == self.numVertices


    def renameVertex(self,a,b):
        # rename the key representing the vertex a

        if not self.isVertex(a):
            if self.showErr:
                print(f"Invalid vertex: {a}")

        elif self.isVertex(b):
            if self.showErr:
                print(f"Vertex {b} already exists")

        elif a == b:
            if self.showErr:
                print("Cannot rename vertex to itself")

        else:
            for key in self.vertices.keys():
                if self.areAdjacent(a,key):
                    self.vertices[key].remove(a)
                    self.vertices[key].append(b)

            self.vertices[b] = self.vertices.pop(a)
