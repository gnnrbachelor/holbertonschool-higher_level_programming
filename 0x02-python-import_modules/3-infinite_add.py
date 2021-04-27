#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    sum = 0
    num_arg = len(argv) - 1
    for i in range(num_arg):
       sum += int(argv[i + 1])
    print("{}".format(sum))
