from Parking.DFS import dfs
from Parking.swap import swap
from Parking.is_empty import is_empty
from Parking.colors import *

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
        '2': ["Platform 1", "NO"],
        '3': ["Platform 2", "NO"],
        '4': ["Platform 3", "NO"],
        '5': ["Platform 4", "NO"],
        '6': ["Platform 5", "NO"]
    }

    while True:
        query = input(BLUE + "Waiting for a query: " + GREEN)
        query = query.split(" ")

        if query[0].strip() == 'help':
            print(BLUE + "HELP I NEED ANYBODY HELP NOT JUST ANYBODY HELP I JUST NEED SOMEONE HEEEEEEEEEEEEEELP")

        elif query[0] == "fill":
            goal = is_empty(spaces)
            if goal is None:
                print(RED + f"No space for {query[1].strip()}" + DEFAULT)

            else:
                visited = min(list(dfs(neighbours, '1', goal)), key=len)
                swap(spaces, visited)
                spaces['1'][1] = query[1].strip()
                print(BLUE + f"Filled {spaces['1'][0]} with a" + GREEN + f" {spaces['1'][1]}" + DEFAULT)

        elif query[0] == 'exit':
            print(BLUE + "Exiting..." + DEFAULT)
            break

        else:
            print(RED + "Unexpected command. Try help." + DEFAULT)
