# Ex 56, Create a list of 7 random items. Reverse the list using both:
    #    list.reverse() method , Slicing ([::-1]). Print both results.

random_list = ["Chair", "Class", "Table", "Dress", "Shop", "Bikes", "Cars"]

sliced_method = random_list[::-1]
print(sliced_method)

random_list.reverse()
print(random_list)
