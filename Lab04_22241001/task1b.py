def adj_list(file, output):
        nums = file.readline().strip().split()
        n, e = int(nums[0]), int(nums[1])
        new_dict = {}
        for i in range(n+1):
             new_dict[i] = []
        for lines in file:
            numbers = lines.strip().split()
            u, v, w = int(numbers[0]), int(numbers[1]), int(numbers[2])
            num_list = (v,w)
            if new_dict[u] == []:
               new_dict[u] = [num_list] 
            else:
               new_dict[u].append(num_list)
        for key,val in new_dict.items():
            if new_dict[key] == []:
               output.write(f"{key} : ")
            else:
               output.write(f"{str(key)} : ")
               for items in val:
                   output.write(f"{str(items)} ")
            output.write("\n")

file1 = open("input1b_1.txt", "r")
output1 = open("output1b_1.txt", "w")
adj_list(file1, output1)
file2 = open("input1b_2.txt", "r")
output2 = open("output1b_2.txt", "w")
adj_list(file2, output2)
file3 = open("input1b_3.txt", "r")
output3 = open("output1b_3.txt", "w")
adj_list(file3, output3)
file1.close()
output1.close()
file2.close()
output2.close()
file3.close()
output3.close()