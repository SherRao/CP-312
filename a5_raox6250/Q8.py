def largestComponent(G):
    V, E = G;

    vertexDeletedIndex = 0;
    largestComponent = 0;
    component = 0;
    colour = [];

    for i in range(len(V)):
        Vcopy = V;
        del Vcopy[i];

        for v in V:
            colour[v] = "white";
        
        for v in Vcopy:
            if colour[v] == "white":
                component = DFS(G, v);
                if(component > largestComponent):
                    largestComponent = component;
                    vertexDeletedIndex = v;

    return vertexDeletedIndex, largestComponent;


def DFS(G, v):
    pass;

