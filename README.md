<div align=center>
<img src="https://raw.githubusercontent.com/lengqie/SimilarCNColor/master/static/scc.jpg"/>
</div>
<div align=center>
<img src="https://img.shields.io/badge/Python-3.8-blue"/>
</div>


## 1. 基本介绍

### 1.1 简介
SimilarCNColor：🌈 相似的华夏色

一个Python实现的找到最相似颜色名的脚本。（比如 口红色号）

### 1.2 功能

- [x]   基本功能
- [x]   多种输入
- [x]   屏幕获取
- [ ]   添加颜色
- [ ]   UI
- [ ]   ...

## 2. 使用

### 2.1 数据获取（可跳过）
数据来源： http://www.2kil.com

保存的Json格式：
~~~json
[
   {
    "name": "粉鳳仙",
    "rgb": "234/192/206",
    "cmyk": "0/118/12/8",
    "hex": "#EAC0CE"
  },
  ...
]
~~~

已经存在的颜色 https://github.com/lengqie/SimilarCNColor/blob/master/color.json


### 2.2 颜色识别
~~~shell
python main.py
~~~
输入rgb 示例：`111,111,111`

输入cmyk 示例：`100,10,100,10`

输入rgb 示例：`#2b2b2b`

### 2.3 屏幕获取
~~~shell
python screen_put.py
~~~


## 3 添加颜色
~~~shell
python main.py
~~~

## 4. 协议

Licensed under the *MIT* license
