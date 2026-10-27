# Ex 43, Make two lists:  list1 = [1, 2, 3] , list2 = [4, 5, 6]
    #    Combine them into a new list using + and print the result.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
 # 1st way

combined = list1 + list2
print(combined)

# 2nd way
list1.extend(list2)
print(list1)