"""Share card, 1200x630: the Ulam spiral with primes gold and semiprimes split, and the title."""
import math, pathlib
from PIL import Image, ImageDraw, ImageFont

out = pathlib.Path(__file__).resolve().parent.parent / "docs" / "card.jpg"
W, H = 1200, 630
img = Image.new("RGB", (W, H), (15, 20, 26))
d = ImageDraw.Draw(img)

def factors(n):
    f, k = [], 2
    while k * k <= n:
        while n % k == 0:
            f.append(k); n //= k
        k += 1
    if n > 1:
        f.append(n)
    return f

x = y = 0; dx, dy = 1, 0; seg = 1; steps = turns = 0
cell = 13; cx, cy = 900, 315
for n in range(1, 3400):
    f = factors(n)
    px, py = cx + x * cell, cy + y * cell
    if 0 <= px < W and 0 <= py < H:
        if len(f) == 1:
            d.ellipse([px - 4.5, py - 4.5, px + 4.5, py + 4.5], fill=(224, 164, 69))
        elif len(f) == 2:
            a = (f[0] * 37 + f[1] * 11) % 6
            ox, oy = math.cos(a) * 3.2, math.sin(a) * 3.2
            for s in (-1, 1):
                d.ellipse([px + s * ox - 2.2, py + s * oy - 2.2, px + s * ox + 2.2, py + s * oy + 2.2], fill=(76, 194, 179))
        elif n > 1:
            d.rectangle([px - 1, py - 1, px + 1, py + 1], fill=(51, 64, 76))
    x += dx; y += dy; steps += 1
    if steps == seg:
        steps = 0; dx, dy = -dy, dx; turns += 1
        if turns % 2 == 0:
            seg += 1

# fade the left for the words
fade = Image.new("L", (W, H), 0)
fd = ImageDraw.Draw(fade)
for i in range(760):
    fd.line([(i, 0), (i, H)], fill=int(255 * max(0.0, 1 - i / 760) ** 0.6))
img.paste(Image.new("RGB", (W, H), (15, 20, 26)), (0, 0), fade)

F = "/System/Library/Fonts/Supplemental/"
big = ImageFont.truetype(F + "Georgia Bold.ttf", 104)
th = ImageFont.truetype(F + "Tahoma Bold.ttf", 60)
small = ImageFont.truetype(F + "Courier New Bold.ttf", 28)
thsmall = ImageFont.truetype(F + "Tahoma.ttf", 30)
d.text((64, 120), "POST-QUANTUM, DRAWN WITH MATH", font=small, fill=(224, 164, 69))
d.text((60, 170), "All Factored", font=big, fill=(228, 233, 238))
d.text((64, 300), "แยกหมดแล้ว", font=th, fill=(154, 167, 179))
d.text((64, 420), "Paint, tables, a mail slot, a floodlight.", font=small, fill=(228, 233, 238))
d.text((64, 462), "ทำไมกุญแจบนอินเทอร์เน็ตกำลังเปลี่ยน", font=thsmall, fill=(154, 167, 179))
d.text((64, 560), "nanobotco.github.io/all-factored", font=small, fill=(76, 194, 179))
img.save(out, quality=88)
print(out)
