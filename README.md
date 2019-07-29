# GeetestV3
Crack Geetest V3

> GeetestV3 的  JS 破解

## 文件说明
```
├── decrypt.py Encrypyed 类
├── function.py 一些解密函数
├── geetest.py Geetest 类
├── geetrace.py 轨迹生成
├── Image 图片目录
│   ├── bg.jpg 带缺口图片
│   └── fullbg.jpg 完整图片
├── img_locate.py 图片偏移还原
├── __init__.py
├── README.md
├── slide.md
└── s.md
```

## 使用

```Python
import geetest

# gt, challenge 的值从目标网站自己寻找, 每个网站获取方式不一样
geetest = Geetest(gt, challenge)
# 获取validate
validate = geetest.crach()
```


## 输出
```bash
# Bilibili 测试
response: 
{'code': 0, 'data': {'redirectUrl': 'https://passport.biligame.com/crossDomain?DedeUserID=7073896&DedeUserID__ckMd5=9c5b8627a2617954&Expires=2592000&SESSDATA=9db05696%2C1566969564%2Ca69fa971&bili_jct=afcc548a9ca62a6fe992cf920b60086c&gourl=https%3A%2F%2Fwww.bilibili.com%2F'}}

# Slide Cutstom 测试
validate: 4d866a4968dc795b43c08c19601ae062
validate: 95e6d0b3327f1c60208cc07276571216
validate: 488ba2b18daa017ea905410a31028715
validate: 46d2ed3b8e7f89de11ee5c720252fc05
validate: 4acc9dbb6ba614266d15b2a515ad5d95
validate: c450af5a59d426ceecbdc25041489ddc
validate: 76adec005cb6d770509efa28348ae2bf
validate: 2fe30a1d15a84b2ca9cf7d91e1503cb0
validate: 9fef324c165c85db2e014059a2142b19
validate: e934302b84caf0d9f0913744922d51ab
```
