# MATH725Project

#### By Michael Wieber, May 2026

Package made for constructing and utilizing the Ln(G) combinatorial graph.

### Includes

- `Graph(int numVertices,bool showErr=True) (class)`: Initializes with `numVertices` vertices and shows errors if `showErr` is `True`. Uses the adjacency list representation of graphs.
- `Graph.vertices (dict)`: The keys in this dictionary are the labels for each vertex, and the value for each key is a list that contains other keys in the dictionary, representing which vertices are adjacent to the key vertex.
- `Graph.numEdges (int)`: The number of edges in the graph.
- `Graph.addEdge(a,b) (a,b str)`: Adds the vertex `a` to the adjacency list of `b` and vice versa. Does not allow parallel edges or loops.
- `Graph.removeEdge(a,b) (a,b str)`: Removes the vertex `a` from the adjacency list of `b` and vice versa. Will only operate if the edge exists.
- `Graph.vertexDegree(a) (a str, return int)`: returns the number of vertices adjacent to `a`.
- `Graph.renameVertex(a,b) (a,b str)`: Relabels the vertex `a` to `b`.
- `Graph.isEulerian() (return bool)`: Reports if the graph is Eulerian by checking the parity of each vertex; if all have even degree, then the graph is Eulerian. Assumes that the graph has all edges in one component.
- `makeLn(graph G,int n,bool autoName=True,bool showErr=False) (return graph)`: Construct the graph L_n(G) using the W_e definition given by H&N. Automatically renames the vertices of L_n(G) if `autoName` is `True` to be the range from 1 to `n*G.numEdges` since it has that many vertices. Passes `showErr` to `Graph()`.

### How To Use

Download and extract the repository and run main.py in the terminal from the directory that contains the repository:

```
python main.py
```

The file runs through the same examples as in the report and runs output through the terminal.

### Dependencies:
Package was built using Python 3.14.4, but should work for any Python 3.x.x
