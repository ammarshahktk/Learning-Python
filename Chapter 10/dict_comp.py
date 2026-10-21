# dictionary Comprehension
# square = {1:1, 2:4, 3:9} like key is 1 so value will be its square
# 1 : 1
# 2 : 4
# square of 1 is 1
# square of 2 is 2
square = {f"Square of {num} is " : num**2 for num in range(1,11) }
# print(square)

for k, v in square.items():
    print(f"{k} : {v} ")


# "Ammar" to count one char in string
 
string = "ammar"
word_count = {char:string.count(char) for char in string}
print(word_count)