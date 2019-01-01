from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals

## WORLD PARAMS
# blocknames = ["dirt", "grassdirt", "stone", "water", "wood", "leaf", "snowdirt", "coin"]
# blockcolor = ["brown", "green", "gray", "blue", "light brown", "light green", "white", "gold"]
blocktypes = [0, 1, 2, 3, 4, 5, 6, 7] # each number corresponds to a name above
length = 15
depth = 15 # these are the parameters for generating the 2D list
earth = [[6]*length for i in range(depth)]

## HELPER FUNCTIONS
def escape(btype):
    bgcolors = [40, 41, 42, 43, 44, 45, 46, 47]
    return "\033[1;37;" + str(bgcolors[btype]) + "m" + "[]"
def visualize(world):
    for subworld in world:
        for block in subworld:
           print(escape(block), end='')
        print("\n")
    print("\n")
def choose_zone(height):
    return (height / depth) * 8 - 1 # the depth of the block over the depth of the world, on an 8 point scale, shifted to a 7-point scale to match up with the block types
def choose_terrain(height):
    zone = choose_zone(height)
    return zone # TODO add some randomness to make this less of a hard line
def terrainify(world):
    height = 0
    for subworld in world:
        for block in subworld:
            block = choose_terrain(height)
        height+=1
    return world
visualize(terrainify(earth))
