# 4

def dfs_func(stack, visited, adj_list, flag):
  if len(stack) != 0 and flag[0] != True:
    if stack[-1] not in visited:
      visited += [stack[-1]]
    for j in adj_list[stack[-1]]:
      if j not in visited:
        stack += [j]
        dfs_func(stack, visited, adj_list, flag)
      if j in visited and j in stack:
        flag[0] = True
        break
    stack.pop()


def traverse_func(file, output):
  n, e = map(int, file.readline().rstrip().split(" "))
  visited = [1]
  stack = [1]
  adj_list = []
  ver1 = ver2 = 0
  for i1 in range(n + 1):
    adj_list += [[]*(n + 1)]
  for i2 in range(e):
    ver1, ver2 = map(int, file.readline().rstrip().split(" "))
    adj_list[ver1] += [ver2]
  flag = [False]
  dfs_func(stack, visited, adj_list, flag)
  if flag[0] == False:
    output.write("NO")
  else:
    output.write("YES")


file1 = open("input4_1.txt", "r")
output1 = open("output4_1.txt", "w")
traverse_func(file1, output1)
file2 = open("input4_2.txt", "r")
output2 = open("output4_2.txt", "w")
traverse_func(file2, output2)
file3 = open("input4_3.txt", "r")
output3 = open("output4_3.txt", "w")
traverse_func(file3, output3)
file4 = open("input4_4.txt", "r")
output4 = open("output4_4.txt", "w")
traverse_func(file4, output4)
file5 = open("input4_5.txt", "r")
output5 = open("output4_5.txt", "w")
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