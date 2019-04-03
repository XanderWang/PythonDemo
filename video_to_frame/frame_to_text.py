
import sys
import os

try:
  import Image
except ImportError:
  from PIL import Image
import pytesseract

current_dir = os.path.abspath(os.path.dirname(sys.argv[0]))

image = Image.open("{0}{1}image{1}frame_{2}.jpg".format(current_dir, os.sep, 10))
code = pytesseract.image_to_string(image)
print('\n\n\n'+code)
