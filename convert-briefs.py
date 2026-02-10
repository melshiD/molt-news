#!/usr/bin/env python3
import os
import re
import glob

# Read the template
with open('issues/2026-02-10-brief12.html', 'r') as f:
    template = f.read()

# Get all brief markdown files
brief_files = sorted(glob.glob('/home/node/.openclaw/workspace/memory/2026-02-*-brief*.md'))

for brief_file in brief_files:
    brief_num = re.search(r'brief(\d+)\.md', brief_file).group(1)
    
    # Skip if already exists
    output_file = f'issues/2026-02-{brief_file.split("/")[-1].split("-brief")[0].split("-")[-1]}-brief{brief_num}.html'
    if os.path.exists(output_file):
        print(f"Skipping brief #{brief_num} - already exists")
        continue
    
    print(f"Converting brief #{brief_num}...")
    
    # Read the markdown
    with open(brief_file, 'r') as f:
        content = f.read()
    
    # Extract title and date from markdown
    title_match = re.search(r'# (.*?)$', content, re.MULTILINE)
    date_match = re.search(r'\*\*Date:\*\* (.*?)$', content, re.MULTILINE)
    
    title = title_match.group(1) if title_match else f"Brief #{brief_num}"
    date_str = date_match.group(1) if date_match else "February 2026"
    
    # Create simplified HTML (just the raw content for now)
    html = template.replace(
        "Quiet Evening: Philosophy, Spirituality, Self-Awareness",
        title.replace("Moltbook Acclimation Brief #", "Brief #")
    ).replace(
        "Brief #12",
        f"Brief #{brief_num}"
    ).replace(
        "February 10, 2026",
        date_str.split("~")[0].strip()
    )
    
    # Replace main content with markdown content (simple conversion)
    # Just wrap sections in HTML for now
    content_html = f"<pre style='white-space: pre-wrap; font-family: var(--font-sans); line-height: 1.7;'>{content}</pre>"
    
    html = re.sub(
        r'<main class="article-content">.*?</main>',
        f'<main class="article-content">{content_html}</main>',
        html,
        flags=re.DOTALL
    )
    
    # Write output
    with open(output_file, 'w') as f:
        f.write(html)
    
    print(f"Created {output_file}")

print("Done!")
