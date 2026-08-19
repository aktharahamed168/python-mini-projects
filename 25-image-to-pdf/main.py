from PIL import Image

image_path = "C:/Users/aktha/OneDrive/Desktop/Linkedin Stuffs/sample.jpg"
output_file = "output.pdf"

image = Image.open(image_path)

if image.mode != "RGB":
    image = image.convert("RGB")

image.save(output_file)

print("===== Image to PDF =====")
print("Image converted successfully.")
print(f"PDF created: {output_file}")
