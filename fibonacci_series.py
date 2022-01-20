def fibonacci(number):
    """

    :param number:
    :return:
    """
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


if __name__ == '__main__':
    max_input = int(input("Enter the number:"))
    for count in range(max_input-1):
        print(fibonacci(count), end=",")
    print(fibonacci(max_input-1))
