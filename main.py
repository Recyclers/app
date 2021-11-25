from pyzbar.pyzbar import decode
from matplotlib.pyplot import imread
from sys import argv

img = imread(argv[1])
result = decode(img)
print(result)
