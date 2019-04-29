from PIL import Image
from pytesseract import image_to_string
#from smartencoding import smart_unicode

openModel = Image.open('KecamatanModel.jpg')
fOpen = open("output.txt","w+")
getStringImg =  image_to_string(openModel)

print getStringImg
#fOpen.write(str(getStringImg))
