import pandas as pd
import gdown
import os
import re

# === CONFIG ===
sheet_id = "1LJHIka0mOQquqnMhxm28p6GZxIkpLLzaYo2JnBRMztA"
sheet_csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

# Prompt for project prefix and range
project_prefix = input("Enter project name prefix (e.g. 'Gravity'): ").strip()
start_row = int(input("Start row number (1-based index): ")) - 1
end_row = int(input("End row number (inclusive): "))

# Load sheet directly from URL
df = pd.read_csv(sheet_csv_url)

# Column definitions (update if headers change)
name_col = "Firstname Lastname"
title_col = "Title of artwork"
desc_col = "Concise description of artwork and artistic choices"
upload_col = "Upload your file (.png, .gif)\n(If your project is a p5.js simulation link, still upload a .png thumbnail of 1 frame)"
p5_col = "p5.js Fullscreen link"
medium_col = "Medium"

# Output directories (must already exist)
png_folder = "ProceduralArt/png"
gif_folder = "ProceduralArt/gif"

html_blocks = []

# Iterate over selected range
for idx, row in df.iloc[start_row:end_row].iterrows():
    name = row.get(name_col, "").strip()
    if not name:
        continue

    first, last = name.split()[0], name.split()[-1]
    title = str(row.get(title_col, "")).strip()
    alt = str(row.get(desc_col, "")).strip()
    medium = str(row.get(medium_col, "")).lower()
    link = str(row.get(p5_col, "")).strip()
    drive_url = str(row.get(upload_col, "")).strip()

    if "drive.google.com" not in drive_url:
        print(f"⚠️ Skipping {name} — No valid Drive link")
        continue

    match = re.search(r"(?:/d/|id=)([a-zA-Z0-9_-]+)", drive_url)
    if not match:
        print(f"⚠️ Could not extract file ID from: {drive_url}")
        continue

    file_id = match.group(1)

    # Decide file extension and target folder
    if "static" in medium:
        ext = ".png"
        folder = png_folder
    elif "animation" in medium:
        ext = ".gif"
        folder = gif_folder
    elif "simulation" in medium:
        ext = ".png"
        folder = png_folder
    else:
        print(f"⚠️ Skipping {name} — Unknown medium '{medium}'")
        continue

    clean_first = re.sub(r'\W+', '', first)
    clean_last = re.sub(r'\W+', '', last)
    filename = f"{project_prefix}{clean_first}{clean_last}{ext}"
    filepath = os.path.join(folder, filename)

    print(f"⬇️ Downloading: {filename} → {folder}/")
    gdown.download(f"https://drive.google.com/uc?id={file_id}", filepath, quiet=False)

    img_src = f"./{folder}/{filename}"
    source_link = f'<a class="source-link" href="{link}" target="_blank">(source)</a>' if link.startswith("http") else ""

    div_class = "artpiece gif" if ext == ".gif" else "artpiece"

    if "simulation" in medium:

        block = f'''
        <div class="{div_class}">
            <a href="{link}" target="_blank">
                <img src="./{ext[1:]}/{filename}" 
                    alt="{alt}" 
                    class="artImage">
            </a>
            <div class="name">{name}</div>
            <span class="title">{title}</span>
            <span class="language">JavaScript
                {source_link}
            </span>
        </div>
        '''
    else:
        block = f'''
        <div class="{div_class}">
            <img src="./{ext[1:]}/{filename}" 
                alt="{alt}" 
                class="artImage">
            <div class="name">{name}</div>
            <span class="title">{title}</span>
            <span class="language">JavaScript
                {source_link}
            </span>
        </div>
        '''
    html_blocks.append(block)

# Save HTML
with open("ProceduralArt/output.html", "w") as f:
    f.write("\n".join(html_blocks))

print("\n✅ Done! Images downloaded to `png/` and `gif/`, and HTML saved to `output.html`.")
