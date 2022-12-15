# For a = [2,2,1,3,4,1] the answer is 3.

def studying_hours(a):
    global_count = 0
    count = 1
    for i in range(1, len(a)):
        if a[i - 1] <= a[i]:
            count += 1
            if global_count < count:
                global_count = count
        elif a[i - 1] > a[i]:
            if global_count < count:
                global_count = count
            count = 1

    return global_count


print(studying_hours([2, 2, 1, 3, 4, 1]))
print(studying_hours([2, 2, 9]))  # 3
print(studying_hours([10, 100, 111, 1, 2]))  # 3
print(studying_hours([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))  # 50