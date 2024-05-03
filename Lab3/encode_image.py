import base64
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
if __name__ == "__main__":
    image_path = "/Users/14435/Desktop/New folder/Lab3/test.jpg"

# Getting the base64 string
    base64_image = encode_image(image_path)
    print(base64_image)
    ## save the base64 string to a temporary file
    with open("/Users/14435/Desktop/New folder/Lab3/test.txt", "wb") as fh:
        fh.write(base64.b64decode(base64_image))
