#1(1)

def check_sum(file, output):
  n, target = file.readline().rstrip().split(" ")
  list1 = file.readline().rstrip().split(" ")
  result = False
  for i in range(int(n)-1):
    for j in range(i + 1, int(n)):
      if int(list1[i]) + int(list1[j]) == int(target):
        result = True
        output.write(f"{i + 1} {j + 1}")
        break
    if result == True:
      break
  if result == False:
    output.write(f"IMPOSSIBLE")


file = open("input1.txt", "r")
output = open("output1a.txt", "w")
check_sum(file, output)
output.write("\n")
check_sum(file, output)
output.write("\n")
check_sum(file, output)
output.write("\n")
check_sum(file, output)
file.close()
output.close()

