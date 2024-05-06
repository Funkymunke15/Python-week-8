# Davis Arita
# 10/17/2022
# Lecture 8A lab 1
# Manipulate lists

def main():
    intList = [1, 2, 3, 4, 5, 6]
    remove6List = [4, 6, 8, 6, 12]
    remove20List = [5, 10, 15, 200, 25, 50, 20]
    list1 = ["M", "na", "i", "Ke"]
    list2 = ["y", "me", "s", "lly"]
    print(reverseList(intList))
    print(remove_from_list(6, remove6List))
    print(replace_in_list(20, 200, remove20List))
    print(zip_list(list1, list2))


def reverseList(param_list):
    return param_list[::-1]


def remove_from_list(to_remove, param_list):
    for index in param_list:
        if index == to_remove:
            param_list.remove(index)
    return param_list


def replace_in_list(value_to_replace, replace_value, param_list):
    for index in range(len(param_list)):
        if param_list[index] == value_to_replace:
            param_list[index] = replace_value
    return param_list


def zip_list(list1, list2):
    return [v1 + v2 for v1, v2 in zip(list1, list2)]



main()
