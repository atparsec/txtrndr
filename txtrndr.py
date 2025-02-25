import random, sys, os, argparse
from PIL import Image, ImageDraw, ImageFont

def bright(rgb: tuple) -> float:
    """
    Get pixel brightness using weighted average
    """
    return (rgb[0]*0.299 + rgb[1]*0.587 + rgb[2]*0.114) / 255

def gb_noise(rgb: tuple) -> tuple:
    """
    Add some noise to green and blue channels
    """
    return (rgb[0], rgb[1] + max(0,min(255,random.randint(-20, 20))), max(0,min(255,rgb[2] + random.randint(-20, 20))))

def generate(src, dest, charset):
    # Validate
    if not charset:
        charset = random.choice([f for f in os.listdir("./charsets") if f.endswith(".txt")])
    if not dest:
        ext = "." + src.split(".")[-1]
        dest = src.replace(ext, "_") + "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=5)) + ext
    if not os.path.exists(src):
        raise FileNotFoundError(f"Source image {src} not found")
    if not os.path.exists(f"./charsets/{charset}"):
        raise FileNotFoundError(f"Charset {charset} not found")
    
    # Load data
    with open(f"./charsets/{charset}", "r", encoding="utf-8") as f: 
        chars = f.readline().rstrip()
        dense = f.readline().rstrip().split("=")[1] == "True"
    
    # Setup
    baseimg = Image.open(src)
    size = baseimg.size
    basepix = baseimg.load()

    newImage = Image.new('RGB', size)
    draw = ImageDraw.Draw(newImage)

    count = 1000*(1+int(dense))
    font_LUT = {}

    # Generate
    for i in range(count):
        x, y = random.randint(0, size[0] - 1), random.randint(0, size[1] - 1)
        char = random.choice(chars)
        brt = bright(basepix[x, y])
        sz = int(10 + (brt * 100))
        color = (int(255*brt), 0, 0) if random.random()*2 < brt else gb_noise(basepix[x, y])
        if sz not in font_LUT:  font_LUT[sz] = ImageFont.truetype("C:/Windows/Fonts/MSMINCHO.TTC", sz)
        draw.text((x, y), char, color, font=font_LUT[sz])
        
    newImage.save(dest)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a new image with text using a charset')
    parser.add_argument('src', type=str, help='Source image', default="./example/earth_publicdomain.png")
    parser.add_argument('--dest', type=str, help='Destination image')
    parser.add_argument('--charset', type=str, help='Charset')
    args = parser.parse_args()
    generate(args.src, args.dest, args.charset)

