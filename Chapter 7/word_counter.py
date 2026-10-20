# WORD COUNTER  
#ammar
# d = {'a' : 2, 'm' : 2, 'r' : 1}
def word_counter(s):
    count = {}
    for char in s:
        count[char] = s.count(char)
    return count

print(word_counter('ammar')) 