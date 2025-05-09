from PIL import Image
import pytesseract

# Path to the image file
image_path = 'image_recog/test_image.png'

# Load image
#img = Image.open("your_image.jpg").convert("L")  # L = grayscale

img = Image.open(image_path)

# Extract text using Tesseract
text = pytesseract.image_to_string(img)

# Output the text
print(text)
