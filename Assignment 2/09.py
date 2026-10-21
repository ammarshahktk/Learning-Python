# Ex 20, FizzBuzz with For Loop. Print numbers from 1 to 50
    #    if divisible by 3 → print “Fizz” , If divisible by 5 → print “Buzz”, If both → print “FizzBuzz”

for num in range(1,51):
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} FizzBuzz")
    elif num % 3 == 0:
        print(f"{num} Fizz")
    elif num % 5 == 0:
        print(f"{num} Buzz")
    else:
        print(num)
