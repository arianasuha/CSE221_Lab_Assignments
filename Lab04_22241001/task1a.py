def adj_matrix(file, output):
        nums = file.readline().strip().split()
        n, e = int(nums[0]), int(nums[1])
        matrix = [[0 for i in range(n+1)] for j in range(n+1)]
        for lines in file:
            num_list = lines.strip().split()
            u, v, w = int(num_list[0]), int(num_list[1]), int(num_list[2])
            matrix[u][v] = w
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                output.write(str(matrix[i][j]) + " ")
            output.write("\n")

file1 = open("input1a_1.txt", "r")
output1 = open("output1a_1.txt", "w")
adj_matrix(file1, output1)
file2 = open("input1a_2.txt", "r")
output2 = open("output1a_2.txt", "w")
adj_matrix(file2, output2)
file1.close()
output1.close()
file2.close()
output2.close()




