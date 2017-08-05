ex_string = "I live in New York"
x = input("Please enter a string: ")
reversed_string = " ".join(ex_string.split(" ")[::-1])
reversed_string1 = " ".join(x.split(" ")[::-1])
print(reversed_string)
print(reversed_string1)
