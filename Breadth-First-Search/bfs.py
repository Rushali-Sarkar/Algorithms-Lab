def bfs(adjacency_list: {int: [int]}, source: int) -> None:

    queue = [source]
    visited = set()
    while len(queue) != 0:

        current_level = len(queue)
        for i in range(current_level):
            node = queue[0]
            queue.pop(0)
            if node not in visited:
                visited.add(node)
                print(node, end = " ")
                if node in adjacency_list and len(adjacency_list[node]) != 0:
                    for each in adjacency_list[node]:
                        queue.append(each)
    print()
    return None

if __name__ == "__main__":

    print("Enter the number of edges")
    edges = int(input())
    print("Enter the edges")
    adjacency_list = {}
    for i in range(edges):
        u, v = list(map(int, input().split()))
        if u in adjacency_list:
            adjacency_list[u].append(v)
        else:
            adjacency_list[u] = [v]
    print("Enter the starting point")
    source = int(input())
    bfs(adjacency_list, source)
