def divisors(number):
    divisors_list = []  # empty list to append divisors numbers
    I = 1
    while I <= number:  # number should be greater than 1
        if number % I == 0:  # rule of divisor
            divisors_list.append(I)     # .append to add numbers in the list
            divisors_list.sort()    # .sort to order value of list from smallest to largest
        I += 1  # increase I by one to avoid infinity loop

    print("the divisors of ", number, " is a reverse order are ", divisors_list[1:-1])


# test your solution here:
if __name__ == "_main_":
    usr_warnings = 0
    n = -1
    x = False
    while n <= 0 and usr_warnings < 100:  # to rerun program if user input a negative num
        n = int(input(f"Enter a positive integer:"))
        usr_warnings += 1
    if usr_warnings <= 100 and n > 0:
        for i in range(2, n):
            if n % i == 0:  # rule of divisor
                x = True  # if factor is found, set x to True
                break  # break out of loop
        if x:  # check if x is True
            divisors(n)
        else:  # x is False
            print(n, " has no divisors ", n, " is prime. ")

# now, complete everything!