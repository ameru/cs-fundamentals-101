"""Project 5 Tests - Pixel Magic
CPE 101
Section: 3 & 7
Name: Amy Ru
Cal Poly User: amru
"""
import pixelmagic

# pixel_list_size tests

assert pixelmagic.pixel_list_size([1,2,3,4,5,6]) == [[1,2,3],[4,5,6]] 
assert pixelmagic.pixel_list_size([1,2,3,4,5,6,7]) == [[1,2,3],[4,5,6],[7]]                  
assert pixelmagic.pixel_list_size([1,2,3,4,5,6,7,8]) == [[1,2,3],[4,5,6],[7,8]]  

# find_image tests

test1 = pixelmagic.pixel_list_size(range(9))
test2 = pixelmagic.pixel_list_size([5]*9)
test3 = pixelmagic.pixel_list_size([10,100,1000,10000,100000,1000000])

assert pixelmagic.find_image(test1) == [[0,0,0],[30,30,30],[60,60,60]]
assert pixelmagic.find_image(test2) == [[50,50,50],[50,50,50],[50,50,50]]
assert pixelmagic.find_image(test3) == [[100,100,100],[255,255,255]]

# fade_image tests

fade1 = pixelmagic.pixel_list_size(range(27))
fade1_width  = [3,3,255]

assert pixelmagic.fade_image(fade1, 1, 1, 1, fade1_width)\
       == [[0,0,0], [0,0,1], [1,1,1],\
           [1,2,2], [12,13,14], [3,3,3],\
           [3,3,4], [4,4,4], [4,5,5]]

fade2 = pixelmagic.pixel_list_size(range(36))
fade2_width = [3,4,255]

assert pixelmagic.fade_image(fade2, 1, 1, 1, fade2_width)\
       == [[0,0,0], [0,0,1], [1,1,1],\
           [1,2,2], [12,13,14], [3,3,3],\
           [3,3,4], [4,4,4], [4,5,5],\
           [5,5,5], [6,6,6], [6,6,7]]

fade3 = pixelmagic.pixel_list_size([0]*27)
fade3_width = [3,3,255]

assert pixelmagic.fade_image(fade3, 1, 1, 1, fade3_width)\
       == [[0,0,0]]*9