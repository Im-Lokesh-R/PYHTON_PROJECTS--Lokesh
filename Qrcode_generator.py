#basic generator 

import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

def create_qrcode():
    info=input("Information--> ")
    img=qrcode.make(info)
    file_name=input("Enter the file name .png: ")
    path=(f"dir_path/{file_name}")
    img.save(path)
    return path

def decode_qrcode(path):
    img=Image.open(path)
    info=decode(img)
    print(info)

if __name__=="__main__":
    path=create_qrcode()
    print("created succeffuly")
    decode_qrcode(path)


