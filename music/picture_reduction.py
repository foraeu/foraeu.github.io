from PIL import Image
import os

# Open an image file
path = r"static/music/"
with Image.open(path + "the rain.jpg") as img:
    # Resize image
    img = img.resize((200, 200))
    # Save it back to the current directory with quality set to 70
    current_directory = os.getcwd()
    img.save(os.path.join(path, "the rain.jpg"), quality=70)