import sys
import re


fangs = [
    ('\[\.\]', '.'),
    ('\[at\]', '@'),
    ('hxxp:\/\/', 'http://'),
    ('hxxps:\/\/', 'http://'),
]


def doUnfang(var):
    for pattern, value in fangs:
        var = re.sub(pattern, value, var)
    return var


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            print(doUnfang(line.rstrip('\n')))
