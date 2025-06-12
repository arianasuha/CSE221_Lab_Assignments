
#1(2)

def check_sum(file, output):
  n, target = file.readline().rstrip().split(" ")
  list1 = file.readline().rstrip().split(" ")
  result = False
  i, j = 0, int(n)-1
  while i != j and i < j and result == False:
    if int(list1[i]) + int(list1[j]) == int(target):
      result = True
      output.write(f"{i + 1} {j + 1}")
      break
    elif int(list1[i]) + int(list1[j]) < int(target):
      i += 1
    elif int(list1[i]) + int(list1[j]) > int(target):
      j -= 1
  if result == False:
    output.write(f"IMPOSSIBLE")


file = open("input1.txt", "r")
output = open("output1b.txt", "w")
check_sum(file, output)
output.write("\n")
check_sum(file, output)
output.write("\n")
check_sum(file, output)
output.write("\n")
check_sum(file, output)
file.close()
output.close()