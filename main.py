import json

in_color = input("please input the RGX or CMYk：")
in_color = in_color.split(",")
in_color = [int(i) for i in in_color]

cmyk = False
res = []

if len(in_color) == 4:
    cmyk = True


def GetColor(is_cmyk: bool):
    with open("color.json", "r", encoding='utf-8') as file:
        Color = json.load(file)

    for i in Color:
        if is_cmyk:
            code = "cmyk"
            rng = 4
        else:
            code = "rgb"
            rng = 3
        code = i[code].split("/")
        t = 0
        for j in range(rng):
            t = (t + ((int(in_color[j]) - int(code[j])) ** 2) ** 0.5)
        res.append(
            {
                "key": i,
                "val": t
            }
        )


def DictSort(ele: dict) -> int:
    return ele["val"]


def Head(li: list, nb: int = 5):
    for i in range(nb):
        li[i]["url"] = "https://encycolorpedia.cn/" + (li[i]["key"]["hex"][1:]).lower()
        print(li[i])


if __name__ == '__main__':
    GetColor(cmyk)
    res.sort(key=DictSort)
    Head(res, 5)
