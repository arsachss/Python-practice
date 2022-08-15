import pyqrcode
import png
import cv2
import os
import glob
from threading import Timer

type_link = input("Enter your URL here.\n")
file_name = input("Enter file name to be saved.\n")

qr_code = pyqrcode.create(type_link)
qr_code.png(file_name +".png", scale=5)

#saving qrcode image created
image = cv2.imread(file_name+'.png')
#path to save the qrcode image
path = r'D:\User Docs\Desktop\New Folder' #<specify your directory to save the generated QrCode image as in example>
(cv2.imwrite(os.path.join(path,file_name+'.png'), image))

#delete copied/duplicated qrcode
def delete():
    filename = file_name + ".png"
    base_dir = "D:\\User Docs\\Desktop\\MyFolder\\python practice\\" #<specify this 'python file' saved path as in example>
    fullpath = os.path.join(base_dir, filename)
    os.remove(fullpath)
    

t = Timer(0.2, delete)
t.start()

print("Done created QrCode")
