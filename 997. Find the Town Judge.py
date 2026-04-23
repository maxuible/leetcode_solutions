# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

# Example 1:

# Input: n = 2, trust = [[1,2]]
# Output: 2
# Example 2:

# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:

# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1


from typing import List

def findJudge(n: int, trust: List[List[int]]) -> int:

    trusted = {}

    trusts_someone = []

    if n == 1 and len(trust) == 0:
        return 1

    for trusts in trust:
        if trusts[1] not in trusted:
            trusted[trusts[1]] = 1
        else:
            trusted[trusts[1]] = trusted[trusts[1]] + 1

        trusts_someone.append(trusts[0])

    for key, value in trusted.items():
        if value >= n -1 and key not in trusts_someone:
            return key

    return -1


print(findJudge(2, [[1,2]]))
print(findJudge(3, [[1,3],[2,3]]))
print(findJudge(3, [[1,3],[2,3],[3,1]]))