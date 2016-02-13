"""
Unfangs stuff.

The script will look at the first variable passed to it and will attempt to
open that as a file and perform various de-fanging on the file based on the
FANGS list.
"""

import sys
import re


FANGS = [
    (r'\[\.\]', '.'),
    (r'\[at\]', '@'),
    (r'hxxp:\/\/', 'http://'),
    (r'hxxps:\/\/', 'https://'),
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
