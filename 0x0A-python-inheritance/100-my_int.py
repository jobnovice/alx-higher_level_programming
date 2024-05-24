#!/usr/bin/python3
"""class myInt extends from int"""


class MyInt(int):
    """New class MyInt implemented from int
      that inverts equality operations."""

    def __init__(self, value):
        """Instantiates MyInt based on the value"""
        super().__init__()

    def __eq__(self, other):
        """Override equality to behave as inequality"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override inequality to behave as equality"""
        return super().__eq__(other)
