# Given two strings, write a function, `remove_repeats` that returns a set of
# the uncommon characters from both strings. Do NOT use the `^` operator.

# Write your code here.
def remove_repeats(str1, str2):
    xor = set()

    for char in str1:
        if str2.find(char) == -1:
            xor.add(char)
    for char in str2:
        if str1.find(char) == -1:
            xor.add(char)

    return xor




str1 = 'aloha'
str2 = 'bonjour'

print(remove_repeats(str1, str2))    # {'r', 'a', 'l', 'h', 'n', 'b', 'j', 'u'}