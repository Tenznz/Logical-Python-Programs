def find_factor(num):
    """

    :param num:
    :return:
    """
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    print("Factors of {} = {}".format(num, factors))
    return factors


def perfect_number(num):
    factors = find_factor(num)
    add_factor = 0
    for index in range(len(factors)-1):
        add_factor = add_factor+factors[index]
    if num == add_factor:
        print("perfect number")
    else:
        print("not perfect number")


if __name__ == '__main__':
    input_num = int(input("enter a number"))
    perfect_number(input_num)
