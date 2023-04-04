from PIL import Image, ImageDraw, ImageFont

image_names = [
    "Wolverine",
    "Mason",
    "Hunter"
]

W, H = 512, 512

for image_name in image_names:
    fnt = ImageFont.truetype('arial.ttf', int(108 / len(image_name) * 7))
    image = Image.new(mode="RGB", size=(W, H), color="white")
    draw = ImageDraw.Draw(image)
    _, _, w, h = draw.textbbox((0, 0), image_name, font=fnt)
    draw.text(((W-w)/2, (H-h)/2), image_name, font=fnt, fill=(0, 0, 0))
    image.save(f"./images/{image_name.lower()}.jpg")