import imgkit
import html

# Speichern des HTML-Inhalts in einer Datei
with open("output.html", "w") as html_file:
    html_file.write(html.CONTENT)

options = {
    'format': 'png',
    'width': html.IMAGE_WIDTH,
    'height': html.IMAGE_HEIGHT
}

# Konvertieren des HTMLs in ein PNG-Bild
imgkit.from_file(filename="output.html", output_path="output.png", options=options)

print("PNG-Bild wurde erstellt.")
