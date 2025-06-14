# 5

def bfs_func(queue, visited, adj_list, dict1):
  new_list = []
  dict1[queue[0]] = None
  while len(queue) != 0:
    new_list = adj_list[queue[0]]
    if len(new_list) != 0:
      for j in new_list:
        if j not in visited and j not in queue:
          queue += [j]
        if j not in dict1:
          dict1[j] = queue[0]
    visited += [queue[0]]
    queue.pop(0)

def traverse_func(file, output):
  n, e, d = map(int, file.readline().rstrip().split(" "))
  visited = []
  queue = [1]
  adj_list = []
  dict1 = {}
  ver1 = ver2 = 0
  for iter1 in range(n + 1):
    adj_list += [[]*(n + 1)]
  for iter2 in range(e):
    ver1, ver2 = map(int, file.readline().rstrip().split(" "))
    adj_list[ver1] += [ver2]
    adj_list[ver2] += [ver1]
  bfs_func(queue, visited, adj_list, dict1)
  path = [d]
  time = 0
  temp = d
  while path[-1] != 1:
    path += [dict1[temp]]
    time += 1
    temp = dict1[temp]
  output.write("Time: " + str(time) + "\n")
  output.write("Shortest Path:")
  for iter3 in range(len(path)-1, -1, -1):
    output.write(" " + str(path[iter3]))


file1 = open("input5_1.txt", "r")
output1 = open("output5_1.txt", "w")
traverse_func(file1, output1)
file2 = open("input5_2.txt", "r")
output2 = open("output5_2.txt", "w")
traverse_func(file2, output2)
file3 = open("input5_3.txt", "r")
output3 = open("output5_3.txt", "w")
traverse_func(file3, output3)
file4 = open("input5_4.txt", "r")
output4 = open("output5_4.txt", "w")
traverse_func(file4, output4)
file5 = open("input5_5.txt", "r")
output5 = open("output5_5.txt", "w")
traverse_func(file5, output5)
file1.close()
output1.close()
file2.close()
output2.close()
file3.close()
output3.close()
file4.close()
output4.close()
file5.close()
output5.close()