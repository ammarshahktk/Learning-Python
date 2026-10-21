#define a function that take list of strings
# list containing reverse of every string 
# NOTE - USE LIST COMPREHENSION because we already did this exercise using normal method
# example
# l = ['abc', 'tuv', 'xyz']
# revere_string(1) ----> ['bac', 'vut', 'zyx']

def reverse_strings(l):
    return[name[::-1] for name in l]

print(reverse_strings(['abc', 'tuv', 'xyz']))