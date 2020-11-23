from Parking.find_solution import find_solution
from Parking.is_goal import is_goal
from Parking.colors import *

if __name__ == '__main__':
    print(GREEN + "Start of main program" + DEFAULT)

    # Οι γειτωνικές σχέσεις του γράφου
    neighbours = {
        '1': set(['2', '4']),
        '2': set(['1', '3']),
        '3': set(['2', '4', '6']),
        '4': set(['1', '3', '5']),
        '5': set(['4', '6']),
        '6': set(['3', '5'])
    }

    # Οι καταστάσεις που βρίσκετε το κάθε node στον γράφο
    spaces = {
        '1': ["Empty", "NO"],
        '2': ["Platform 1", "NO"],
        '3': ["Platform 2", "NO"],
        '4': ["Platform 3", "NO"],
        '5': ["Platform 4", "NO"],
        '6': ["Platform 5", "NO"]
    }

    # Το επιθυμιτό, τελικό αποτέλεσμα
    goal_state = {
        "Empty": "NO",
        "Platform 1": "YES",
        "Platform 2": "YES",
        "Platform 3": "YES",
        "Platform 4": "YES",
        "Platform 5": "YES"
    }

    print(GREEN + "INITIAL VALUES")
    print("NEIGHBOURS: " + BLUE + f"{neighbours}")
    print(GREEN + "SPACES: " + BLUE + f"{spaces}")
    print(GREEN + "GOAL STATE: " + BLUE + f"{goal_state}")

    method = input("Choose method you want to use.\nAvailable Methods DFS, BFS, BestFS: " + GREEN)

    while True:
        # Επέστρεψε την νέα μορφή των καταστάσεων του γράφουν.
        # Εάν εγίνε κάτι λάθος στην πορεία του προγράμματος, επιστρέφει empty και
        # λήγει το πρόγραμμα.
        spaces = find_solution(neighbours, spaces, goal_state, method)
        if spaces is None:
            break

        print(GREEN + "NEW STATE: " + BLUE + f"{spaces}")

        state = dict()
        for node in spaces:
            state[spaces[node][0]] = spaces[node][1]

        if is_goal(state, goal_state):
            print(BLUE + "Found goal state..." + GREEN + "\nExiting" + DEFAULT)
            break
