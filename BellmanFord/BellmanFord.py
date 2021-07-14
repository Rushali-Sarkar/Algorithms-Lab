import heapq

def bellmanford(edges: [[int]], nodes: int, source: int) -> [int]:

    min_distances = []
    for node in range(nodes):
        if node == source:
            min_distances.append(0)
        else:
            min_distances.append(float('inf'))

    for i in range(1, nodes):
        for u, v, w in edges:
            distance = min_distances[u] + w
            if distance < min_distances[v]:
                min_distances[v] = distance

    return min_distances


if __name__ == "__main__":

    print("Enter the number of nodes")
    nodes = int(input())
    print("Enter the number of edges")
    edges = int(input())
    print("Enter all the edges with their weights")
    edges_list = []
    for i in range(edges):
        u, v, w = list(map(int, input().split()))
        edges_list.append([u, v, w])
    print("Enter the source")
    source = int(input())
    min_distances = bellmanford(edges_list, nodes, source)
    print("The single source shortest path distances are: ")
    print(min_distances)


