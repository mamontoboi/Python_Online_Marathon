# Example:
#
# For expression = ["2","+","3"] the output should be ["2","3","+"].

def toPostFixExpression(e):
    symb = ["+", "-", "/", "*", ")", "(", "%", "^"]
    numbs = []
    operats = []
    for sym in e:
        if sym not in symb:
            numbs.append(sym)
        elif sym == "*" or sym == "/":
            if len(operats) > 0:
                if sym == "*" and operats[-1] == "/":
                    val = operats.pop()
                    numbs.append(val)
                elif sym == "/" and operats[-1] == "*":
                    val = operats.pop()
                    numbs.append(val)
                elif sym == "/" and operats[-1] != "*":
                    operats.append(sym)
                elif sym == "*" and operats[-1] != "/":
                    operats.append(sym)
            else:
                operats.append(sym)

        elif sym == ")":
            while operats[-1] != "(":
                val = operats.pop()
                numbs.append(val)
            operats.remove("(")

        else:
            operats.append(sym)

    for i in range(len(operats)):
        operat = operats.pop()
        numbs.append(operat)

    return numbs


expression = ["2", "+", "3"]
print(toPostFixExpression(expression))
#
print(toPostFixExpression(["20", "+", "3", "*", "(", "5", "*", "4", ")"]))
# # ['20', '3', '5', '4', '*', '*', '+']

print(toPostFixExpression(
    ["(", "(", "(", "1", "+", "2", ")", "*", "3", ")", "+", "6", ")", "/", "(", "2", "+", "3", ")"]))
# ['1', '2', '+', '3', '*', '6', '+', '2', '3', '+', '/']