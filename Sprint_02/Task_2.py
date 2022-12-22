# Numbers in the Morse code have the following pattern:
#
# all digits consist of 5 characters;
# the number of dots at the beginning indicates the numbers from 1 to 5, the remaining characters are dashes;
# starting with the number 6, each dot is replaced by a dash and vise versa.
# Write the function morse_number() for encryption of a number in a three-digit format in Morse code.
#
#
#
# Attention!
# Do not use any collection data like lists, tuples, dictionaries for holding Morse codes

def morse_number(number: str):
    string = ''
    for letter in list(number):
        if int(letter) in range(1, 6):
            string += int(letter) * '.' + (5 - int(letter)) * '-' + ' '
        elif int(letter) in range(6, 10):
            string += (int(letter) - 5) * '-' + (10 - int(letter)) * '.' + ' '
        elif letter == '0':
            string += '----- '

    return string

# def morse_number(number: str):
    # string = ''
    # for letter in list(number):
    #     match letter:
    #         case '1':
    #             string += '.---- '
    #         case '2':
    #             string += '..--- '
    #         case '3':
    #             string += '...-- '
    #         case '4':
    #             string += '....- '
    #         case '5':
    #             string += '..... '
    #         case '6':
    #             string += '-.... '
    #         case '7':
    #             string += '--... '
    #         case '8':
    #             string += '---.. '
    #         case '9':
    #             string += '----. '
    #         case '0':
    #             string += '----- '
    #
    # return string

print(morse_number("295"))
print(morse_number("005"))