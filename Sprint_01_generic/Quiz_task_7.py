def Cipher_Zeroes(N):
    dict_of_zeroes = {"0": 1, "6": 1, "9": 1, "8": 2}
    count = 0
    lst = [letter for letter in N]

    for element in lst:
        if element in dict_of_zeroes.keys():
            count += dict_of_zeroes[element]

    if count > 0 and count % 2 == 0:
        count -= 1
    elif count % 2:
        count += 1

    return str(bin(count))[2:]


print(Cipher_Zeroes("565"))
print(Cipher_Zeroes("8200"))