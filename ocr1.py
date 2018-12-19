import cv2
import numpy as np
import pytesseract
from PIL import Image
import base64

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    #resiging Image.
    img = cv2.resize(img, None, fx=1.4, fy=1.3, interpolation=cv2.INTER_CUBIC)
    #img = cv2.resize(img, None, fx=1.3, fy=1.3, interpolation=cv2.INTER_AREA)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite("removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite("thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open("thres.png"))
    #result = pytesseract.image_to_string(Image.open(img_path))

    return result




print ('--- Start recognize text from image ---')
result = (get_string('org_file_1.jpg'))
print (result)
#Conversing the unprinable character to utf-8 to print if properly.
new_result = result.encode('utf-8').decode('latin-1')

from PIL import Image, ImageDraw   
img = Image.new('RGB', (300,250), color = (0,0,0))  #Blank image creation with black background
d = ImageDraw.Draw(img)
d.text((10,10), new_result, fill=(255,255,255)) #writing text on the image
img.save('image.png')

print ("------ Done -------")
