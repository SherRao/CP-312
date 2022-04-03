def shortestCycle(G):
    V, E = G;
    shortestCycle = MAX_VALUE;

    visited = [False] * V;
    distance = [0] * V;
    queue = Queue();

    for v in V:
        visited[v] = False;
        distance[v] = 0
        queue.append(v);

        while len(queue) > 0:
            u = queue.pop();
            visited[u] = True;
            for adj in E[u]:
                if visited[adj] == False:
                    distance[adj] = distance[u] + 1;
                    queue.append(v);

                else:
                    dist = distance[u] + distance[adj] + 2;
                    shortestCycle  = min(shortestCycle, dist);
    
    if(shortestCycle == MAX_VALUE):
        return -1;

    return shortestCycle;