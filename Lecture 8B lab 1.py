# Davis Arita
# 10/19/2022
# CS 131 Lecture 8B lab 1
# checks whether two lists have the same elements in some order, with the same
# multiplicities

def sameElements(listA, listB):
    listA.sort()
    listB.sort()
    return listA == listB


def main():
    listA = [1, 4, 9, 16, 9, 7, 4, 9, 11]
    listB = [11, 1, 4, 9, 16, 9, 7, 4, 9]

    print("The lists contain the same elements: ", end="")
    print(sameElements(listA, listB))


main()