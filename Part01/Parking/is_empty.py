from Parking.colors import *


def is_empty(spaces, goal_state):
    for i in range(1, len(spaces) + 1):
        if spaces[str(i)][0][:1] == 'E' or spaces[str(i)][1] != "NO" or goal_state[spaces[str(i)][0]] == "NO":
            continue

        return str(i)


if __name__ == '__main__':
    print(GREEN + "Start of is_empty Test" + DEFAULT)

    test_spaces = {
        '1': ["Empty"],
        '2': ["Platform 1", "YES"],
        '3': ["Platform 2", "NO"],
        '4': ["Platform 3", "YES"]
    }

    test_goal_state = {
        "Empty": "NO",
        "Platform 1": "YES",
        "Platform 2": "YES",
        "Platform 3": "YES"
    }

    print(BLUE + f"Output: {is_empty(test_spaces, test_goal_state)}" + DEFAULT)

    print(GREEN + "Test was successful" + DEFAULT)
