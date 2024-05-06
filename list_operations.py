##
#  Implement and demonstrate a collection of list functions below.
#

# Define constant variables.
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def swap_first_last(data):
    data[0], data[-1] = data[-1], data[0]
    return data


def shift_right(data):
    data.insert(0, data.pop())
    return data


def replace_even(data):
    for index in range(len(data)):
        if index % 2 == 1:
            data[index] = 0
    return data


def replace_neighbors(data):
    for index in range(1, len(data) - 1):
        data[index] = max(data[index - 1], data[index + 1])
    return data


def remove_middle(data):
    size = len(data)
    index = size // 2
    if size % 2 == 0:
        data.pop(index)
        data.pop(index - 1)
    else:
        data.pop(index)

    return data


def even_to_front(data):
    index = 0
    for i in data:
        if i % 2 == 0:
            data.remove(i)
            data.insert(index, i)

            index += 1


def second_largest(data):
    data.sort()
    return data[-2]


def is_increasing(data):
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True


def has_adjacent_duplicate(data):
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            return True
    return False


def has_duplicate(data):
    data.sort()
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            return True
    return False


def main():
    print("The original data for all functions is: ", ONE_TEN)

    # Demonstrate swapping the first and last element.
    data = list(ONE_TEN)
    swap_first_last(data)
    print("After swapping first and last: ", data)

    # Demonstrate shifting to the right.
    data = list(ONE_TEN)
    shift_right(data)
    print("After shifting right: ", data)

    # Demonstrate replacing even elements with zero.
    data = list(ONE_TEN)
    replace_even(data)
    print("After replacing even elements: ", data)

    # Demonstrate replacing values with the larger of their neighbors.
    data = list(ONE_TEN)
    replace_neighbors(data)
    print("After replacing with neighbors: ", data)

    # Demonstrate removing the middle element.
    data = list(ONE_TEN)
    remove_middle(data)
    print("After removing the middle element(s): ", data)

    # Demonstrate moving even elements to the front of the list.
    data = list(ONE_TEN)
    even_to_front(data)
    print("After moving even elements: ", data)

    # Demonstrate finding the second largest value.
    print("The second largest value is: ", second_largest(ONE_TEN))

    # Demonstrate testing if the list is in increasing order.
    print("The list is in increasing order: ", is_increasing(ONE_TEN))

    # Demonstrate testing if the list contains adjacent duplicates.
    print("The list has adjacent duplicates: ", has_adjacent_duplicate(ONE_TEN))

    # Demonstrate testing if the list contains duplicates.
    print("The list has duplicates: ", has_duplicate(ONE_TEN))


main()
