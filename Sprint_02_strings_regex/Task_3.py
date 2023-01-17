# The string defining the points of the quadrilateral has the next form: "#LB1:1#RB4:1#LT1:3#RT4:3"
#
#  LB - Left Bottom point
#  LT - Left Top point
#  RT - Right Top point
#  RB - Right Bottom point
# numbers after letters are the coordinates of a point.
# Write a function figure_perimetr() that calculates the perimeter of a quadrilateral
#
# The formula for calculating the distance between points:
# test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
# print(figure_perimetr(test1))  # 10


def figure_perimetr(test: str):
    numbs = test.lstrip('#').split('#')
    seq = ((numbs[1], numbs[0]), (numbs[3], numbs[1]), (numbs[3], numbs[2]), (numbs[2], numbs[0]))

    def inner_func(a, b):
        return ((int(a[2]) - int(b[2])) ** 2 + ((int(a[4])) - (int(b[4]))) ** 2) ** 0.5

    length = 0
    for element in seq:
        length += inner_func(*element)

    return length


test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
print(figure_perimetr(test1))
