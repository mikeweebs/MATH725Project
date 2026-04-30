class Graph:

    def __init__(self, numVertices):
        self.numVertices = numVertices
        self.numEdges = 0

        d = {}
        for i in range(1,numVertices+1):
            d[str(i)] = []

        self.vertices = d


    def __str__(self):
        string = f"Object: Graph({self.numVertices=})\n\n"
        string += 'Vertex:\t\tAdjacency List'
        for key in self.vertices.keys():
            string += f'\n{key}\t\t{self.vertices[key]}'

        return string


    def areAdjacent(self,a,b):
        try:
            return (a in self.vertices[b]) and (b in self.vertices[a])
        except:
            print(f"Invalid vertex/vertices: {a}, {b}")
            return False


    def isVertex(self,a):
        try:
            return a in self.vertices.keys()
        except:
            print(f"Invalid vertex: {a}")


    def addEdge(self,a,b):
        if a == b:
            print("Vertices must not be equal")

        elif a not in self.vertices.keys():
            print(f"Invalid vertex: {a}")

        elif b not in self.vertices.keys():
            print(f"Invalid vertex: {b}")

        elif self.areAdjacent(a,b):
            print(f"edge ({a},{b}) already exists")

        else:
            self.vertices[a].append(b)
            self.vertices[a].sort()
            self.vertices[b].append(a)
            self.vertices[b].sort()

            self.numEdges += 1


    def removeEdge(self,a,b):
        if self.areAdjacent(a,b):
            self.vertices[a].remove(b)
            self.vertices[b].remove(a)

            self.numEdges -= 1

        else:
            print(f"Invalid edge ({a},{b})")


    def vertexDegree(self,a):
        if self.isVertex(a):
            return len(self.vertices[a])
        else:
            print(f"Invalid vertex: {a}")


    def isEulerian(self):

        numEven = 0

        for v in self.vertices.keys():
            if (self.vertexDegree(v) % 2) == 0:
                numEven += 1

        return numEven == self.numVertices


    def renameVertex(self,a,b):
        if not self.isVertex(a):
            print(f"Invalid vertex: {a}")

        elif self.isVertex(b):
            print(f"Vertex {b} already exists")

        elif a == b:
            print("Cannot rename vertex to itself")

        else:
            for key in self.vertices.keys():
                if self.areAdjacent(a,key):
                    self.vertices[key].remove(a)
                    self.vertices[key].append(b)

            self.vertices[b] = self.vertices.pop(a)
