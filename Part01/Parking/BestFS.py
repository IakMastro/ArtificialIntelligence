from Parking.colors import *


def best_fs(graph, node, goal):
    queue = [(node, [node])]

    while queue:
        (vertex, path) = queue.pop(0)

        if vertex == goal:
            yield path

        else:
            for next in graph[vertex] - set(path):
                queue.append((next, path + [next]))


if __name__ == '__main__':
    print(GREEN + "Start of BestFS Test" + DEFAULT)

    test_graph = {
        '1': set(['2', '3']),
        '2': set(['1', '4', '5']),
        '3': set(['1']),
        '4': set(['2', '5']),
        '5': set(['2', '4'])
    }

    print(BLUE + f"Starting point: {test_graph}" + DEFAULT)

    for i in range(1, 6):
        visited = list(best_fs(test_graph, str(i), '5'))
        print(BLUE + f"{i}) Visited: {visited}" + DEFAULT)

        if len(visited) != 0:
            visited = min(visited, key=len)
            print(BLUE + f"Fastest path: {visited}" + DEFAULT)

        else:
            print(BLUE + "There is no path" + DEFAULT)

    print(GREEN + "Test was successful" + DEFAULT)
