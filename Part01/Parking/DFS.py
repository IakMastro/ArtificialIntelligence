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
        '1': set(['2', '4']),
        '2': set(['1', '3']),
        '3': set(['2', '4']),
        '4': set(['1', '3'])
    }

    print(BLUE + f"Starting point: {test_graph}" + DEFAULT)

    # Κάνουμε με 4 διαφορετικούς για να δούμε όλους τους πιθανούς συνδιασμούς για να φτάσουμε στο 3.
    for i in range(1, 5):
        # Το dfs απο μόνο του επιστρέφει generator, εμείς το μετατρέπουμε σε λίστα. Θα πάρουμε την μόρφη [[...],...]
        visited = list(dfs(test_graph, str(i), '3'))
        print(BLUE + f"{i}) Visited: {visited}" + DEFAULT)

        # Εδώ κοιτάμε τι μας έχει επιστρέψει το DFS. Εάν το μέγεθος είναι ίσο με το 1, απλώς πέρνουμε αυτό και το
        # μετατρέπουμε σε μονοδιάστατη λίστα, από δυσδιάστατη
        if len(visited) == 1:
            visited = visited[0]

        # Εδώ κοιτάμε πια λίστα θα έχει παραπάνω steps και κρατάμε αυτήν που έχει λιγότερα. Εάν έχουν το ίδιο κρατάμε
        # την δεύτερη τυχαία.
        elif len(visited[0]) >= len(visited[1]):
            visited = visited[1]

        else:
            visited = visited[0]

        print(BLUE + f"Fastest path: {visited}" + DEFAULT)

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