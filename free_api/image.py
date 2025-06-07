# If you see "ModuleNotFoundError: No module named 'PIL'", install Pillow with:
# pip install Pillow

import requests
from PIL import Image
from io import BytesIO

# Image URL
url = "https://randomuser.me/api/portraits/women/65.jpg"

# Fetch the image
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# Display the image
img.show()


