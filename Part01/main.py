from DFS import dfs
from swap import swap
from is_empty import is_empty
from colors import *

if __name__ == '__main__':
    neighbours = {
        '1': set(['2', '4']),
        '2': set(['1', '3']),
        '3': set(['2', '4', '6']),
        '4': set(['1', '3', '5']),
        '5': set(['4', '6']),
        '6': set(['3', '5'])
    }

    spaces = {
        '1': ["Empty"],
        '2': ["Platform 1", "YES"],
        '3': ["Platform 2", "YES"],
        '4': ["Platform 3", "YES"],
        '5': ["Platform 4", "NO"],
        '6': ["Platform 5", "YES"]
    }

    goal = is_empty(spaces)
    if goal is None:
        print("No space")

    else:
        visited = min(list(dfs(neighbours, '1', is_empty(spaces))), key=len)
        print(BLUE + f"DFS: {visited}" + DEFAULT)

        swap(spaces, visited)
        print(BLUE + f"SWAP: {spaces}" + DEFAULT)
