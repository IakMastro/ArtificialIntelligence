from DFS import dfs
from swap import swap
from colors import *

if __name__ == '__main__':
    neighbours = {
        '1': set(['2', '4']),
        '2': set(['1', '3']),
        '3': set(['2', '4']),
        '4': set(['1', '3'])
    }

    spaces = {
        '1': "Platform 1",
        '2': "Platform 2",
        '3': "Empty",
        '4': "Platform 3"
    }

    visited = list(dfs(neighbours, '1', '3'))

    if len(visited) == 1:
        visited = visited[0]
    elif len(visited[0]) > len(visited[1]):
        visited = visited[1]
    else:
        visited = visited[0]

    print(BLUE + f"DFS: {visited}" + DEFAULT)

    swap(spaces, visited)
    print(BLUE + f"SWAP: {spaces}" + DEFAULT)
