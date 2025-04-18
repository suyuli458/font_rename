import os
from fontTools.ttLib import TTFont

INPUT_DIR = "input_fonts"
OUTPUT_DIR = "output_fonts"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def rename_font(file_path, output_path, new_name):
    font = TTFont(file_path)
    name_table = font['name']

    for record in name_table.names:
        if record.nameID in [1, 4, 6, 16, 17]:
            try:
                record.string = new_name.encode(record.getEncoding())
            except:
                record.string = new_name.encode('utf-16-be')  # fallback

    font.save(output_path)

for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith(".ttf"):
        font_path = os.path.join(INPUT_DIR, filename)
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(OUTPUT_DIR, base_name + "_mod.ttf")
        rename_font(font_path, output_path, base_name)
