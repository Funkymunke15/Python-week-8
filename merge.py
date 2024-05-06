# Davis Arita
# 10/24/22
# CS 131 Exercise 8 part D
# merges two lists, alternating elements from both lists


def main():
    list1 = [1, 4, 9, 16]
    list2 = [9, 7, 4, 9, 11]

    print("List a is", list1)
    print("List b is", list2)
    result = merge(list1, list2)
    print("The merged list is", result)


def merge(listA, listB):
    mergedList = []
    lenA = len(listA)
    lenB = len(listB)

    for i in range(max(lenA, lenB)):
        if i < lenA:
            mergedList.append(listA[i])
        if i < lenB:
            mergedList.append(listB[i])

    return mergedList


main()