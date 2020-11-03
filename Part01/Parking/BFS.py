from Parking.colors import *


# Μέθοδος που υλοποιείται ο αλγόριθμος BFS σε Python
def bfs(graph, node, goal):
    queue = [(node, [node])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


# Επείδηξη λειτουργίας του BFS αλγορίθμου
if __name__ == '__main__':
    print(GREEN + "Start of BFS Test" + DEFAULT)

    test_graph = {
        '1': set(['2', '3']),
        '2': set(['1', '4', '5']),
        '3': set(['1']),
        '4': set(['2', '5']),
        '5': set(['2', '4'])
    }

    print(BLUE + f"Starting point: {test_graph}" + DEFAULT)

    # Κάνουμε με 5 διαφορετικούς για να δούμε όλους τους πιθανούς συνδιασμούς για να φτάσουμε στο 5.
    for i in range(1, 6):
        # Το bfs απο μόνο του επιστρέφει generator, εμείς το μετατρέπουμε σε λίστα. Θα πάρουμε την μόρφη [[...],...]
        visited = list(bfs(test_graph, str(i), '5'))
        print(BLUE + f"{i}) Visited: {visited}" + DEFAULT)

        if len(visited) != 0:
            visited = min(visited, key=len)
            print(BLUE + f"Fastest path: {visited}" + DEFAULT)

        else:
            print(BLUE + "There is no path" + DEFAULT)

    print(GREEN + "Test was successful" + DEFAULT)

    '''
    Η λειτουργία του BFS είναι πολύ παρόμοια απο αυτή του BFS. Στο δικό μας παράδειγμα, δεν υπάρχει καμία διαφορά
    εκτός άμα το goal είναι το αρχικό node. Εκεί δεν μας επιστρέφει path, αφού δεν υπάρχει.
    '''
