from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF

from pathlib import Path
from consts import * 
from tools import wrap_text

current_path = Path.cwd()

pdfs_files_path = current_path / "pdfs"
fonts_files_path = current_path / "fonts"
images_files_path = current_path / "images"

def wrap_text(text, font, max_width):
    lines = []
    words = text.split(' ')
    line = ''
    for word in words:
        test_line = line + word + ' '
        if font.getbbox(test_line)[2] <= max_width:
            line = test_line
        else:
            lines.append(line)
            line = word + ' '
    lines.append(line)
    return lines

def add_text_to_image(image, text, coordinates, 
                      font_path, font_size, color, 
                      max_width=2000, # Average width of the image
                      show=False):
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(str(font_path), font_size)
    wrapped_text = wrap_text(text, font, max_width)
    
    x, y = coordinates
    for line in wrapped_text:
        draw.text((x, y), line.strip(), font=font, fill=color)
        y += font.getbbox(line.strip())[3]  # Move to the next line

    if show:
        image.show()

if __name__ == "__main__":
    bootcamp_name = 'Python avanzado'
    full_name = 'Eduardo de Jesús Chapa Koloffon'
    date = "Aprobado el 19 de Septiembre de 2023."

    base_image_path = images_files_path / "background.jpg"
    with Image.open(base_image_path) as img:

        add_text_to_image(
            img,
            'Bootcamp de',
            BOOTCAMP_TITLE_COORDINATES,
            BOOTCAMP_FONT_PATH,
            BOOTCAMP_FONT_SIZE,
            WHITE
        )
        
        add_text_to_image(
            img,
            bootcamp_name, # We need to add a new life for the bootcamp name
            (BOOTCAMP_TITLE_COORDINATES[0], BOOTCAMP_TITLE_COORDINATES[1] + 200),
            BOOTCAMP_FONT_PATH,
            BOOTCAMP_FONT_SIZE,
            WHITE,
        )

        add_text_to_image(
            img,
            full_name,
            FULL_NAME_COORDINATES,
            FULLNAME_FONT_PATH,
            FULLNAME_FONT_SIZE,
            GREEN,
            max_width=MAX_FULLNAME_LENGTH
        )
        
        add_text_to_image(
            img,
            "Por su participación en un programa de 12 semanas de formación",
            DETAIL_COORDINATES,
            DETAIL_FONT_PATH,
            DETAIL_FONT_SIZE,
            WHITE,
        )

        add_text_to_image(
            img,
            "intensiva en el área de rails, con más de 50 horas de clases.",
            (DETAIL_COORDINATES[0], DETAIL_COORDINATES[1] + 60),
            DETAIL_FONT_PATH,
            DETAIL_FONT_SIZE,
            WHITE,
        )

        add_text_to_image(
            img,
            date,
            (DETAIL_COORDINATES[0], DETAIL_COORDINATES[1] + 180),
            DETAIL_FONT_PATH,
            DETAIL_FONT_SIZE,
            WHITE,
            show=True
        )
        