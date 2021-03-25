#to print the positive numbers

list1 = [12, -7, 5, 64, -14]

A = list(filter(lambda x: (x >= 0), list1))
print(A)

list2 = [12, 14, -95, 3]

B = [val for val in list2 if val >0]
print(B)







