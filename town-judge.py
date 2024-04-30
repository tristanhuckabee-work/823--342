"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
"""
def findJudge(n, trust):
    trusts = {}

    for a, b in trust:
        if a in trusts:
            trusts[a]['trustees'].append(b)
        else:
            trusts[a] = {
                'trustees': [b],
                'trusters': []
            }
        if b in trusts:
            trusts[b]['trusters'].append(a)
        else:
            trusts[b] = {
                'trustees': [],
                'trusters': [a]
            }

    for el, trust_table in trusts.items():
        cnt = n - 1
        if not len(trust_table['trustees']) and len(trust_table['trusters']) == cnt:
            return el
    return -1


test_a = [2, [[1,2]]]
test_b = [3, [[1,3], [2,3]]]
test_c = [3, [[1,3],[2,3],[3,1]]]

print(findJudge(*test_a)) # 2
print(findJudge(*test_b)) # 3
print(findJudge(*test_c)) # -1