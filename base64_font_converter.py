import base64

with open("font/Jost-Regular.ttf", "rb") as font_file:
    font_data = base64.b64encode(font_file.read()).decode('utf-8')

print(font_data)
# the converted base64 font can be set in the html.py file as BASE64_FONT value
