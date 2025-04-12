"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int  # tells you day of the river's lifecycle
    bears: list[Bear]  # list of different bear
    fish: list[Fish]  # list of fish to represent river's fish population

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """To keep bears that are 5 or younger"""
        surviving_bear = []  # new list with only bear age 5 or younger
        for bears in self.bears:
            if bears.age <= 5:
                surviving_bear.append(bears)  # populating new list
        self.bears = surviving_bear  # updating river bear population

        """To keep fish that are younger than 3 years of age"""
        surviving_fish = []
        for fish in self.fish:  # for the vlaue in the list of fish created in fish.py
            if fish.age <= 3:
                surviving_fish.append(fish)  # populating river fish population
        self.fish = surviving_fish  # updating river bear population

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        bears_left = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                bears_left.append(bear)
        self.bears = bears_left
        return None

    def repopulate_fish(self):
        # number of fish offspring to add
        fish_offspring_count: int = len(self.fish) // 2 * 4
        fish_added: int = 0
        # Adding fish offspring until required number is reached
        while fish_added < fish_offspring_count:
            self.fish.append(Fish())
            fish_added += 1
        return None

    def repopulate_bears(self):
        # number of new bears to add
        bears_offspring_count: int = len(self.bears) // 2
        bears_added: int = 0
        # Adding bear offspring until required number is reached
        while bears_added < bears_offspring_count:
            self.bears.append(Bear())
            bears_added += 1
        return None

    def view_river(self):
        """Prints status of bear and fish populations in a given River object"""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None

    def remove_fish(self, amount: int) -> None:
        removed: int = 0
        while (
            removed < amount and self.fish
        ):  # ensures there are still fish left in the List of fish
            self.fish.pop(0)  # esnures fish are rmeoved from the front of the list
            removed += 1
