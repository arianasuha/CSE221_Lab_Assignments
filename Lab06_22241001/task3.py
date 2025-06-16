import heapq

def dijkstra_func(adjList, n):
    distance = [float("inf")] * (n + 1)
    distance[1] = 0
    visited = [False] * (n + 1)
    pri_q = [(0, 1)]
    
    while len(pri_q) != 0:
        curr_min_dis, node = heapq.heappop(pri_q)
        if node in visited:
            continue
        else:
            visited[node] = True

        for neighbor_node, cost in adjList[node]:
            new_dis = curr_min_dis if curr_min_dis > cost else cost
            if new_dis < distance[neighbor_node]:
                distance[neighbor_node] = new_dis
                heapq.heappush(pri_q, (new_dis, neighbor_node))

    return distance

   
def func1(file, output):
    n, m = map(int, file.readline().split())
    adjList = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v, w = map(int, file.readline().split())
        adjList[u].append((v, w))

    result = dijkstra_func(adjList, n)
    if result[n] == float("inf"):
        output.write("Impossible")
    else:
        output.write(f"{result[n]}")


file1 = open("input3_1.txt","r")
output1 = open("output3_1.txt","w")
func1(file1,output1)
file2 = open("input3_2.txt","r")
output2 = open("output3_2.txt","w")
func1(file2,output2)
file1.close()
output1.close()
file2.close()
output2.close()