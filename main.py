import json
from enum import Enum


class InType(Enum):
    RGB = "rgb"
    CMYK = "cmyk"
    HEX = "hex"


res = []
in_color = ""
in_type = InType.RGB


def InFilter(input_: str):
    global in_type
    global in_color
    if "," in input_ and len(input_.split(",")) == 3:
        in_type = InType.RGB
        in_color = input_.split(",")
        for i in in_color:
            if not i.isdigit():
                raise Exception("unfair input")
        in_color = [int(i) for i in in_color]

    elif "," in input_ and len(input_.split(",")) == 4:
        in_type = InType.CMYK
        in_color = input_.split(",")

        for i in in_color:
            if not i.isdigit():
                raise Exception("unfair input")
        in_color = [int(i) for i in in_color]

    elif input_.startswith("#"):
        in_type = InType.HEX
        if len(input_) != 7:
            raise Exception("unfair input")
        in_color = input_[1:]
        # hex -> rgb
        in_color = [int(in_color[i:i + 2], 16) for i in range(0, len(in_color), 2)]
        # print(in_color)

    else:
        raise Exception("unfair input")


def GetColor(in_type_: InType):
    code = ""
    rng = 0

    with open("color.json", "r", encoding='utf-8') as file:
        Color = json.load(file)

    for i in Color:
        if in_type_ == InType.RGB:
            code = "rgb"
            rng = 3
        elif in_type_ == InType.CMYK:
            code = "cmyk"
            rng = 4
        elif in_type_ == InType.HEX:
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

    res.sort(key=DictSort)


def DictSort(ele: dict) -> int:
    return ele["val"]


def Head(li: list, nb: int = 5):
    for i in range(nb):
        li[i]["url"] = "https://encycolorpedia.cn/" + (li[i]["key"]["hex"][1:]).lower()
        print(li[i])


if __name__ == '__main__':
    in_color = input("please input the RGX or CMYk or HEX：")
    InFilter(in_color)
    GetColor(in_type)
    Head(res, 5)
