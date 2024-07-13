def wrap_text(text, font, max_width):
    lines = []
    words = text.split()
    line = ''
    for word in words:
        test_line = line + word + ' '
        if font.getsize(test_line)[0] <= max_width:
            line = test_line
        else:
            lines.append(line)
            line = word + ' '
    lines.append(line)
    return lines
