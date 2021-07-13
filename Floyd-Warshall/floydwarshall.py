def floydwarshall(adjacency_matrix: [[int]]) -> [[int]]:
    nodes = len(adjacency_matrix)
    for i in range(nodes):
        for j in range(nodes):
            for k in range(nodes):
                if i == j:
                    if min(adjacency_matrix[i][j], adjacency_matrix[i][k] + adjacency_matrix[k][j]) < 0:
                        return [[-1]]
                elif k != i and k != j:
                    adjacency_matrix[i][j] = min(adjacency_matrix[i][j], adjacency_matrix[i][k] + adjacency_matrix[k][j])
    return adjacency_matrix


if __name__ == "__main__":

    print("Enter the number of nodes in the graph")
    n = int(input())
    print("Enter the adjacency matrix row wise")
    adjacency_matrix = []
    for i in range(n):
        row = list(map(float, input().split()))
        adjacency_matrix.append(row)
    adjacency_matrix = floydwarshall(adjacency_matrix)
    print("All Pair Shortest Path are: ")
    if adjacency_matrix == [[-1]]:
        print("Sorry cannot find all pair shortest path")
        print("Negative edge weight cycle is present")
    else:
        for each in adjacency_matrix:
            print(each)
