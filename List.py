#Q Python program to remove duplicate element from a list

#...way 1....removing duplicate elements from a single list...
cric = [275, 49.3, "saurabh","saurabh"]
print(list(set(cric)))

'''....EXPLANATION...firstly we convert list into set, as set cannot have a duplicated item...then again convert it into list...
so we will get a list as an output without showing duplicate elements'''

#....way 2....removing duplicate elements from the two created list...
aws = [2,3,4,9,11]
swa = [3,9,15,17,19]
print(list(set(aws) ^ set(swa)))
