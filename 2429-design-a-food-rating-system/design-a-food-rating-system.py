# invariant that the cuisine and food exist 
# sorted set in decesding order (use negative values)

from sortedcontainers import SortedSet
from collections import defaultdict

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_map = defaultdict(SortedSet)  # cuisine -> (rating, food)
        self.food_map_2 = {} # food --> (cuisine, rating)

        for i in range(len(foods)):
            self.food_map[cuisines[i]].add((-ratings[i], foods[i]))
            self.food_map_2[foods[i]] = (cuisines[i], -ratings[i])

    def changeRating(self, food: str, newRating: int) -> None:
        c,r = self.food_map_2[food][0], self.food_map_2[food][1]

        self.food_map[c].remove((r, food))
        self.food_map[c].add((-newRating, food))

        self.food_map_2[food] = (c, -newRating)

    def highestRated(self, cuisine: str) -> str:
        return self.food_map[cuisine][0][1] # cuisine --> first element in sorted set --> food


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)