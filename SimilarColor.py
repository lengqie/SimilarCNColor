import json

in_color = input("please input the RGX：")
in_rgb = in_color.split(",")
in_rgb = [int(i) for i in in_rgb]

with open("color.json", "r", encoding='utf-8') as file:
    Color = json.load(file)

res = []
for i in Color:
    rgb = i["rgb"].split("/")
    t = 0
    for j in range(3):
        t = (t + ((int(in_rgb[j]) - int(rgb[j])) ** 2) ** 0.5)
    res.append(
        {
            "key": i,
            "val": t
        }
    )


def DictSort(ele: dict) -> int:
    return ele["val"]


res.sort(key=DictSort)


def Head(li: list, nb: int = 5):
    for i in range(nb):
        li[i]["url"] = "https://encycolorpedia.cn/" + (li[i]["key"]["hex"][1:]).lower()
        print(li[i])


Head(res)
