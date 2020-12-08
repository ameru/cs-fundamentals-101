"""Project 5 - Pixel Magic
CPE 101
Section: 3 & 7
Name: Amy Ru
Cal Poly User: amru
"""
# top-left pixel location: <0, 0>
# bottom-right pixel location: <width - 1, height - 1>

def main():
    import sys
    arg_list = sys.argv
    if len(arg_list) < 3 or len(arg_list) > 6 or\
       len(arg_list) >= 3 and ('-decoded' not in arg_list and\
                              '-faded' not in arg_list):
            
        print('Usage: python pixel_magic.py <mode> <image>')
        print('-decoded for decode\n-faded for fade')
        return

    if '-decoded' in arg_list:
        decode_status = True
        arg_list.remove('-decoded')
    else: 
        decode_status = False

    if '-faded' in arg_list:
        fade_status = True
        arg_list.remove('-faded')
        if not len(arg_list) == 5:
            print('Usage: python pixel_magic.py <image> <row> <column> '\
                   '<radius>')
            return 

        for thing in arg_list[2:]:
            if not thing.isdigit():
                print('Usage: python pixel_magic.py <image> <row> <col> '\
                   '<radius>')
                print('Error: Invalid Mode')
                return 
    else:
        fade_status = False

    ### Error messages:
    # Usage: python pixelmagic.py <mode> <image>
    # Error: Unable to Open (filename)
    # Error: Invalid Mode

    try:
        pixels = read_image(arg_list[1])
        width = pixels[0:3] 
        del pixels[0:3]
        pixels = pixel_list_size(pixels)
        if decode_status:
            decoded_image = find_image(pixels)
            write_image('decoded.ppm',decoded_image,width)
        if fade_status:
            faded_image = fade_image(pixels,int(arg_list[2]),\
                          int(arg_list[3]),int(arg_list[4]),width) 
            write_image('faded.ppm',faded_image,width)
    except:
        print('Error: Unable to open {0}'.format(arg_list[1]))


def read_image(file_name):
    f = open(file_name, 'r')
    store_list = []
    while True:
        line = f.readline()
        if line == '':
            break
        line_list = line.split()
        for sublist in line_list:
            store_list.append(int(sublist))
    f.close()
    return store_list 



def write_image(file_name,pixels,width):
    f = open(file_name, 'w')
    f.write('P3\n')
    f.write('{0} {1}\n'.format(width[0],width[1]))
    f.write('{0}\n'.format(width[2]))
    for pixel_list in pixels:
        for pixel in pixel_list: 
            f.write('{0:d}\n'.format(pixel))
    f.close()

# ensuring pixel length of 3
def pixel_list_size(sq):
    i = 0                                                                       
    full_list = []                                                              
    sub_list = []                                                               
    for num in sq:                                                          
        i += 1                                                                  
        if i <= 3:                                                              
            sub_list.append(num)                                                
        else:                                                                   
            full_list.append(sub_list)                                          
            sub_list = []                                                       
            sub_list.append(num)                                                
            i = 1                                                               
    return full_list + [sub_list] 
    
def find_image(pixels) -> list:
    """ Returns decoded pixels. Corresponds to the filter mode ‘decode’.
    Arguments:
        pixels(list): list of 3 numerical digits
    Returns:
        list: Returns decoded list of numerical digits.
    """
    for pixel in pixels:
        pixel[0] = pixel[0]*10
        if pixel[0] > 255:
            pixel[0] = 255
        pixel[1] = pixel[0]
        pixel[2] = pixel[0]
    return pixels

def fade_image(pixels, width, row, col, radius) -> list:
    """ Returns faded pixels. Corresponds to the filter mode ‘fade’.
    Arguments:
        pixels(list): list of 3 numerical digits
        width(int): numerical width of image
        row(int): number of rows faded
        col(int): number of columns faded
        radius(int): user input radius
    Returns:
        list: returns the updated pixel list values.
    """
    # usage: python pixelmagic.py fade <image> <row> <col> <radius>
    width = width[0] 
    for i, pixel in enumerate(pixels):
        pixel_y = i / width
        pixel_x = i % width 
        dist_x = pixel_x - col
        dist_y = pixel_y - row
        distance = ((dist_x)**2 + (dist_y)**2)**0.5   
        scale_value = (radius - distance) / radius
        if scale_value < 0.2:
            scale_value = 0.2

        pixel[0] = int(pixel[0]*scale_value)
        pixel[1] = int(pixel[1]*scale_value)
        pixel[2] = int(pixel[2]*scale_value)
    return pixels

def denoise_image(pixels, width, height, reach, beta):
    """ Returns denoiseed pixels. Corresponds to the filter mode ‘denoise’.
    Arguments:
        pixels(list): list of 3 numerical digits
        width(int): numerical width of image
        height(int): numerical height of image
        reach(int): reach distance between two pixels
        beta(): 
    Returns:
        list: returns the updated pixel list values.
    """
# usage: python pixelmagic.py denoise <image> <reach> <beta>
    pass


if __name__== "__main__":
    main()
