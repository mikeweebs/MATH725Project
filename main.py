from graph import Graph
from ln import makeLn

def main():
    G = Graph(3)

    G.addEdge('1','2')
    G.addEdge('2','3')
    #G.addEdge('1','3')



    print(f'{G.numEdges=}')
    L = makeLn(G,2)
    print(L)



main()
