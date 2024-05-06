# Davis Arita
# 10/17/22
# Exercise 8 part A
# removes non-prime numbers and prints remaining values

def main():
    prime_list = []
    for index in range(1, 101):
        prime_list.append(index)

    del prime_list[0]
    for num in range(2, 101):
        for i in range(2, num):
            if num % i == 0:
                if num in prime_list:
                    prime_list.remove(num)

    print(prime_list)

main()