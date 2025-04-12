"""My first exercise in COMP110!"""

__author__ = "730824316"


def greet(name: str) -> str:
    """A welcoming first function def"""
    return "Hello, " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("What is your name? ")))
