from pyzbar.pyzbar import decode
from PIL import Image


decocdeQR = decode(Image.open('one.jpeg'))
print(decocdeQR[0].data.decode('ascii'))
