from DFS import dfs
from colors import *

if __name__ == '__main__':
    graph = {
        '1': ["PLATFORM 1", '2', '4'],
        '2': ["PLATFORM 2", '1', '3'],
        '3': ["EMPTY", '2', '4'],
        '4': ["PLATFORM 3", '1', '3']
    }

    visited = dfs("1", graph)
    print(BLUE + f"{visited}" + DEFAULT)
