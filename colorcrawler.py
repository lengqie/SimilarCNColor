from requests_html import HTMLSession
import json

session = HTMLSession()

url = "http://www.2kil.com/"
response = session.get(url)
response.html.render()


def FormatRgb(_hex: str) -> str:
    return str(int(_hex,16))


Colors = []
for i in range(1, 321):
    css = "#colors > div > div > div:nth-child(" + str(i) + ")"
    r = response.html.find(css, first=True).text.split("\n")

    rgb = r[5][1:]
    rgb = "" + FormatRgb(rgb[:2]) + "/" + FormatRgb(rgb[2:4]) + "/" + FormatRgb(rgb[4:])
    cmyk = "" + r[1][:-2] + r[2][:-3] + r[3][:-3] + r[4][:-4]

    temp = {
        "name": r[0],
        "rgb": rgb,
        "cmyk": cmyk,
        "hex": r[5]
    }

    Colors.append(temp)

# print(Colors[0])
with open("color.json", "w", encoding='utf-8') as file:
    json.dump(Colors, file, ensure_ascii=False)

print("OK----------------------")
