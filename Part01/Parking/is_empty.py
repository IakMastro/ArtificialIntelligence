from Parking.colors import *


# Συνάρτηση που βρίσκει την άδεια θέση ενός state. Eάν δεν υπάρχει, στέλνει None.
def is_empty(spaces, goal_state):
    for i in range(1, len(spaces) + 1):
        if spaces[str(i)][0][:1] == 'E' or spaces[str(i)][1] != "NO" or goal_state[spaces[str(i)][0]] == "NO":
            continue

        return str(i)


# Επείδηξη λειτουργίας της συνάρτησης is_empty.
if __name__ == '__main__':
    print(GREEN + "Start of is_empty Test" + DEFAULT)

    test_spaces = {
        '1': ["Empty"],
        '2': ["Platform 1", "YES"],
        '3': ["Platform 2", "NO"],
        '4': ["Platform 3", "YES"]
    }

    print(BLUE + f"Output: {is_empty(test_spaces)}" + DEFAULT)

    print(GREEN + "Test was successful" + DEFAULT)
