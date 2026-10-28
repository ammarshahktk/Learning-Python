# Ex 57, Create a list of words.
    #    Use a loop to count how many words contain at least one vowel (a, e, i, o, u).

words = ["python", "sky", "rhythm", "apple", "fly", "code", "dry"]

vowels = "aeiouAEIOU"

vowel_word_count = 0

for word in words:
    for char in word:
        if char in vowels:
            vowel_word_count += 1
            break  


print("Original list:", words)
print("Number of words with at least one vowel:", vowel_word_count)