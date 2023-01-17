# Generator function randomWord has as an argument list of words. It should return any random word from this list.
# Each time words are different until the end of the list is reached. Then words are taken from the initial list again.
#
# For example if
#
# list = ['book', 'apple', 'word']
#
# books = randomWord(list)
#
# then possible output example
#
# first call of next(books) returns apple
#
# second call of next(books) returns book
#
# third call of next(books) returns word
#
# fourth call of next(books) returns book
import random


def randomWord(lst: list):
    if len(lst) > 0:
        while True:
            lst_new = lst.copy()
            for i in range(len(lst_new)):
                x = random.choice(lst_new)
                lst_new.remove(x)
                yield x
            continue
    else:
        yield None


words = [3, 4, 7]
rand = randomWord([3,2,90])
list1 = []
list2 = []
for i in range(len(words)):
    list1.append(next(rand))
print(list1)
for i in range(len(words)):
    list2.append(next(rand))
print(list2)
print(list1 != list2)
