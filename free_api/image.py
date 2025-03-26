import requests
from PIL import Image
from io import BytesIO

# Image URL
url = "https://randomuser.me/api/portraits/women/59.jpg"

# Fetch the image
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# Display the image
img.show()


