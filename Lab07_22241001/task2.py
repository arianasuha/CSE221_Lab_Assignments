
import heapq as h
def rank_finder(ind, list1):
    if ind == list1[ind][0]:
        return ind
    else:
        return rank_finder(list1[ind][0], list1)
def func1(file, output):  
    
    x,y = file.readline().split(" ")
    lis1, lis2 = [], []
    distance = 0
    rank = [None] * (int(x) + 1)
    for i in range(int(x) + 1):
        rank[i] = [i,1]

    for j in range(int(y)):
        k, q, z = file.readline().split(" ")
        k, q, z = int(k), int(q), int(z)
        h.heappush(lis1, [z,k,q])

    while len(lis1) != 0:
        p = h.heappop(lis1)
        a, b, c = p
        u = rank_finder(b, rank)
        v = rank_finder(c, rank)
        if u != v:
                if rank[u][1] >= rank[v][1]:
                    rank[u] =  [u ,  rank[u][1] + rank[v][1]]
                    rank[c] = [u, rank[c][1]]
                else:
                    rank[v] = [v, rank[v][1] + rank[u][1]]
                    rank[b] = [v, rank[b][1]]
                distance += p[0]
                lis2.append(p)
    output.write(f"{distance}\n")

file1 =  open("input2_1.txt","r")
output1 = open("output2_1.txt","w")
func1(file1, output1)
file2 =  open("input2_2.txt","r")
output2 = open("output2_2.txt","w")
func1(file2, output2)
file1.close()
output1.close()
file2.close()
output2.close()

