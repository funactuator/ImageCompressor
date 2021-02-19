# For compressing a single image file
# We are using Pillow here for image processing
import PIL
from PIL import Image
import os,sys

# width = 300
source_dir = "/home/darkcarnage/Videos/Pictures"
dest_dir ='/home/darkcarnage/Videos/PicturesCompressed'

# we can take this path of a folder via dialog, prompt which we will see later

def resize_pic(pic, width):
    img = Image.open(source_dir+'/'+pic)
    # print(img.size)
    wpercent = (width/float(img.size[0]))
    hsize = int(float(img.size[1]*float(wpercent)))
    img = img.resize((width, hsize), PIL.Image.ANTIALIAS)
    img.save(dest_dir+'/'+pic)

# Taking a folder to compress it whole
count = 0
files = os.listdir(source_dir)
for file in files:
    count+=1
    resize_pic(file, 500)
    # count+=1
    print(count, 'done')
