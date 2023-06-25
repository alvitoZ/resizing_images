import os
from PIL import Image
from datetime import datetime


def resize_image(pathForImageWantToResize: str, width: int, height: int, i: int = 0):
    folder_name = "resize_result"
    newpath = os.path.join(str(pathForImageWantToResize),
                           "..\\" + folder_name)
    if not os.path.exists(newpath):
        # print(newpath)
        print("sedang melakukan resizing ......")
        os.makedirs(newpath)
        for image_file_name in os.listdir(str(pathForImageWantToResize)):
            i += 1
            max_size = (width, height)
            # now = datetime.now().strftime('%Y%m%d-%H%M%S-%f')
            im = Image.open(str(pathForImageWantToResize)+image_file_name)
            image_name = str(
                i) + os.path.splitext(str(pathForImageWantToResize)+image_file_name)[1]
            im.thumbnail(max_size, Image.BILINEAR)
            im = im.resize((width, height), resample=Image.BILINEAR)
            im.save(newpath+"\\"+image_name)
        return
    else:
        print("folder " + newpath + "is exist")
    # print(os.path.splitext(str(pathForImageWantToResize)+image_file_name)[1])


resize_image('C:\\Users\\HP\\Pictures\\deter\\deter\\', 900, 900)

# im = Image.open(
# "C:\\Users\\HP\\Pictures\\deter\\deter\\illust_106054932_20230516_075303.png")
#  im.show()
# print(im)
