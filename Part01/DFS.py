from colors import *


# Μέθοδος που υλοποιείται ο αλγόριθμος DFS σε Python
def dfs(graph, node, goal, path=None):
    if path is None:
        path = [node]
    if node == goal:
        yield path
    for next_node in graph[node] - set(path):
        yield from dfs(graph, next_node, goal, path + [next_node])


# Επείδηξη λειτουργίας του DFS αλγορίθμου
if __name__ == '__main__':
    print(GREEN + "Start of DFS Test" + DEFAULT)

    test_graph = {
        '1': set(['2', '4']),
        '2': set(['1', '3']),
        '3': set(['2', '4']),
        '4': set(['1', '3'])
    }

    for i in range(1, 5):
        visited = list(dfs(test_graph, str(i), '3'))
        print(BLUE + f"{i}) Visited: {visited}" + DEFAULT)

        if len(visited) == 1:
            visited = visited[0]
        elif len(visited[0]) > len(visited[1]):
            visited = visited[1]
        else:
            visited = visited[0]

        print(BLUE + f"Fastest path: {visited}" + DEFAULT)

    print(GREEN + "Test was successful" + DEFAULT)

    '''
    
    '''
