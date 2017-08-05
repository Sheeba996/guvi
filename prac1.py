#def main():
 #   x = String(input("Please enter a string: "))






def reverse_a_string_slowly(a_string):
    new_string = ''
    index = len(a_string)
    while index:
        index -= 1                    # index = index - 1
        new_string += a_string[index] # new_string = new_string + character
    return new_string


rrr= reverse_a_string_slowly("i love this")
print(rrr)
