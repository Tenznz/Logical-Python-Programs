from array import array
from random import randint


def get_coupon(num_of_coupon):
    """

    :param num_of_coupon:
    :return:
    """
    num_arr = []
    while num_of_coupon != 0:
        num_arr.append(randint(1, 100))
        num_of_coupon = num_of_coupon - 1
    return num_arr


if __name__ == '__main__':
    input_number = int(input("Enter a coupon number"))
    print(get_coupon(input_number))
