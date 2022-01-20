import time


def time_convert(sec):
    """

    :param sec:
    :return:
    """
    minutes = sec // 60
    sec = sec % 60
    hours = minutes // 60
    minutes = minutes % 60
    print("Time Lapsed = {0}h:{1}m:{2}s".format(int(hours), int(minutes), int(sec)))


if __name__ == '__main__':
    input("Press Enter to start")
    start_time = time.time()
    input("Press Enter to stop")
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
