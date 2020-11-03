from Parking.colors import *


# Μέθοδος που υλοποιείται ο αλγόριθμος DFS σε Python
def dfs(graph, node, goal, path=None):
    if path is None:
        path = [node]

    if node == goal:
        yield path

    for next_node in graph[node] - set(path):
        yield from dfs(graph, next_node, goal, path + [next_node])


# Επείδηξη λειτουργίας του DFS αλγορίθμου
if __name__ == '__main__':
    print(GREEN + "Start of DFS Test" + DEFAULT)

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
        # Το dfs απο μόνο του επιστρέφει generator, εμείς το μετατρέπουμε σε λίστα. Θα πάρουμε την μόρφη [[...],...]
        visited = list(dfs(test_graph, str(i), '5'))
        print(BLUE + f"{i}) Visited: {visited}" + DEFAULT)

        if len(visited) != 0:
            visited = min(visited, key=len)
            print(BLUE + f"Fastest path: {visited}" + DEFAULT)

        else:
            print(BLUE + "There is no path" + DEFAULT)

    print(GREEN + "Test was successful" + DEFAULT)

    '''
    Αρχίκα θα έχουμε τον πίνακα που βλέπουμε στην άρχη. Αυτός ο πίνακας μας δείχνει τις σχέσεις που έχει κάθε
    κόμβος με αλλούς (δηλαδή ποιοι είναι οι γειτονές τους). Ο ίδιος ο αλγόριθμος κοιτάει αυτές τις σχέσεις και
    σχηματίζει 2 διαφορετικά μονοπάτια για να φτάσουμε από τον αρχικό κόμβο στον τελικό μας (στο τεστ ήταν το 3, 
    στο κανονικό πρόγραμμα θα είναι σε όποιο έχει ιδιότητα empty). Παράδειγμα, εάν θέλουμε να πάμε από το 2 στο 3, 
    θα μας επιστρέψει δύο πιθανές διαδρομές, την 2 -> 1 -> 4 -> 3 και την 2 -> 3. Εμείς για να το επεξεργαστούμε και
    να συνεχίσουμε στο επόμενο βήμα (του swap), θα κρατήσουμε το δεύτερο επειδή είναι πιο γρήγορη συγκριτικά 
    με το πρώτο.
    '''
