from graph import Graph
from ln import makeLn

def main():
    G = Graph(6)            # Create G with its edges as from the report

    G.addEdge('1','2')
    G.addEdge('2','3')
    G.addEdge('3','4')
    G.addEdge('5','4')
    G.addEdge('3','5')
    G.addEdge('3','6')
    G.addEdge('1','6')

    H = Graph(5)            # Create H with its edges as from the report

    H.addEdge('1','2')
    H.addEdge('3','2')
    H.addEdge('3','4')
    H.addEdge('4','5')
    H.addEdge('1','5')
    H.addEdge('1','4')
    H.addEdge('4','2')
    H.addEdge('5','2')

    # Generate L_3 for both G and H as from the report
    L_3G = makeLn(G,3)
    L_3H = makeLn(H,3)

    #print(L_3H)

    print('Graph G, in accordance to the construction in the report:\n')
    print(G)
    print('\nG has the corresponding graph L_3(G):\n')
    print(L_3G)
    print(f'\nIs G Eulerian: {G.isEulerian()}')
    print(f'Since G {'is' if G.isEulerian() else 'is not'} Eulerian, then L_3(G) {'is' if G.isEulerian() else 'is not'} Hamiltonian')

    print('\n')

    print('Graph H, in accordance to the construction in the report:\n')
    print(H)
    print('\nH has the corresponding graph L_3(H):\n')
    print(L_3H)
    print(f'\nIs H Eulerian: {H.isEulerian()}')
    print(f'Since H {'is' if H.isEulerian() else 'is not'} Eulerian, then L_3(H) {'is' if H.isEulerian() else 'is not'} Hamiltonian')

main()
