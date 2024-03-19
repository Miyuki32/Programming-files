list1 = [12,8,9,2.5,3.6,7,4.4,14.5]

list2 = [2.5,3,14.5,12,9]

print("Output1: ",list(set(list1)-set(list2)))

print("Output2: ",list(set(list2)-set(list1)))