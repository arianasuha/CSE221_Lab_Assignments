# 6

def func1(stack, matrix, visited, neighbour, r, h):
  count = i = j = k = l = 0
  while len(stack) != 0:
    i, j = stack[-1]
    stack.pop()
    if 0 <= i < r and 0 <= j < h and matrix[i][j] != "#" and visited[i][j] == False:
      visited[i][j] = True
      if matrix[i][j] == "D":
        count += 1
      for i3 in neighbour:
        k = i + i3[0]
        l = j + i3[1]
        if  0 <= k < r and 0 <= l < h and visited[k][l] == False and matrix[k][l] != "#":
          stack += [(k, l)]
  return count


def diamond_find(file, output):
  r, h = map(int, file.readline().rstrip().split(" "))
  count = 0
  dia_count = []
  neighbour = [(1, 0), (-1, 0), (0, -1), (0, 1)]
  matrix = []
  stack = []
  for i1 in range(r):
    matrix += [file.readline()]
  visited = []
  for i2 in range(r):
    visited += [[False] * h]
  for row in range(r):
    for col in range(h):
      if matrix[row][col] == "." or matrix[row][col] == "D" and visited[row][col] == False:
        stack += [(row, col)]
        count = func1(stack, matrix, visited, neighbour, r, h)
      dia_count += [count]
  output.write(str(max(dia_count)))


file1 = open("input6_1.txt", "r")
output1 = open("output6_1.txt", "w")
diamond_find(file1, output1)
file2 = open("input6_2.txt", "r")
output2 = open("output6_2.txt", "w")
diamond_find(file2, output2)
file3 = open("input6_3.txt", "r")
output3 = open("output6_3.txt", "w")
diamond_find(file3, output3)
file4 = open("input6_4.txt", "r")
output4 = open("output6_4.txt", "w")
diamond_find(file4, output4)
file5 = open("input6_5.txt", "r")
output5 = open("output6_5.txt", "w")
diamond_find(file5, output5)
file6 = open("input6_6.txt", "r")
output6 = open("output6_6.txt", "w")
diamond_find(file6, output6)
file7 = open("input6_7.txt", "r")
output7 = open("output6_7.txt", "w")
diamond_find(file7, output7)
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
file6.close()
output6.close()
file7.close()
output7.close()
