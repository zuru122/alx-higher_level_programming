#!/usr/bin/python3
# Author: Sunday, Justice Gabriel

def cal_sum_of_arg(arguments):
    n = len(arguments) - 1

    if n == 0:
        return (n)
    else:
        sum_of_arg = 0
        for x in range(1, n + 1):
            sum_of_arg += int(arguments[x])
        return (sum_of_arg)


if __name__ == "__main__":
    import sys

    cal_sum = cal_sum_of_arg(sys.argv)
    print(cal_sum)
