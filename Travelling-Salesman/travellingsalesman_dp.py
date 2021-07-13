def travellingSalesman(adjacency_matrix: [[int]], starting_point: int)-> (int, [int]):

    total_nodes = len(adjacency_matrix)
    remaining_nodes = set([])
    for i in range(total_nodes):
        if i != starting_point:
            remaining_nodes.add(i)
    def findPath(current_position: int, remaining_positions: set([])) -> (int, [int]):
        if len(remaining_positions) == 0:
            return adjacency_matrix[current_position][starting_position], [starting_point]
        min_cost = float('inf')
        min_path = []
        for each in remaining_positions:
            cost, path = findPath(each, remaining_positions - set([each]))
            cost = cost + adjacency_matrix[current_position][each]
            if cost < min_cost:
                min_cost = cost
                min_path = [each] + path
        return min_cost, min_path
            
    return findPath(starting_point, remaining_nodes)


if __name__ == "__main__":

    print("Enter the number of nodes ")
    nodes = int(input())
    print("Enter the adjacency matrix row wise")
    adjacency_matrix = []
    for i in range(nodes):
        row = list(map(int, input().split()))
        adjacency_matrix.append(row)
    print("Enter the starting position")
    starting_position = int(input())
    cost, path = travellingSalesman(adjacency_matrix, starting_position)
    print("The distance travelled is: ", cost, " units")
    path = [starting_position] + path
    print("The path traversed is: ")
    print(path)
