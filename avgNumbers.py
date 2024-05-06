# file reading

def main():
    infile = open("numbers.txt", "r")
    outfile = open("output.txt", "w")
    total = 0
    count = 0
    line = infile.readline()
    while line != "":
        total += float(line)
        print(line, end="")
        count += 1
        line = infile.readline()
    print(total)

    infile.close()
    outfile.close()


main()