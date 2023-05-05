# Creates the best code ever

SUPPORTED_LENGTH = 50
TAB_SIZE = 4
TAB_CHARACTER = ' '

output_list = []


def put(string_in, indent_level=0):
    global output_list
    prefix = TAB_SIZE * TAB_CHARACTER * indent_level
    output_list.append(prefix + string_in)


# Add the comment

put('#thank you to the amazing CS faculty for giving us the skills to write code like this')
put('def checkWhetherANumberIsEvenOrOddAndReturnOddOrEven(number: int):')

for i in range(1, SUPPORTED_LENGTH + 2):

    # Check for length == 1 edge case
    if SUPPORTED_LENGTH == 1:
        put("answer = ' '.join(('too','big','could','not','compute'))", 1)
        put("return answer", 2)
        break

    # Check for end or starting cases
    if i == SUPPORTED_LENGTH + 1:
        put('else:', 1)
        put("answer = ' '.join(('too','big','could','not','compute'))", 2)
        put("return answer", 2)
        continue
    elif i == 1:
        put(f'if number == {i}:', 1)
        put("answer = ''.join(('o','d','d'))", 2)
        put("return answer", 2)
        continue

    # Check for even or odd cases
    put(f'elif number == {i}:', 1)
    if i % 2 == 0:
        put("answer = ''.join(('e','v','e','n'))", 2)
    else:
        put("answer = ''.join(('o','d','d'))", 2)
    put("return answer", 2)

put('print(checkWhetherANumberIsEvenOrOddAndReturnOddOrEven(int(input("Type a number to check: "))))')
put('')

# Print list to the file

with open("bestcodeever.py", "w+") as file_out:
    file_out.writelines('\n'.join(output_list))
    print(file_out.read())

# Debug print

# print('\n'.join(output_list))
