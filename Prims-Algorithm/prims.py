def selectMinVertex(vertices: int, value: [int], set_MST: [bool]) -> int:
    minimum = float('inf')
    vertex = 0
    for i in range(vertices):
        if set_MST[i] == False and value[i] < minimum:
            vertex = i
            minimum = value[i]
    return vertex

def prims(vertices: int, adjacency_matrix: [[int]]) -> [int]:

    minimum_spanning_graph = []
    parent = [-1 for i in range(vertices)]
    value =  [float('inf') for i in range(vertices)]
    set_MST = [False for i in range(vertices)]
    
    parent[0] = -1
    value[0] = 0

    for i in range(vertices - 1):
        u = selectMinVertex(vertices, value, set_MST)
        set_MST[u] = True
        for j in range(vertices):
            if adjacency_matrix[u][j] != 0 and set_MST[j] == False and adjacency_matrix[u][j] < value[j]:
                value[j] = adjacency_matrix[u][j]
                parent[j] = u
    return parent

def printGraph(parent: [int], adjacency_matrix: [[int]]) -> None:
    for i in range(len(parent)):
        print("Source -> Destination: ", parent[i], " -> ", i, " Weight = ", adjacency_matrix[parent[i]][i])
    return None

if __name__ == "__main__":

    print("Enter the number of vertices")
    vertices = int(input())
    adjacency_matrix = []
    print("Enter the adjacency matrix row wise")
    for i in range(vertices):
        row = list(map(int, input().split()))
        adjacency_matrix.append(row)
    minimum_spanning_graph = prims(vertices, adjacency_matrix)
    printGraph(minimum_spanning_graph, adjacency_matrix)
    
