# Davis Arita
# 10/17/2022
# Lecture 8A lab 2
# compute the alternating sum and difference of all elements in a list

def main():
    flag = True
    my_list = []
    while flag:
        userInput = input("Enter value (blank line to quit): ")
        if userInput == "":
            flag = False
            continue
        my_list.append(userInput)

    print(my_list)
    print(compute(my_list))


def compute(param_list):
    total = 0

    i = 0

    while i <= len(param_list):
        if i % 2:
            total -= i
        else:
            total += i
        i += 1

    return total


main()