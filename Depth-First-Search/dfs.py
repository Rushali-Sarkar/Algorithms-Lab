def dfs(source: int, adjacency_list: {int: [int]}) -> None:

    visited = set()
    def recurse(source: int) -> None:
        if source in visited:
            return None
        visited.add(source)
        print(source, end = " ")
        if source in adjacency_list:
            for each in adjacency_list[source]:
                recurse(each)
        return None
    recurse(source)
    print()
    return None

if __name__ == "__main__":
    print("Enter the number of edges")
    edges = int(input())
    adjacency_list = {}
    print("Enter all the edges")
    for i in range(edges):
        u, v = list(map(int, input().split()))
        if u not in adjacency_list:
            adjacency_list[u] = [v]
        else:
            adjacency_list[u].append(v)
    print("Enter the starting node")
    source = int(input())
    dfs(source, adjacency_list)

