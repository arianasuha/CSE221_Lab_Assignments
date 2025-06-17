def find_rank(ind , list1 ):
    if ind == list1[ind][0]:
        return ind
    else:
        return find_rank(list1[ind][0] , list1)
    
def func1(file, out):
    x,y = file.readline().split(" ")
    rank = [None]* int(x)
    for i in range(int(x)):
        rank[i] = [i,1]
    for j in range(int(y)):
        k,q = file.readline().split(" ")
        k = int(k)
        q = int(q)
        u = find_rank(k,rank)
        v = find_rank(q,rank)
        if u != v:
            rank[u] = [u , rank[u][1] + rank[v][1]]
            rank[q] =  [ u ,  rank[q][1]]
        out.write(f"{rank[u][1]}\n")
 

file1 =  open("input1_1.txt","r")
output1 = open("output1_1.txt","w")
func1(file1, output1)
file2 =  open("input1_2.txt","r")
output2 = open("output1_2.txt","w")
func1(file2, output2)
file1.close()
output1.close()
file2.close()
output2.close()
