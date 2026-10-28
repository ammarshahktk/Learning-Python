# Ex 61, Given two lists, find all elements that exist in both using loops and conditions.

list_a = [1, 3, 5, 7, 9, 12, 15]
list_b = [2, 3, 6, 9, 12, 18, 20]

common_items = []

for item in list_a:
    if item in list_b and item not in common_items:
        common_items.append(item)

print("List A:", list_a)
print("List B:", list_b)
print("Common Items:", common_items)