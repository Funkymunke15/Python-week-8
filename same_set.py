# Davis Arita
# 10/24/22
# CS 131 Exercise 8 Part C
# checks whether two lists have the same elements in some order, ignoring duplicates

def main():
    list1 = [1, 4, 9, 16, 9, 7, 4, 9, 11]
    list2 = [11, 11, 7, 9, 16, 4, 1]

    print("The lists contain the same elements:", same_set(list1, list2))


def same_set(listA, listB):
    for i in listA:
        if i not in listB:
            return False
    return True


main()
