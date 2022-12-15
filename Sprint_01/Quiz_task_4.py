# Example
#  q[i] = p[r[i]].
# Input:
# p = [5, 1, 3],  q = [3, 1, 5]
#
# Output:
# r = [3, 2, 1]

def findPermutation(p, q):
    r = []
    for i in q:
        if i in p:
            val = p.index(i)
            r.append(val + 1)

    return r

p = [5, 1, 3]
q = [3, 1, 5]
print(findPermutation(p, q))