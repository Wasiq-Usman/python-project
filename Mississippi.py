def count_s(word):
    count = 0
    for char in word:
        if char == 's' or char == 'S':
            count += 1
    return count
word = "mississippi"
result = count_s(word)
print(f"The number of 's' or 'S' in the word '{word}' is: {result}")



