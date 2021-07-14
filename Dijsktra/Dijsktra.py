import heapq
def makeAdjacencyList(graph: [[int]]) -> {int: [[int]]}:
    adjacency_list = {}
    for u, v, w in graph:
        if u in adjacency_list:
            adjacency_list[u].append([v, w])
        else:
            adjacency_list[u] = [[v, w]]
        if v in adjacency_list:
            adjacency_list[v].append([u, w])
        else:
            adjacency_list[v] = [[u, w]]
    return adjacency_list

def dijsktra(graph: {int: [[int]]}, source: int, nodes: int) -> ([int], [int]):

        min_distance = []
        processed = set([])
        parents = []

        for i in range(nodes):
            if i == source:
                min_distance.append(0)
            else:
                min_distance.append(float('inf'))
            parents.append(-1)

        minheap = []
        parents[source] = source
        heapq.heappush(minheap, [0, source])
        

        while len(minheap) != 0:

            w, v = minheap[0]
            heapq.heappop(minheap)

            if v not in processed:
                processed.add(v)
                for each, weight in graph[v]:
                    if w + weight < min_distance[each]:
                        min_distance[each] = w + weight
                        parents[each] = v
                    heapq.heappush(minheap, [w + weight, each])

        return min_distance, parents 



if __name__ == "__main__":
    print("Enter the number of nodes")
    nodes = int(input())
    print("Enter the number of edges")
    edges = int(input())
    print("Enter the edges with the edge weights")
    graph = []
    for i in range(edges):
        edge = list(map(int, input().split()))
        graph.append(edge)
    print("Enter the source")
    source = int(input())
    adjacency_list = makeAdjacencyList(graph)
    min_distances, shortest_path_graph = dijsktra(adjacency_list, source, nodes)
    print("The minimum distances is")
    print(min_distances)
    print("The Shortest Path Graph is")
    print(shortest_path_graph)
