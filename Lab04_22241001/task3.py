# 3

def dfs_func(stack, visited, adj_list):
  if len(stack) != 0:
    if stack[-1] not in visited:
      visited += [stack[-1]]
    for j in adj_list[stack[-1]]:
      if j not in visited:
        stack += [j]
        dfs_func(stack, visited, adj_list)
    stack.pop()



def traverse_func(file, output):
  n, e = map(int, file.readline().rstrip().split(" "))
  visited = [1]
  stack = [1]
  adj_list = []
  ver1 = ver2 = 0
  for iter1 in range(n + 1):
    adj_list += [[]*(n + 1)]
  for iter2 in range(e):
    ver1, ver2 = map(int, file.readline().rstrip().split(" "))
    adj_list[ver1] += [ver2]
    adj_list[ver2] += [ver1]
  dfs_func(stack, visited, adj_list)
  for iter3 in visited:
    output.write(str(iter3) + " ")


file1 = open("input3_1.txt", "r")
output1 = open("output3_1.txt", "w")
traverse_func(file1, output1)
file2 = open("input3_2.txt", "r")
output2 = open("output3_2.txt", "w")
traverse_func(file2, output2)
file3 = open("input3_3.txt", "r")
output3 = open("output3_3.txt", "w")
traverse_func(file3, output3)
file4 = open("input3_4.txt", "r")
output4 = open("output3_4.txt", "w")
traverse_func(file4, output4)
file1.close()
output1.close()
file2.close()
output2.close()
file3.close()
output3.close()
file4.close()
output4.close()