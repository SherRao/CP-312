def gPrime(G):
    """
    G is a graph
    returns a graph with all edges reversed
    """
    V, E = G;
    gPrime = {};
    for v in V:
        gPrime[v] = [];

    for v in V:
        for e in E[v]:
            gPrime[e[1]].append(E[e][v]);

    return gPrime;

    