def sub_list_counter(l):
    count = 0
    for i in l:
        if type(i)== list:
            count += 1
    return count

num = [1, 2, 3, [1, 2], [3, 4], [6, 7], [8, 9]]
print(sub_list_counter(num))