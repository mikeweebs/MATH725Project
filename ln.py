from graph import Graph

def getLnVertexBase(vstring):
    # helper func: return the name of the base vertex in the temporary vertex naming convention

    v,e = vstring.split(',')

    return v

def getLnEdge(vstring):
    # helper func: return the name of the base edge in the temporary vertex naming convention

    v,e = vstring.split(',')

    return e

def makeLn(G,n,autoName=True,showErr=False):
    # return the Ln graph of G according to H&N

    newG = Graph(n*G.numEdges,showErr)          # initialize with nq edges

    i = 1                               # edge counter

    for v in G.vertices.keys():
        for w in G.vertices.keys():
            if G.areAdjacent(v,w):
                # rename a vertex according to the method in H&N - each edge corresponds to 2
                # vertices, labeled by its corresponding vertex and edge

                if v < w:
                    newG.renameVertex(str(i),f"{v},{v}-{w}")

                elif v > w:
                    newG.renameVertex(str(i),f"{v},{w}-{v}")

                i += 1

    for v in newG.vertices.keys():
        for w in newG.vertices.keys():
            # two vertices in Ln are adjacent if they share the same base vertex but distinct edges

            if ',' in v and ',' in w:
                if getLnVertexBase(v) == getLnVertexBase(w) and v != w:
                    newG.addEdge(v,w);

    edgelist = []                       # initialize list that has all names of new edges once

    for v in newG.vertices.keys():
        if ',' in v:
            edge = getLnEdge(v)
            if edge not in edgelist:
                edgelist.append(edge)

    edgelist.sort()

    j = n - 2                   # Additional index giving how many internal vertices of W_e to add

    # Rename jq vertices for easier manipulation
    for edge in edgelist:
        for a in range(1,j+1):
            newG.renameVertex(str(i),f'm,{edge},{a}')

            i += 1

    # Join two vertices along W_e according to H&N
    for v in newG.vertices.keys():
        for w in newG.vertices.keys():
            if v.split(',')[0] == 'm' and w.split(',')[0] == 'm':
                if v.split(',')[2] == '1':
                    newG.addEdge(v.split(',')[1][0]+','+v.split(',')[1],v)

                if v.split(',')[1] == w.split(',')[1] and (j != 0 or j != 1) and abs(int(v.split(',')[2]) - int(w.split(',')[2])) <= 1:
                    newG.addEdge(v,w)

                if w.split(',')[2] == str(j):
                    newG.addEdge(w.split(',')[1][2]+','+w.split(',')[1],w)

            elif j == 0:
                if v.split(',')[1] == w.split(',')[1]:
                    newG.addEdge(v,w)

    # Automatically renames the vertices to more legible labels
    if autoName:

        i = 1

        mylist = [v for v in newG.vertices.keys()]

        for v in mylist:
            newG.renameVertex(v,str(i))
            i += 1

    return newG
