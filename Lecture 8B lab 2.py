# Davis Arita
# 10/19/2022
# CS 131 Lecture 8B lab 2
# creates a 4 x 4 table with int values and tests whether
# the numbers create a magic square

def createTable():

    ROWS = 4
    COLUMNS = 4

    table = [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]
    return table


def printSquare(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


def magicTest(matrix):
    magic_constant = 0
    n = len(matrix)
    for i in matrix[0]:  # get sum of first row to act as key to check against
        magic_constant += i

    for i in range(n):  # iterates over each row
        sum_row = 0
        for j in range(n):
            sum_row += matrix[i][j]  # sums the row
        if sum_row != magic_constant:  # checks against constant
            return False

    for i in range(n):  # iterates over each column
        sum_col = 0
        for j in range(n):
            sum_col += matrix[j][i]  # sums the column
        if sum_col != magic_constant:  # checks against the constant
            return False

    sum_diag = 0
    for i in range(n):
        sum_diag += matrix[i][i]  # sums the left to right diagonal
    if sum_diag != magic_constant:  # checks against the constant
        return False
    sum_diag = 0
    for i in range(n):
        sum_diag += matrix[i][-(i+1)]  # sums the right to left diagonal
    if sum_diag != magic_constant:  # checks against the constant
        return False

    return True


def main():
    square = createTable()
    printSquare(square)
    if magicTest(square):
        print("It is a magic square.")
    else:
        print("It is not a magic square")


main()
