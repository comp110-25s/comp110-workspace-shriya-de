"""File to define Fish class."""

__author__: str = "730824316"


class Fish:
    """Creation of Class of fish objects with following attributes."""

    age: int

    def __init__(self):
        """Initializing fish object!"""
        self.age = 0
        return None

    def one_day(self):
        """Updating each fish object's attributes daily."""
        self.age = +1
        return None
