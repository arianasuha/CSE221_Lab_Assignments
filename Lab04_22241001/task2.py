# 2

def bfs_func(queue, visited, adj_list):
  new_list = []
  while len(queue) != 0:
    new_list = adj_list[queue[0]]
    if len(new_list) != 0:
      for j in new_list:
        if j not in visited and j not in queue:
          queue += [j]
    visited += [queue[0]]
    queue.pop(0)


def traverse_func(file, output):
  n, e = map(int, file.readline().rstrip().split(" "))
  visited = []
  queue = [1]
  adj_list = []
  ver1 = ver2 = 0
  for iter1 in range(n + 1):
    adj_list += [[]*(n + 1)]
  for iter2 in range(e):
    ver1, ver2 = map(int, file.readline().rstrip().split(" "))
    adj_list[ver1] += [ver2]
    adj_list[ver2] += [ver1]
  bfs_func(queue, visited, adj_list)
  for iter3 in visited:
    output.write(str(iter3) + " ")


file1 = open("input2_1.txt", "r")
output1 = open("output2_1.txt", "w")
traverse_func(file1, output1)
file2 = open("input2_2.txt", "r")
output2 = open("output2_2.txt", "w")
traverse_func(file2, output2)
file3 = open("input2_3.txt", "r")
output3 = open("output2_3.txt", "w")
traverse_func(file3, output3)
file4 = open("input2_4.txt", "r")
output4 = open("output2_4.txt", "w")
traverse_func(file4, output4)
file1.close()
output1.close()
file2.close()
output2.close()
file3.close()
output3.close()
file4.close()
output4.close()