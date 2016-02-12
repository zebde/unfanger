import sys
import re


FANGS = [
    (r'\[\.\]', '.'),
    (r'\[at\]', '@'),
    (r'hxxp:\/\/', 'http://'),
    (r'hxxps:\/\/', 'http://'),
]


def unfang(var):
    """Return an unfanged string based on regexes defined in FANGS."""
    for pattern, value in FANGS:
        var = re.sub(pattern, value, var)
    return var


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            print(unfang(line.rstrip('\n')))
