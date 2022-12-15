# Example
#
# For a = [10, 5, 4], the output should be
# order(a) = "descending";
# For a = [6, 20, 160, 420], the output should be
# order(a) = "ascending";
# For a = [1, 7, 0, 4, 8, 1], the output should be
# order(a) = "not sorted".

def order(a):
    count = 0
    for i in range(1, len(a)):
        if a[i - 1] > a[i]:
            count -= 1
        elif a[i - 1] < a[i]:
            count += 1

    if count == len(a) - 1:
        return "ascending"
    elif count == - len(a) + 1:
        return "descending"
    else:
        return "not sorted"

print(order([10, 5, 4]))
print(order([6, 20, 160, 420]))
print(order([1, 7, 0, 4, 8, 1]))
