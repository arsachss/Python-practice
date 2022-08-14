import pyqrcode
import png
import cv2
import os

type_link = input("Enter your URL here.\n")
file_name = input("Enter file name to be saved.\n")

qr_code = pyqrcode.create(type_link)
qr_code.png(file_name +".png", scale=5)


image = cv2.imread(file_name+'.png')
#path to save the qrcode image
path = r'D:\User Docs\Desktop\MyFolder'
(cv2.imwrite(os.path.join(path,file_name+'.png'), image))

print("Done")



