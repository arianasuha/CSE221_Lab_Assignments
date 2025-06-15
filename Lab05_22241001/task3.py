# 3

def dfs1(adjL, visited, stack, v):
  if visited[v] != 1:
    visited[v] = 1
  if len(adjL[v]) != 0:
    for i3 in adjL[v]:
      if visited[i3] == 0:
        dfs1(adjL, visited, stack, i3)
  if v not in stack:
    stack += [v]


def dfs2(adjL, visited, stack, u, opt):
  if visited[u] != 1:
    visited[u] = 1
    opt[-1] += [u]
  if len(adjL[u]) != 0:
    for i4 in adjL[u]:
      if visited[i4] == 0:
        dfs2(adjL, visited, stack, i4, opt)


def adjList(file, n, m):
  tpzL = [[] for _ in range(n + 1)]
  adjL = [[] for _ in range(n + 1)]
  integers = ""
  a = b = 0
  for i2 in range(m):
    integers = file.readline().rstrip().split(" ")
    a, b = int(integers[0]), int(integers[1])
    adjL[a] += [b]
    tpzL[b] += [a]
  return adjL, tpzL


def strongly_connected(file, output):
  integers = file.readline().rstrip().split(" ")
  n, m = int(integers[0]), int(integers[1])
  adjL, tpzL = adjList(file, n, m)
  visited1 = [0] * (n + 1)
  stack = []
  v = 1
  while v <= n:
    if visited1[v] != 1:
      dfs1(adjL, visited1, stack, v)
    v += 1

  visited2 = [0] * (n + 1)
  opt = []
  while len(stack) != 0:
    if visited2[stack[-1]] == 0:
      opt += [[]]
      dfs2(tpzL, visited2, stack, stack[-1], opt)
    stack.pop()
  for i5 in sorted(opt):
    for i6 in sorted(i5):
      output.write(str(i6) + " ")
    output.write("\n")


file1 = open("input3_1.txt", "r")
output1 = open("output3_1", "w")
strongly_connected(file1, output1)
file2 = open("input3_2.txt", "r")
output2 = open("output3_2", "w")
strongly_connected(file2, output2)
file3 = open("input3_3.txt", "r")
output3 = open("output3_3", "w")
strongly_connected(file3, output3)
file1.close()
output1.close()
file2.close()
output2.close()
file3.close()
output3.close()