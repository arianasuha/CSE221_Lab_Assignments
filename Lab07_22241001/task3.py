def climb_ways(steps, stairs):
    mat = [[0 for i in range(stairs + 1)] for i in range(len(steps) + 1)]
    
    for iter in range(len(steps) + 1):
        mat[iter][0] = 1
        
    for iter1 in range(len(mat)):
        if iter1 == 0:
            continue
        for iter2 in range(stairs + 1):
            if iter2 - steps[iter1 - 1] < 0:
                mat[iter1][iter2] = mat[iter1 - 1][iter2]
            else:
                for iter3 in range(1, steps[iter1 - 1] + 1):
                    mat[iter1][iter2] += mat[iter1][iter2 - iter3]

    return mat[len(steps)][stairs]


def func1(file, output):
    stairs = file.readline().strip()
    way_climb = climb_ways([1, 2], int(stairs))
    output.write(f"{str(way_climb)}")
            
            
file1 = open("input3_1.txt", "r")
output1 = open("output3_1.txt", "w")
func1(file1, output1)
file2 = open("input3_2.txt", "r")
output2 = open("output3_2.txt", "w")
func1(file2, output2)
file3 = open("input3_3.txt", "r")
output3 = open("output3_3.txt", "w")
func1(file3, output3)
file4 = open("input3_4.txt", "r")
output4 = open("output3_4.txt", "w")
func1(file4, output4)

file1.close()
output1.close()
file2.close()
output2.close()
file3.close()
output3.close()
file4.close()
output4.close()
