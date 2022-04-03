def gPrime(G):
    """
    G is a graph
    returns a graph with all edges reversed
    """
    V, E = G;
    gPrime = {};
    for v in V:
        for i in range(len(v)):
            for j in range(len(v[0])):
                gPrime[j][i] = v[i][j];

    return (V, E);


    