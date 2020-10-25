from colors import *


# Μέθοδος που υλοποιείται ο αλγόριθμος DFS σε Python
def dfs(node, graph, found=False, visited=None):
    if visited is None:
        visited = []

    # Εάν ο κόμβος δεν είναι στην λίστα visited (δηλαδή δεν το έχει επισκεφτεί ακόμα)
    if node not in visited:
        # Το προσθέτει στην λίστα από αυτών που τους έχει επισκεφτεί
        visited.append(node)

        if graph[node][0] == "EMPTY" and not found:
            found = True

        elif not found:
            # Για κάθε γειτωνικό κόμβο που του κόμβου, ξανατρέξε το DFS με τον νέο κόμβο
            for n in graph[node]:
                if n[:1] == 'P':
                    continue

                dfs(n, graph, found, visited)

        return visited


# Επείδηξη λειτουργίας του DFS αλγορίθμου
if __name__ == '__main__':
    print(GREEN + "Start of DFS Test" + DEFAULT)

    test_graph = {
        '1': ["PLATFORM 1", '2', '4'],
        '2': ["PLATFORM 2", '1', '3'],
        '3': ["EMPTY", '2', '4'],
        '4': ["PLATFORM 3", '1', '3']
    }

    for i in range(1, 5):
        print(BLUE + f"{i}) Visited: {dfs(str(i), test_graph)}" + DEFAULT)

    print(GREEN + "Test was successful" + DEFAULT)

    '''
    
    '''
