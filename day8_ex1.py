### Coding exercise 1 from day 8 - Function to calculate number of cans of paint

import math 

def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    result = math.ceil(number_of_cans)
    print(f"You'll need {result} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

