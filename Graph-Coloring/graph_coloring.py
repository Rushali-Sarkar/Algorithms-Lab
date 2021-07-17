def graphColoring(adjacency_matrix: [[int]], colors: [str]) -> [str]:

    if len(colors) == 0:
        return [-1]

    nodes = len(adjacency_matrix)
    coloring = [None for i in range(nodes)]

    def isColorPossible(node: int, color: str) -> bool:
        for i in range(nodes):
            if adjacency_matrix[node][i] == 1 and coloring[i] == color:
                return False
        return True


    def backtracking(current_node: int, visited: set()) -> bool:

        if len(visited) == nodes:
            return True

        for i in range(nodes):
            if i not in visited and adjacency_matrix[current_node][i] == 1:
                visited.add(i)
                for each in colors:
                    if isColorPossible(i, each):
                        coloring[i] = each
                        if backtracking(i, visited):
                            return True
                visited.remove(i)
        return False

    coloring[0] = colors[0]
    if backtracking(0, set([0])):
        return coloring
    return [-1]

if __name__ == "__main__":

    print("Enter the number of nodes")
    nodes = int(input())
    print("Enter the number of edges")
    edges = int(input())
    print("Enter all the edges")
    adjacency_matrix = [[0 for i in range(nodes)] for j in range(nodes)]
    for i in range(edges):
        u, v = list(map(int, input().split()))
        adjacency_matrix[u][v] = 1
        adjacency_matrix[v][u] = 1
    print("Enter the colors")
    colors = list(map(str, input().split()))
    coloring = graphColoring(adjacency_matrix, colors)
    if coloring == [-1]:
        print("Sorry Coloring not Possible")
    else:
        print("Coloring Possible in the order: ")
        print(coloring)



