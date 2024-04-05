import imgkit
import html
from GuildMember import GuildMember
from datetime import date

GUILD_MEMBER = GuildMember(user_id=123,
                           name='Error404 | Manuel',
                           level=56,
                           points=12345,
                           last_activity=date.today(),
                           msg_counter=6034,
                           vc_time=7513,
                           birthday='12.04.1985',
                           battle_tag='Error#0815',
                           steam_code='34090784')

if __name__ == '__main__':
    # Speichern des HTML-Inhalts in einer Datei
    with open("output.html", "w") as html_file:
        dynamic_html = html.create_dynamic_html(guild_member=GUILD_MEMBER)
        html_file.write(dynamic_html)

    options = {
        'format': 'png',
        'width': html.IMAGE_WIDTH,
        'height': html.IMAGE_HEIGHT
    }

    # Konvertieren des HTMLs in ein PNG-Bild
    imgkit.from_file(filename="output.html", output_path="output.png", options=options)

    print("PNG-Bild wurde erstellt.")
