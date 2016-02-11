import sys


def doUnfang():
    with open(sys.argv[1]) as f:
        for line in f:
            print(line.replace("[.]", "."))


if __name__ == '__main__':
    doUnfang()
