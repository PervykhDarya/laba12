# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    data = set()

def generate(n, string='', level=0):
    if n == 0:
        return string
    if n == level:
        data.add(string)
        return string
    line = f"({string})"
    generate(n, string=line, level=level+2)
    line_2 = f"{string}()"
    generate(n, string=line_2, level=level + 2)
    line_3 = f"(){string}"
    generate(n, string=line_3, level=level+2)
    return 1

n = int(input())
generate(n)
print(data)
