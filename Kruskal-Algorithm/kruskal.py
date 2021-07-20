class DisjointSet:

    def __init__(self, parent = -1, rank = 0):
        self.parent = parent
        self.rank = rank


def kruskals(edge_list: [[int]], vertices: int, edges: int) -> [[int]]:
    minimum_spanning_tree = []
    disjoint_set = [DisjointSet() for i in range(vertices)]

    def find(vertice: int) -> int:
        if disjoint_set[vertice].parent == -1:
            return vertice
        disjoint_set[vertice].parent = find(disjoint_set[vertice].parent)
        return disjoint_set[vertice].parent

    def union_operator(from_parent: int, to_parent: int) -> None:
        if disjoint_set[from_parent].rank > disjoint_set[to_parent].rank:
            disjoint_set[to_parent].parent = from_parent
        elif disjoint_set[from_parent].rank < disjoint_set[to_parent].rank:
            disjoint_set[from_parent].parent = to_parent
        else:
            disjoint_set[from_parent].parent = to_parent
            disjoint_set[to_parent].rank += 1
        return None


    edge_list = sorted(edge_list)
    i = 0
    j = 0
    while i < vertices - 1 and j < edges:
        from_parent = find(edge_list[j][1])
        to_parent = find(edge_list[j][2])

        if from_parent == to_parent:
            j = j + 1
            continue
        union_operator(from_parent, to_parent)
        minimum_spanning_tree.append(edge_list[j])
        i = i + 1
    return minimum_spanning_tree

def print_tree(minimum_spanning_tree: [[int]]) -> None:
    for w, u, v in minimum_spanning_tree:
        print("Source: ", u, "To: ", v, "Weight: ", w)
    return None


if __name__ == "__main__":

    print("Enter the number of vertices")
    vertices = int(input())
    print("Enter the number of edges")
    edges = int(input())
    edge_list = []
    print("Enter the edges with the edge weights")
    for i in range(edges):
        u, v, w = list(map(int, input().split()))
        edge_list.append([w, u, v])
    minimum_spanning_tree = kruskals(edge_list, vertices, edges)
    print_tree(minimum_spanning_tree)
    



