"""
CP 312 - Assignment 4
P1.py

@author Nausher Rao (190906250)
@author Will Roberts (191023880)
"""
import math
import time
import sys

result = float('inf')


def main():
    args = sys.argv[1:]
    if(len(args) == 0):
        raise Exception("Program needs a file to run!")
        exit()

    vertices, graph = processFile(args[0])
    finalPath = [None] * (vertices + 1)
    visited = [False] * vertices
    visited[0] = True

    currentPath = [-1] * (vertices + 1)
    currentPath[0] = 0

    currentBound = 0
    for i in range(vertices):
        currentBound += minEdge(graph, i, vertices) + secondMinEdge(graph, i, vertices)
    currentBound = math.ceil(currentBound / 2)

    print(f"Vertices = {vertices}")
    print(f"Graph = {graph}")

    start = time.perf_counter()
    salesmanBacktrack(graph, visited, currentBound, 0, 1, vertices, currentPath, finalPath)
    finish = time.perf_counter()

    print(f"Time Taken: {(finish - start) * 1000}ms")
    print(f"Shortest Cycle Length: {result}")
    return


def processFile(fileName: str):
    """
    Processes the file and returns the amount of vertices in the graph, as well
    as the adjency matrix representation of the graph.
    """

    file = open(fileName, "r+")
    lines = file.readlines()
    if(len(lines) < 2):
        raise Exception("File must have atleast two lines!")
        exit()

    vertices = int(lines[0])
    graph = []
    for line in lines[1:]:
        splitLine = line.split(" ")
        graph.append([int(x) for x in splitLine])

    return vertices, graph


def salesmanBacktrack(
        graph: list, visited: list, currentBound: int, currentWeight: int, level: int, vertices: int, currentPath: list,
        finalPath: list):
    """
    Recursive function that finds the shortest cycle in the graph.
    """
    global result
    if(level == vertices):
        cycleWeight = currentWeight + graph[currentPath[level - 1]][currentPath[0]]
        if(cycleWeight < result):
            finalPath[:vertices + 1] = currentPath[:]
            finalPath[vertices] = currentPath[0]
            result = cycleWeight

    else:
        for i in range(vertices):
            temp = currentBound
            currPath = graph[currentPath[level - 1]][i]

            if(currPath != 0 and not visited[i]):
                currentWeight = currentWeight + currPath
                halfMinEdge = minEdge(graph, i, vertices) / 2
                if(level == 1):
                    currentBound -= minEdge(graph, currentPath[level - 1], vertices) + halfMinEdge

                else:
                    currentBound -= secondMinEdge(graph, currentPath[level - 1], vertices) + halfMinEdge

            if(currentBound + currentWeight < result):
                currentPath[level] = i
                visited[i] = True
                salesmanBacktrack(graph, visited, currentBound, currentWeight,
                                  level + 1, vertices, currentPath, finalPath)

            currentWeight -= graph[currentPath[level - 1]][i]
            currentBound = temp
            visited = [False] * len(visited)
            for j in range(level):
                if(currentPath[j] != -1):
                    visited[currentPath[j]] = True

    return


def minEdge(graph, i, vertices):
    """
    Returns the minimum edge weight in the graph, ending at vertex i.
    """

    min = float('inf')
    for j in range(vertices):
        x = graph[i][j]
        if(x < min and i != j):
            min = x

    return min


def secondMinEdge(graph, i, vertices):
    """
    Returns the second minimum edge weight in the graph, ending at vertex i.
    """

    min, secondMin = float('inf'), float('inf')
    for j in range(vertices):
        if(i == j):
            continue

        x = graph[i][j]
        if(x <= min):
            secondMin = min
            min = x

        elif(x <= secondMin and x != min):
            secondMin = x

    return secondMin


if(__name__ == "__main__"):
    main()
