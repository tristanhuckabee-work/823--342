"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.
Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

def numJewelsInStones(jewels, stones):
    cnt = 0
    for stone in stones:
        if stone in jewels:
            cnt += 1
    return cnt


test_a = ["aA", "aAAbbbb"]
test_b = ["z", "ZZ"]
print(numJewelsInStones(*test_a)) # 3
print(numJewelsInStones(*test_b)) # 0
