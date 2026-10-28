# Ex 45, Create a list of numbers from 1 to 10 and:
    #    Print the first 3 items , Print the last 3 items , Print every second item using slicing

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_three = numbers[:3]

last_three = numbers[-3:]

every_second = numbers[: :2]

print("First 3 item of list : ", first_three)

print("Last 3 item of list : ", last_three)

print("Every second item : " ,every_second)