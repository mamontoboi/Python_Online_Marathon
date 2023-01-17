# Create function create with one string argument. This function should return anonymous function that checks
# if the argument of function is equals to the argument of outer function.
#
# For example:


# def create(text: str):
#     def inner(text2: str):
#         if text2 == text:
#             print(True)
#         else:
#             print(False)
#
#     return inner

def create(text):
    return lambda text2: text == text2


tom = create("pass_for_Tom")

print(tom("pass_for_Tom"))  # returns true

print(tom("pass_for_tom"))  # returns false