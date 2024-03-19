num_list = [[11,12,13], [45,55,56], [10,11,12], [71,28,94]]

output1 = num_list[0] + num_list[3]

output2 = num_list[3] + num_list[1]

output3 = list(set(num_list[0]) - set(num_list[2]))

output4 = list(set(num_list[2]) - set(num_list[0]))

output5 = num_list[0:3] + num_list[1:3]

print('Output 1:', output1)

print('Output 2:', output2)

print('Output 3:', output3)

print('Output 4:', output4)

print('Output 5:', output5)