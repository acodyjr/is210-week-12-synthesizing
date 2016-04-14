#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


def exception_test(arg1, arg2, arg3):
    """Catch TypeErros, KeyErros, and IndexErrors.

    Args:
        arg1 (mixed): Argument 1.
        arg2 (mixed): Argument 2.
        arg3 (mixed): Argument 3.

    Returns:
        caught (bool): Whether error was caught or not.

    Examples:
        >>>exception_test(['apple'], 0, 'p')
        False

        >>>exception_test(43, 1, 1)
        True
    """
    caught = False
    try:
        arg1[arg2].index(arg3)
    except (TypeError, LookupError):
        caught = True

    return caught
