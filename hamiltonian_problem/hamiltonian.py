def hamiltoniancycle(adjacency_matrix: [[int]]) -> [int]:

    starting_vertex = 0
    nodes = len(adjacency_matrix)

    def backtrack(current_vertex: int, visited: [int]) -> (bool, [int]):

        if len(visited) == nodes:
            if adjacency_matrix[current_vertex][starting_vertex] == 1:
                return True, [starting_vertex]
            return False, -1


        for i in range(nodes):
            if i not in visited and adjacency_matrix[current_vertex][i] == 1:
                visited.add(i)
                isPossible, path = backtrack(i, visited)
                if isPossible:
                    return True, [i] + path
                visited.remove(i)
        return False, [-1]

    isPossible, path = backtrack(0, set([0]))
    if not isPossible:
        return [-1]
    return [0] + path


if __name__ == "__main__":

    print("Enter the number of nodes")
    nodes = int(input())
    adjacency_matrix = [[0 for j in range(nodes)]for i in range(nodes)]
    print("Enter the number of edges")
    edges = int(input())
    print("Enter " , edges, " edges")
    for i in range(edges):
        u, v = list(map(int, input().split()))
        adjacency_matrix[u][v] = 1
        adjacency_matrix[v][u] = 1
    hamiltonian_cycle = hamiltoniancycle(adjacency_matrix)
    if hamiltonian_cycle == [-1]:
        print("Sorry no hamiltonian cycle possible")
    else:
        print("Possible Hamiltonian cycle is")
        print(hamiltonian_cycle)









