# Create function-generator divisor that should return all divisors of the positive number.
# If there are no divisors left function should return None.
# three = divisor(3)
# next(three) => 1
# next(three) => 3
# next(three) => None

def divisor(number):
    yield from [x for x in range(1, 1000) if not number % x]
    while True:
        yield None





three = divisor(3)
print(next(three))
print(next(three))
print(next(three))

two = divisor(2)
print(next(two))
print(next(two))
print(next(two))
print(next(two))