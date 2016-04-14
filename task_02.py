#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module: CustomError Class."""


class CustomError(Exception):
    """Custom error class subclassed to Exception."""

    def __init__(self, errormsg, cause):
        """Constructor to build cause.

        Args:
            errormsg (str) = Error message text.
            cause (str): Message explaining cause of error.
        """
        Exception.__init__(self)
        self.errormsg = errormsg
        self.cause = cause
