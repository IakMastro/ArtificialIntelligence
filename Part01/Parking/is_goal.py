from Parking.colors import *


# Συνάρτηση που βλέπει κάθε node του state και το συγκρίνει με το παρόμοιο του.
def is_goal(state, goal_state):
    for node in state:
        if state[node] != goal_state[node]:
            return False

    return True


if __name__ == '__main__':
    print(GREEN + "Start of is_goal Test" + DEFAULT)

    test_state1 = {
        "Platform1": "Yes",
        "Platform2": "Yes",
        "Platform3": "Yes",
        "Empty": "No"
    }

    test_state2 = {
        "Platform1": "No",
        "Platform2": "Yes",
        "Platform3": "Yes",
        "Empty": "No"
    }

    test_goal = {
        "Platform1": "Yes",
        "Platform2": "Yes",
        "Platform3": "Yes",
        "Empty": "No"
    }

    if is_goal(test_state1, test_goal):
        print(BLUE + "We have reached the goal for test_state1" + DEFAULT)

    else:
        print(BLUE + "We haven't reached the goal for test_state1" + DEFAULT)

    if is_goal(test_state2, test_goal):
        print(BLUE + "We have reached the goal for test_state2" + DEFAULT)

    else:
        print(BLUE + "We haven't reached the goal for test_state2" + DEFAULT)

    print(GREEN + "Test was successful" + DEFAULT)
