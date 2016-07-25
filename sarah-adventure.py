from adventure_lib.advent import *
from adventure_lib.advent import Game, Location, Connection, Object, Animal, Robot, Pet, Player
from adventure_lib.advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION


game = Game("Sarah's Adventure")

living_room = game.new_location(
    "Living Room",
    "A small, cosy living room. There is a wooden windowed door to the"
    " west leading outside into the garden, a wooden door to the south, "
    "and a doorway to the east.")

garden = game.new_location(
    "Garden",
    "A small square paved garden, bordered by flowerbeds. The flowerbeds "
    "contain a number of common herbs, some brightly coloured flowers, "
    "and a large patch of rhubarb. The garden is bordered by thin wooden "
    "fences to the north and south, and a stone wall covered in ivy on the "
    "northern side."
)

game.new_connection("Wooden Windowed Door", living_room, garden, [OUT, WEST], [IN, EAST])

player = game.new_player(living_room)

game.run()