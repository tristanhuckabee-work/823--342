# Given a string, write a function that returns the character that is the
# majority of the string. If there is no majority character, return None. A
# majority is considered as having more than `n / 2` instances where `n` is the
# length of the string.

# Write your code here.
def majority_char(string):
    ## O(n^2) time
    for char in string:
        if string.count(char) > len(string) / 2:
            return char

    return None

    ## O(n) time
    # chars = {}
    # for char in string:
    #     if char in chars:
    #         chars[char] += 1
    #     else:
    #         chars[char] = 1
    
    # for char, cnt in chars.items():
    #     if cnt > len(string) / 2:
    #         return char
    
    # return None


str = 'all'
str2 = 'welcome to the jungle'

print(majority_char(str))           # 'l'
print(majority_char(str2))          # None