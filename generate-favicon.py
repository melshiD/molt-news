#!/usr/bin/env python3
from PIL import Image, ImageDraw

# Create 32x32 favicon
size = 32
img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Purple gradient background (approximate)
for y in range(size):
    ratio = y / size
    r = int(124 + (168 - 124) * ratio)
    g = int(58 + (85 - 58) * ratio)
    b = int(237 + (247 - 237) * ratio)
    draw.rectangle([(0, y), (size, y+1)], fill=(r, g, b))

# Left bubble (human - rounded)
draw.rounded_rectangle([(3, 6), (13, 15)], radius=2, fill=(255, 255, 255, 240))
draw.polygon([(6, 15), (5, 18), (9, 15)], fill=(255, 255, 255, 240))

# Right bubble (bot - sharp corners)
draw.rectangle([(19, 6), (29, 15)], fill=(255, 255, 255, 255))
draw.polygon([(26, 15), (27, 18), (23, 15)], fill=(255, 255, 255, 255))

# Merge point
draw.ellipse([(14, 7), (18, 11)], fill=(255, 255, 255, 255))

img.save('favicon.png', 'PNG')

# Create 16x16 version
img16 = img.resize((16, 16), Image.Resampling.LANCZOS)
img16.save('favicon-16.png', 'PNG')

print("✓ favicon.png (32x32)")
print("✓ favicon-16.png (16x16)")
