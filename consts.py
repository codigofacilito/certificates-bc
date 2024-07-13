from pathlib import Path

current_path = Path.cwd()

FULL_NAME_COORDINATES = (160, 1300)
BOOTCAMP_TITLE_COORDINATES = (160, 500)

FOOTER_COORDINATES = (160, 1900)
FOOTER_FONT_SIZE = 50
FOOTER_FONT_PATH = current_path / "fonts" / "plex" / "IBMPlexSans-Regular.ttf"
# ------------ FONTS ------------

FULLNAME_FONT_SIZE = 150
FULLNAME_FONT_PATH = current_path / "fonts" / "playwrite" / "PlaywriteHU-VariableFont_wght.ttf"
MAX_FULLNAME_LENGTH = 1800 # MAX LENGTH OF THE FULL NAME <------------ !IMPORTANT TO TRUNCATE THE TEXT

BOOTCAMP_FONT_SIZE = 180
BOOTCAMP_FONT_PATH = current_path / "fonts" / "plex" / "IBMPlexSans-Bold.ttf"

# ------------ COLORS ------------

WHITE = (255, 255, 255)
GREEN = (42, 186, 159)

