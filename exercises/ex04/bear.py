"""File to define Bear class."""

__author__: str = "730824316"


class Bear:
    """Creating class of Bear objects, each bear has age and hunger_score."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes each bear object."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Updating each bear object's attributes daily."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Asssigning bear's hunger_score based on number of fish eaten."""
        self.hunger_score += num_fish
        return None
