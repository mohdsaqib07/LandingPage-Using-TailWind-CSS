from rembg import remove
from PIL import Image

input_path = './phone.jpg'
output_path = './removephone.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)