# -*- encoding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import time


def foo(number):
    return number * 2


def prime_numbers(limit):
    figures = list(range(2, limit + 1))
    for prime in figures:
        for multiple in range(prime * 2, limit + 1, prime):
            if multiple in figures:
                figures.remove(multiple)
    return figures


def _evil():
    print(int(time.time()))
    time.sleep(1)


def evil():
    i = 0
    while i < 300:
        try:
            _evil()
        except:
            print('ZONK!')
        i += 1
    return 1
