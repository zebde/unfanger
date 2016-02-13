#!/bin/bash
# ------------------------------------------------------------------
# [cwtaylor] Unfanger
#          Description
#
#          This script unfangs text in a file.
#
# ------------------------------------------------------------------
VERSION=0.1.0
USAGE="Usage: unfanger.sh file.txt"

sed -e 's/\[\.\]/./g' -e 's/\[at\]/@/g' -e 's/hxxp:/http:/g' -e 's/hxxps:/https:/g' $1
