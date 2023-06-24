import os
from PIL import Image
from datetime import datetime


def resize_image(i: int, pathForImageWantToResize: str):
    resize_result = "resize_result"
    newpath = os.path.join(str(pathForImageWantToResize),
                           "..\\" + resize_result)
    if not os.path.exists(newpath):
        # print(newpath)
        print("sedang melakukan resizing ......")
        os.makedirs(newpath)
    for image_file_name in os.listdir(str(pathForImageWantToResize)):
        i += 1
        new_width = 900
        new_height = 900
        max_size = (new_width, new_height)
        # now = datetime.now().strftime('%Y%m%d-%H%M%S-%f')
        im = Image.open(str(pathForImageWantToResize)+image_file_name)
        image_name = str(
            i) + os.path.splitext(str(pathForImageWantToResize)+image_file_name)[1]
        im.thumbnail(max_size, Image.BILINEAR)
        im = im.resize((new_width, new_height), resample=Image.BILINEAR)
        im.save(newpath+"\\"+image_name)

    # print(os.path.splitext(str(pathForImageWantToResize)+image_file_name)[1])


# resize_image(0, 'C:\\Users\\HP\\Pictures\\deter\\deter\\')

# im = Image.open(
# "C:\\Users\\HP\\Pictures\\deter\\deter\\illust_106054932_20230516_075303.png")
#  im.show()
# print(im)
