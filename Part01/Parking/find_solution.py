from Parking.colors import *
from Parking.DFS import *
from Parking.BFS import *
from Parking.BestFS import *
from Parking.is_empty import *
from Parking.swap import *


def find_solution(neighbour_graph, space_graph, goal_state, method):
    # Πρώτα θα βρούμε σε ποια θέση βρίσκεται το πρώτο node, όπου έχει empty πλατφόρμα
    goal = is_empty(space_graph, goal_state)
    if goal is None:
        print(RED + "NO SOLUTION COULD BE FOUND" + DEFAULT)
        return None

    # Αναλόγως με την μέθοδο που έχουμε επιλέξει στην αρχή του προγράμματος,
    # θα πάρουμε και ένα διαφορετικό αποτέλεσμα. Κάθε αλγόριθμος επιστρέφει και διαφορετικό
    # πίνακα. Επειδή επιστρέφουν generator, εμείς το μετατρέπουμε σε λίστα.
    visited = []
    if method == "DFS":
        visited = list(dfs(neighbour_graph, '1', goal))

    elif method == "BFS":
        visited = list(bfs(neighbour_graph, '1', goal))

    elif method == "BestFS":
        visited = list(best_fs(neighbour_graph, '1', goal))

    else:
        print(RED + "METHOD NOT FOUND" + DEFAULT)
        return None

    # Από το Front, επιλέγει την πιο γρήγορη διαδρόμη, και στην συνέχεια κάνει την συνάρτηση swap για να
    # ανταλλάξει τα nodes μεταξύ τους και να φέρει το node με την άδεια πλατφόρμα στην θέση 1 του γράφου.
    print(GREEN + "FRONT: " + BLUE + f"{visited}")
    visited = min(visited, key=len)
    print(GREEN + "FASTEST SOLUTION: " + BLUE + f"{visited}")
    swap(space_graph, visited)
    space_graph['1'][1] = "YES"

    return space_graph


if __name__ == '__main__':
    print(GREEN + "Start of find_solution Test" + DEFAULT)

    test_neighbours = {
        '1': set(['2', '4']),
        '2': set(['1', '3']),
        '3': set(['2', '4', '6']),
        '4': set(['1', '3', '5']),
        '5': set(['4', '6']),
        '6': set(['3', '5'])
    }

    test_spaces = {
        '1': ["Empty", "NO"],
        '2': ["Platform 1", "NO"],
        '3': ["Platform 2", "NO"],
        '4': ["Platform 3", "NO"],
        '5': ["Platform 4", "NO"],
        '6': ["Platform 5", "NO"]
    }

    test_goal_state = {
        "Empty": "NO",
        "Platform 1": "NO",
        "Platform 2": "YES",
        "Platform 3": "YES",
        "Platform 4": "YES",
        "Platform 5": "YES"
    }

    find_solution(test_neighbours, test_spaces, test_goal_state,  "DFS")
    print(test_spaces)

    print(GREEN + "Test ended successfully" + DEFAULT)
