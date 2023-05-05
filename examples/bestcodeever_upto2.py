#thank you to the amazing CS faculty for giving us the skills to write code like this
def checkWhetherANumberIsEvenOrOddAndReturnOddOrEven(number: int):
    if number == 1:
        answer = ''.join(('o','d','d'))
        return answer
    elif number == 2:
        answer = ''.join(('e','v','e','n'))
        return answer
    else:
        answer = ' '.join(('too','big','could','not','compute'))
        return answer
print(checkWhetherANumberIsEvenOrOddAndReturnOddOrEven(int(input("Type a number to check: "))))
