from Parking.colors import *


def swap(spaces, visited):
    for i in range(len(visited) - 1, 0, -1):
        spaces[visited[i]], spaces[visited[i - 1]] = spaces[visited[i - 1]], spaces[visited[i]]
    return spaces


if __name__ == '__main__':
    print(GREEN + "Start of Swap Test" + DEFAULT)

    test_spaces = {
        '1': ["Empty"],
        '2': ["Platform 1", "YES"],
        '3': ["Platform 2", "NO"],
        '4': ["Platform 3", "YES"]
    }

    test_visited = ['1', '4', '3']

    print(BLUE + f"BEFORE: {test_spaces}" + DEFAULT)
    test_spaces = swap(test_spaces, test_visited)
    print(BLUE + f"AFTER: {test_spaces}" + DEFAULT)

    print(GREEN + "Test was successful" + DEFAULT)
