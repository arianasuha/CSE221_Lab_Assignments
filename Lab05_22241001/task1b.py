# 1B

def bfs(adjL, queue, inC, n, m, otp):
  cv = 0
  while len(queue) != 0:
    cv = queue[0]
    otp += [queue[0]]
    queue.pop(0)
    if len(adjL[cv]) != 0:
      for i5 in adjL[cv]:
        inC[i5] -= 1
        if inC[i5] == 0:
          queue += [i5]



def cycle_checker(stack, visited, adjL, flag):
  if len(stack) != 0 and flag[0] != True:
    if stack[-1] not in visited:
      visited += [stack[-1]]
    for i3 in adjL[stack[-1]]:
      if i3 not in visited:
        stack += [i3]
        cycle_checker(stack, visited, adjL, flag)
      if i3 in visited and i3 in stack:
        flag[0] = True
        break
    stack.pop()


def adjList(file, n, m):
  inC = [0] * (n + 1)
  adjL = []
  integers = ""
  a = b = 0
  for i1 in range(n + 1):
    adjL += [[]*(n + 1)]
  for i2 in range(m):
    integers = file.readline().rstrip().split(" ")
    a, b = int(integers[0]), int(integers[1])
    inC[b] += 1
    adjL[a] += [b]
  return adjL, inC


def course_order(file, output):
  integers = file.readline().rstrip().split(" ")
  n, m = int(integers[0]), int(integers[1])

  queue = []
  v = 0
  otp = []

  adjL, inC = adjList(file, n, m)

  stCyc = []
  flag = [False]
  visC = []
  while v < n and flag[0] == False:
    v += 1
    if v not in visC:
      stCyc = [v]
      visC = [v]
      cycle_checker(stCyc, visC, adjL, flag)

  if flag[0] == True:
    output.write("IMPOSSIBLE")
  else:
    for i4 in range(1, len(inC)):
      if inC[i4] == 0:
        queue += [i4]
    bfs(adjL, queue, inC, n, m, otp)
    for i6 in otp:
      output.write(str(i6) + " ")



file1 = open("input1b_1.txt", "r")
output1 = open("output1b_1", "w")
course_order(file1, output1)
file2 = open("input1b_2.txt", "r")
output2 = open("output1b_2", "w")
course_order(file2, output2)
file3 = open("input1b_3.txt", "r")
output3 = open("output1b_3", "w")
course_order(file3, output3)
file1.close()
output1.close()
file2.close()
output2.close()
file3.close()
output3.close()