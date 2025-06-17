def minimum(coin, total):
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for iter1 in coin:
        for iter2 in range(iter1, total + 1):
            dp[iter2] = min(dp[iter2], dp[iter2 - iter1] + 1)

    return dp[total]


def func1(file, output):
    line = file.readline().split()
    n, x = int(line[0]), int(line[1])

    coin = [int(i) for i in file.read().split()]

    result = minimum(coin, x)

    if result == float('inf'):
        result = -1

    output.write(str(result))

file1 = open("input4_1.txt", "r")
output1 = open("output4_1.txt", "w")
func1(file1, output1)
file2 = open("input4_2.txt", "r")
output2 = open("output4_2.txt", "w")
func1(file2, output2)
file1.close()
output1.close()
file2.close()
output2.close()

    