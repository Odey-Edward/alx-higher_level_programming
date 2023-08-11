#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("{:d} arguments.".format(0))
    else:
        if len(argv) - 1 == 1:
            args = "argument"
        else:
            args = "arguments"
        print("{:d} {}:".format(len(argv) - 1, args))
        for i in range(1, len(argv)):
            print("{:d}: {}".format(i, argv[i]))
