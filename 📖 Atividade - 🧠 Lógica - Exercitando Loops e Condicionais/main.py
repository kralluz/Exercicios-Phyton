def corresponding_parenthesis(text: str):
    open: int = text.count("(")
    close: int = text.count(")")
    difference: int = open - close

    if difference > 0:
        return "(" * difference
    elif difference < 0:
        return ")" * (difference * -1)

    return ""


# Exemplo 1
result = corresponding_parenthesis("()()")
# print("ex 1: " + result)

# Exemplo 2
result = corresponding_parenthesis("()))")
# print("ex 2: " + result)

# Exemplo 3
result = corresponding_parenthesis(")))(((((")
# print("ex 3: " + result)


def remove_more_than_two_repetitions(str: str):
    new_char = ""
    for char in range(len(str)):
        if char < 2:
            new_char += str[char]
        elif not (str[char] == str[char - 1] == str[char - 2]):
            new_char += str[char]
    return new_char


text = "Ollloco meuuuu, taaa peegaando fogoo biiiiichooo"
text = remove_more_than_two_repetitions(text)
print(text)
