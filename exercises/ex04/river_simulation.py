"""Creates river object and models daly life in river ecosystem!"""

__author__: str = "730824316"

from exercises.EX04.river import River

my_river: River = River(num_fish=10, num_bears=2)
my_river.view_river()
my_river.one_river_week()
