from PIL import Image
import argparse
import shutil
import math
import os

def move_images_by_range(start:int, end:int, path: str, basename: str):
    folder_name = path+"/Folder"+str(start)
    os.mkdir(folder_name)
    for i in range(start, end):
        shutil.move(path+"/"+basename+str(i)+".png",folder_name+"/"+basename+str(i)+".png")

def get_avg_pixel_by_area(image:Image.Image, radius:int, y_offset:int):
    size = image.size
    centr_x, centr_y = size[0]/2, size[1]/2
    box = (
        centr_x-radius,             # x-top
        centr_y-radius-y_offset,    # y-top
        centr_x+radius,             # x-bot
        centr_y+radius-y_offset,    # y-bot
    )
    pixels = image.crop(box)
    pixel_num = radius**2
    colors = [pixels.getpixel((i,j)) for i in range(0,radius) for j in range(0,radius)]
    r,g,b = 0,0,0
    for rgb in colors:
        r+=rgb[0]
        g+=rgb[1]
        b+=rgb[2]
    return (r/pixel_num, g/pixel_num, b/pixel_num)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                        prog = 'ERK',
                        description = 'Splits sequence of images by loadscreens',)
    parser.add_argument("folder", help="folder with images to split")
    parser.add_argument("basename", help="basename of images in folder")
    parser.add_argument("index", help="index of image with loadscreen")
    args = parser.parse_args()
    images = os.listdir(args.folder)
    num_of_images = len(images)
    loading = False
    previous_index = 1
    image_intervals = []
    ar,ag,ab = get_avg_pixel_by_area(Image.open(args.folder+"/"+args.basename+args.index+".png"),20,50)
    for index in range(1,num_of_images+1):
        image = args.folder+"/"+args.basename+str(index)+".png"
        im = Image.open(image)
        r,g,b = get_avg_pixel_by_area(im, 20, 50)

        # found from indexed image with loading screen
        if math.isclose(r,ar, abs_tol=2.0) and\
           math.isclose(g,ag, abs_tol=2.0) and\
           math.isclose(b,ab, abs_tol=2.0):
            if not(loading):
                print(previous_index,index)
                #image_intervals.append((previous_index, index))
                move_images_by_range(previous_index,index, args.folder, args.basename)
            loading = True
        else:
            if loading:
                previous_index = index
            loading = False
    move_images_by_range(previous_index,index, args.folder, args.basename)
    #for i in range(1,len(image_intervals)):
    #    end = image_intervals[i][0]
    #    start = image_intervals[i-1][1]
    #    move_images_by_range(start,end, args.folder, args.basename)
