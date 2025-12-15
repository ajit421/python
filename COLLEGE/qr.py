import qrcode

# Data to be encoded
data = "https://www.google.com"

# Generate the QR code
img = qrcode.make(data)

# Save the QR code image
img.save("my_qrcode.png")