"""
CP 312 - Assignment 4
P1.py

@author Nausher Rao (190906250)
@author Will Roberts (191023880)
"""
import sys
import time


def main():
    args = sys.argv[1:]
    if(len(args) == 0):
        raise Exception("Program needs a file to run!")
        exit()

    vertices, graph = processFile(args[0])
    visited = [False] * vertices
    visited[0] = True

    print(f"Vertices = {vertices}")
    print(f"Graph = {graph}")

    start = time.perf_counter()
    result = []
    salesmanBacktrack(result, graph, visited, 0, vertices, 1, 0)
    finish = time.perf_counter()

    print(f"Time Taken: {(finish - start) * 1000}ms")
    print(f"Shortest Cycle Length: {min(result)}")
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


def salesmanBacktrack(result: list, graph: list, visited: list, current: int, vertices: int, count: int, cost: int):
    """
    Recursive function that finds the shortest cycle in the graph.
    """
    if(count == vertices):
        result.append(cost + graph[current][0])

    else:
        for i in range(vertices):
            if(visited[i] == False):
                visited[i] = True
                salesmanBacktrack(result, graph, visited, i, vertices, count + 1, cost + graph[current][i])
                visited[i] = False

    return


if(__name__ == "__main__"):
    main()
