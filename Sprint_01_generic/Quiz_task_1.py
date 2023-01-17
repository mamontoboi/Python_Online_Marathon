# For the given integer n, consider an increasing sequence consisting of all positive integers that are
# either powers of n, or sums of distinct powers of n.
#
# Your task is to find the kth (1-based) number in this sequence.
#
# Example
#
# For n = 3 and k = 4, the output should be
# kthTerm(n, k) = 9.
#
# For n = 3, the sequence described above begins as follows: 1, 3, 4, 9, 10, 12, 13...
# [3**0] => [1]
# [1, 3**1, 3**1 +1] => [1, 3, 4]
# [1, 3, 4, 3**2, 3**2 +1, 3**2 +3, 3**2 +4] => [1, 3, 4, 9, 10, 12, 13]
# ...
#
# The 4th number in this sequence is 9, which is the answer.
#
# Input/Output
#
# [input] integer n
#
# The number to build the sequence by.
#
# Constraints:
# 2 ≤ n ≤ 30.
#
# [input] integer k
#
# The 1-based index of the number in the sequence.
#
# Constraints:
# 1 ≤ k ≤ 100.
#
# [output] integer
#
# The kth element of the sequence.
import itertools

# Step 1: Converting the binary number (10110110)2 to decimal
#
# (1 × 27) + (0 × 26) + (1 × 25) + (1 × 24) + (0 × 23) + (1 × 22) + (1 × 21) + (0 × 20)
#
# = 128 + 0 + 32 + 16 + 0 + 4 + 2 + 0 = (182)10


def kthTerm(n, k):
    bin_val = bin(k)[2:]

    bin_code = [x for x in bin_val]

    result = 0
    for i in range(len(bin_code)):
        num = bin_code.pop(-1)
        if int(num):
            fig = n ** i
            result += fig

    return result


print(kthTerm(3, 4))  # 4
print(kthTerm(3, 7))  # 13

print(kthTerm(3, 3))  # 4
print(kthTerm(2, 7))  # 7
print(kthTerm(30, 100))  # 753300900
print(kthTerm(21, 63))  # 4288306
print(kthTerm(10, 99))  # 1100011