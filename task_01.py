#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module: BaseError"""


class BaseError(Exception):
    """BaseError class extending Exception."""


class StringError(BaseError, TypeError):
    """String Error class subclassed to BaseError and TypeError."""


class NumberError(BaseError, TypeError):
    """Numbe Error class subclassed to BaseError and TypeError."""


class NonZeroError(NumberError):
    """Non-zero Error class subclassed to NumberError class."""
