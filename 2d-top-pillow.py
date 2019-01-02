from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals

from PIL import Image, ImageDraw
import datetime
import random
from math import sqrt

height_width = 500# square image; height=width
iterations = 500
im = Image.new('RGB', (height_width, height_width))
draw = ImageDraw.Draw(im)

def render_image():
    # im.save(str(datetime.datetime.today().strftime('%Y-%m-%d_%I-%M%p')) + ".png")
    # uncomment previous line to save results
    im.show()

city = [(46,44,46),(29,25,33),(72,68,76)]
grassy = [(88,153,42),(143,153,42),(100,119,76)]
water = [(50,82,153),(26,54,114),(59,78,119)]
desert = [(137,90,46),(124,94,24),(130,110,63)]
stone = [(147,146,141),(137,136,133),(104,104,104)] # these were all selected by hand
biomes = city+grassy+water+desert+stone

def random_coords():
    x = random.randrange(height_width)
    y = random.randrange(height_width)
    return (x,y)

def place_inital_dots():
    for biome in biomes:
       im.putpixel(random_coords(), biome)

# def true_or_false(probability):
#     if random.random() < probability:
#         return True
#     else:
#         return False

def distance_to_point(coord1, coord2):
    (x,y) = coord1
    (x1,y1) = coord2
    return sqrt((x1-x)**2+(y1-y)**2)

def get_new_x(x, x_offset):
    if (x + x_offset) < height_width-2 and (x + x_offset) > 2:
        new_x = x + x_offset
        return new_x
    else:
        new_x = random.randrange(height_width)
        return new_x

def get_new_y(y, y_offset):
    if (y + y_offset) < height_width-2 and (y + y_offset) > 2:
        new_y = y + y_offset
        return new_y
    else:
        new_y = random.randrange(height_width)
        return new_y

def offset_coords(coords):
    x_offset = random.randint(-1,1)
    y_offset = random.randint(-1,1)
    (x, y) = coords
    return (get_new_x(x, x_offset), get_new_y(y,y_offset))

def generate_new_dot():
    search_start_point = random_coords()
    biome_of_choice = random.choice(biomes)
    x_offset = random.randint(-1,1)
    y_offset = random.randint(-1,1)
    for x in range(height_width):
        for y in range(height_width):
            pixel = im.getpixel((x,y))
            if pixel == biome_of_choice:
                im.putpixel(offset_coords(search_start_point), biome_of_choice)

def iterate(num):
    for i in range(num):
        generate_new_dot()

place_inital_dots()
# iterate(iterations)
render_image()
