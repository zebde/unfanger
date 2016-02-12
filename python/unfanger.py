import sys
import re


FANGS = [
    (r'\[\.\]', '.'),
    (r'\[at\]', '@'),
    (r'hxxp:\/\/', 'http://'),
    (r'hxxps:\/\/', 'http://'),
]


def unfang(var):
    """Removes fangs from strings bases on a list tuple key pair"""
    for pattern, value in FANGS:
        var = re.sub(pattern, value, var)
    return var


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            print(unfang(line.rstrip('\n')))
