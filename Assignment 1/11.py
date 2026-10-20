# Ex 11, Write a string "hello world hello" and Count how many times "hello" appears also check the length of the string

line = "hello world hello"
count_hello = line.count("hello") 
line_length = len(line)

print(f"The word hello appears {count_hello} times.")
print(f"The length of the string is {line_length} characters.")