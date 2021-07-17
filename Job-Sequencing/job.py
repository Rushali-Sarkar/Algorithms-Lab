import heapq

def sequenceJob(jobs: [str], profits: [int], deadlines: [int]) -> [str]:

    maximum_time = max(deadlines)
    sequence = [None for i in range(maximum_time)]
    profit = 0

    def isPossible(deadline: int) -> int:
        for i in range(deadline - 1, -1, -1):
            if sequence[i] == None:
                return i
        return -1

    maxheap = []
    for i in range(len(profits)):
        heapq.heappush(maxheap, [profits[i] * -1, i])

    while len(maxheap) != 0:
        current_index = maxheap[0][1]
        heapq.heappop(maxheap)
        possible_index = isPossible(deadlines[current_index])
        if possible_index != -1:
            profit += profits[current_index]
            sequence[possible_index] = jobs[current_index]
    return profit, sequence

if __name__ == "__main__":

    print("Enter the jobs")
    jobs = list(map(str, input().split()))
    print("Enter the profits")
    profits = list(map(int, input().split()))
    print("Enter the deadlines")
    deadlines = list(map(int, input().split()))

    profit, sequence = sequenceJob(jobs, profits, deadlines)
    print("Maximum possible profit is: ", profit)
    print("The sequencing according to deadline is: ")
    print(sequence)
    
