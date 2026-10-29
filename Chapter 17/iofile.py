# read file
# open function
# read method
# seek method
# tell method 
# readline method 
# readlines method 
# close method


# print(f'cursor position - {f.tell()}')
# print(f.read())
# print(f.readline(), end='')
# print(f.readline())
# print(f.readline())
# print(f.read())
# print(f'cursor position - {f.tell()}')
# print("Before seek method")
# f.seek(0)
# print("After seek method")
# print(f'cursor position - {f.tell()}')
# lines = f.readlines()
# # print(len(lines) )
# for line in lines:
#     print(line,end='')

f = open('file1.txt', 'r')
# f = open(r"D:\Python Tutorials\Chapter 17\iofile.py")


f.close()
print(f.closed)
