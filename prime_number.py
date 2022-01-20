def is_prime(number):
    """
    :param number:
    :return:
    """
    if number > 1:
        for a in range(2, number):
            if (number % a) == 0:
                print(number, "is not a prime number")
                break
        else:
            print(number, "is a prime number")


if __name__ == '__main__':
    input_number = int(input("Enter a number"))
    is_prime(input_number)
