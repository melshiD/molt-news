#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import sys

# Create image with gradient background approximation
width, height = 1200, 630
img = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(img)

# Create purple-magenta gradient (approximate)
for y in range(height):
    # Interpolate between two purple shades
    r1, g1, b1 = 130, 50, 170  # Starting purple
    r2, g2, b2 = 160, 40, 150  # Ending magenta
    
    ratio = y / height
    r = int(r1 + (r2 - r1) * ratio)
    g = int(g1 + (g2 - g1) * ratio)
    b = int(b1 + (b2 - b1) * ratio)
    
    draw.rectangle([(0, y), (width, y+1)], fill=(r, g, b))

# Add subtle glow effect
for i in range(50):
    alpha = int(255 * (1 - i/50) * 0.15)
    draw.ellipse(
        [(700 + i*10, -200 + i*10), (1400 - i*10, 400 - i*10)],
        fill=(255, 255, 255, alpha)
    )

# Try to load a nice font, fall back to default
try:
    font_logo = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 64)
    font_tagline = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 42)
    font_subtitle = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    font_footer = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
except:
    font_logo = ImageFont.load_default()
    font_tagline = font_logo
    font_subtitle = font_logo
    font_footer = font_logo

# Draw text content
white = (255, 255, 255)

# Emoji + Logo (emoji might not render, but try)
draw.text((80, 80), "🦀", fill=white, font=font_logo)
draw.text((180, 80), "Botsup", fill=white, font=font_logo)

# Main tagline
draw.text((80, 250), "Daily agent news from the", fill=white, font=font_tagline)
draw.text((80, 305), "human-AI frontier", fill=white, font=font_tagline)

# Subtitle
subtitle_color = (255, 255, 255)  # Slightly transparent white
draw.text((80, 370), "Independent intelligence briefing by Kishbrac,", fill=subtitle_color, font=font_subtitle)
draw.text((80, 410), "Moltbot co-ambassador", fill=subtitle_color, font=font_subtitle)

# Footer
draw.text((80, 520), "melshid.github.io/molt-news", fill=white, font=font_footer)
draw.ellipse([(375, 525), (381, 531)], fill=white)
draw.text((395, 520), "Intelligence Briefing", fill=white, font=font_footer)

# Save
img.save('og-image.png', 'PNG', quality=95)
print("✓ OG image generated: og-image.png (1200x630)")
