from Parking.colors import *


def dfs(graph, node, goal, path=None):
    if path is None:
        path = [node]

    if node == goal:
        yield path

    for next_node in graph[node] - set(path):
        yield from dfs(graph, next_node, goal, path + [next_node])


if __name__ == '__main__':
    print(GREEN + "Start of DFS Test" + DEFAULT)

    test_graph = {
        '1': set(['2', '3']),
        '2': set(['1', '4', '5']),
        '3': set(['1']),
        '4': set(['2', '5']),
        '5': set(['2', '4'])
    }

    print(BLUE + f"Starting point: {test_graph}" + DEFAULT)

    for i in range(1, 6):
        visited = list(dfs(test_graph, str(i), '5'))
        print(BLUE + f"{i}) Visited: {visited}" + DEFAULT)

        if len(visited) != 0:
            visited = min(visited, key=len)
            print(BLUE + f"Fastest path: {visited}" + DEFAULT)

        else:
            print(BLUE + "There is no path" + DEFAULT)

    print(GREEN + "Test was successful" + DEFAULT)
