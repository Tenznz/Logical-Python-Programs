def reverse(number):
    """

    :param number:
    :return:
    """
    reverse_number = 0
    while number != 0:
        reverse_number = reverse_number*10+number % 10
        number = number // 10
    return reverse_number


if __name__ == '__main__':
    inputNumber = int(input("Enter a number"))
    print(reverse(inputNumber))
