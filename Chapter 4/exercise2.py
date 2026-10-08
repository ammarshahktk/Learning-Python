def is_pelindrom(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
       return False

print(is_pelindrom("naman"))
print(is_pelindrom("horse"))