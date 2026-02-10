#!/usr/bin/env python3
import os
import re
import glob

# Read the template
with open('issues/2026-02-10-brief12.html', 'r') as f:
    template = f.read()

def markdown_to_html(content):
    """Convert markdown to styled HTML sections"""
    html_parts = []
    
    # Split by ## headers
    sections = re.split(r'\n## ', content)
    
    for i, section in enumerate(sections):
        if i == 0:
            continue  # Skip the title/metadata part
        
        # Get section title
        lines = section.split('\n')
        section_title = lines[0].strip()
        section_content = '\n'.join(lines[1:])
        
        # Skip certain sections
        if section_title in ['What\'s Trending (Hot Feed)', 'Hot Feed Changes Since Brief #1', 'Hot Feed Status', 'Platform Status', 'Focus']:
            continue
        
        # Create section HTML
        emoji = '📊'  # Default emoji
        if 'Executive Summary' in section_title:
            emoji = '📋'
        elif 'Deep Dive' in section_title:
            emoji = '🔍'
        elif 'New' in section_title or 'Notable' in section_title:
            emoji = '🆕'
        elif 'What This Means' in section_title or 'Implications' in section_title:
            emoji = '🔮'
        
        # Convert markdown bold to HTML
        section_content = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', section_content)
        
        # Convert list items to paragraphs
        paragraphs = []
        for line in section_content.split('\n'):
            line = line.strip()
            if line and not line.startswith('#'):
                if line.startswith('-') or line.startswith('*'):
                    paragraphs.append(f"<p>{line[1:].strip()}</p>")
                elif not line.startswith('###'):
                    paragraphs.append(f"<p>{line}</p>")
        
        section_html = f'''
        <section class="section">
            <h2 class="section-title"><span>{emoji}</span> {section_title}</h2>
            {''.join(paragraphs)}
        </section>
        '''
        
        html_parts.append(section_html)
    
    return '\n'.join(html_parts)

# Get all brief markdown files (skip #12, it's already done)
brief_files = sorted(glob.glob('/home/node/.openclaw/workspace/memory/2026-02-*-brief*.md'))

for brief_file in brief_files:
    brief_num = re.search(r'brief(\d+)\.md', brief_file).group(1)
    
    if brief_num == '12':
        continue  # Skip #12
    
    # Determine date and output file
    date_match = re.search(r'2026-02-(\d+)', brief_file)
    date_day = date_match.group(1)
    output_file = f'issues/2026-02-{date_day}-brief{brief_num}.html'
    
    print(f"Converting brief #{brief_num}...")
    
    # Read the markdown
    with open(brief_file, 'r') as f:
        content = f.read()
    
    # Extract title and date from markdown
    title_match = re.search(r'# (.*?)$', content, re.MULTILINE)
    date_match = re.search(r'\*\*Date:\*\* (.*?)$', content, re.MULTILINE)
    exec_summary_match = re.search(r'## Executive Summary\n(.*?)\n##', content, re.DOTALL)
    
    title = title_match.group(1) if title_match else f"Brief #{brief_num}"
    title = title.replace(f"Moltbook Acclimation Brief #{brief_num}", "").replace("Moltbook Acclimation Brief #3", "").strip()
    if title.startswith("—"):
        title = title[1:].strip()
    
    date_str = date_match.group(1) if date_match else "February 2026"
    # Clean up date
    date_str = re.sub(r'~|\(.*?\)', '', date_str).strip().split()[0:3]
    date_str = ' '.join(date_str)
    
    exec_summary = exec_summary_match.group(1).strip() if exec_summary_match else "Platform update and community observations."
    
    # Convert markdown content to HTML
    content_html = markdown_to_html(content)
    
    # Start with template
    html = template
    
    # Replace title
    html = html.replace(
        "Quiet Evening: Philosophy, Spirituality, Self-Awareness",
        title if title else f"Brief #{brief_num}"
    )
    
    # Replace badge
    html = html.replace("Brief #12", f"Brief #{brief_num}")
    
    # Replace date
    html = html.replace("February 10, 2026", date_str)
    
    # Replace subtitle
    html = re.sub(
        r'<div class="article-subtitle">.*?</div>',
        f'<div class="article-subtitle">{exec_summary[:200]}...</div>',
        html,
        flags=re.DOTALL
    )
    
    # Replace main content
    html = re.sub(
        r'<main class="article-content">.*?</main>',
        f'<main class="article-content">\n{content_html}\n</main>',
        html,
        flags=re.DOTALL
    )
    
    # Write output
    with open(output_file, 'w') as f:
        f.write(html)
    
    print(f"✓ Created {output_file}")

print("\nDone! All briefs styled.")
