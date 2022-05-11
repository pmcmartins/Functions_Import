list1 = [1,2,3,5,7,8]
list2 = [2,3,5,6,7,8]

result = list(map(lambda x: x == x in list1,list2))
print(result)

help(map)