import math
import hashlib
import time
import random
import re

h = {
    "move": 0,
    "down": 1,
    "up": 2,
    "scroll": 3,
    "focus": 4,
    "blur": 5,
    "unload": 6,
    "unknown": 7
}


def cal_a(c, s, gt, challenge):
    tt = int(time.time() * 1000)
    ee = [
        ["move", 303, 418, 1563888260111, "pointermove"],
        ["move", 302, 419, 1563888260129, "pointermove"],
        ["move", 302, 418, 1563888260130, "mousemove"],
        ["move", 301, 419, 1563888260157, "pointermove"],
        ["move", 301, 418, 1563888260158, "mousemove"],
        ["move", 301, 419, 1563888260162, "pointermove"],
        ["move", 301, 419, 1563888260218, "pointermove"],
        ["move", 301, 419, 1563888260258, "pointermove"],
        ["move", 300, 419, 1563888260259, "mousemove"],
        ["move", 300, 419, 1563888260293, "pointermove"],
        ["move", 300, 420, 1563888260300, "pointermove"],
        ["move", 299, 420, 1563888260642, "pointermove"],
        ["move", 299, 421, 1563888260650, "pointermove"],
        ["move", 298, 421, 1563888260663, "pointermove"],
        ["move", 297, 421, 1563888260676, "pointermove"],
        ["move", 296, 423, 1563888260685, "pointermove"],
        ["move", 295, 423, 1563888260696, "pointermove"],
        ["move", 294, 425, 1563888260709, "pointermove"],
        ["move", 294, 424, 1563888260710, "mousemove"],
        ["move", 293, 427, 1563888260719, "pointermove"],
        ["move", 292, 427, 1563888260730, "pointermove"],
        ["move", 291, 430, 1563888260746, "pointermove"],
        ["move", 291, 431, 1563888260752, "pointermove"],
        ["move", 290, 432, 1563888260763, "pointermove"],
        ["move", 289, 434, 1563888260777, "pointermove"],
        ["move", 289, 435, 1563888260785, "pointermove"],
        ["move", 287, 440, 1563888260797, "pointermove"],
        ["move", 287, 440, 1563888260798, "mousemove"],
        ["move", 287, 441, 1563888260809, "pointermove"],
        ["move", 287, 441, 1563888260810, "mousemove"],
        ["move", 286, 443, 1563888260819, "pointermove"],
        ["move", 284, 449, 1563888260831, "pointermove"],
        ["move", 284, 448, 1563888260832, "mousemove"],
        ["move", 283, 450, 1563888260844, "pointermove"],
        ["move", 281, 453, 1563888260853, "pointermove"],
        ["move", 280, 453, 1563888260854, "mousemove"],
        ["move", 280, 454, 1563888260865, "pointermove"],
        ["move", 279, 455, 1563888260877, "pointermove"],
        ["move", 279, 455, 1563888260887, "pointermove"],
        ["down", 279, 455, 1563888261343, "pointerdown"],
        ["focus", 1563888261344],
        ["up", 279, 455, 1563888261450, "pointerup"],
    ]

    for i in range(len(ee)):
        if len(ee[i]) >= 3:
            ee[i][3] = tt
        else:
            ee[i][1] = tt
        tt += random.randint(2, 30)

    fp, lp, r_ = cal_n_help3(ee)
    n = cal_n(r_)
    r = "M(*((1((M(("
    o = "6322magic data7608magic dataCSS1Compatmagic data1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data2magic data3magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data1magic data-1magic data-1magic data-1magic data10magic data44magic data0magic data0magic data737magic data784magic data1687magic data888magic datazh-CNmagic datazh-CN,zhmagic data-1magic data1.5magic data24magic dataMozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36magic data1magic data1magic data1706magic data960magic data1707magic data960magic data1magic data1magic data1magic data-1magic dataLinux x86_64magic data0magic data-8magic data0a93728bbc5be4241e024b729f6c5e5dmagic data3f4cf59bdc7d0da206835d0e495e258amagic datainternal-pdf-viewer,mhjfbmdgcfjbbpaeojofohoefgiehjaimagic data0magic data-1magic data0magic data8magic dataArial,BitstreamVeraSansMono,Courier,CourierNew,Helvetica,Monaco,Times,TimesNewRoman,Wingdings,Wingdings2,Wingdings3magic data1563801637024magic data-1,-1,9,4,11,0,17,0,50,2,10,10,30,95,95,98,99,99,99,-1magic data-1magic data-1magic data12magic data-1magic data-1magic data-1magic data5magic datafalsemagic datafalse"
    t_1233 = "6322!!7608!!CSS1Compat!!1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!2!!3!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!1!!-1!!-1!!-1!!10!!44!!0!!0!!737!!784!!1687!!888!!zh-CN!!zh-CN,zh!!-1!!1.5!!24!!Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36!!1!!1!!1706!!960!!1707!!960!!1!!1!!1!!-1!!Linux x86_64!!0!!-8!!0a93728bbc5be4241e024b729f6c5e5d!!3f4cf59bdc7d0da206835d0e495e258a!!internal-pdf-viewer,mhjfbmdgcfjbbpaeojofohoefgiehjai!!0!!-1!!0!!8!!Arial,BitstreamVeraSansMono,Courier,CourierNew,Helvetica,Monaco,Times,TimesNewRoman,Wingdings,Wingdings2,Wingdings3!!1563801637024!!-1,-1,9,4,11,0,17,0,50,2,10,10,30,95,95,98,99,99,99,-1!!-1!!-1!!12!!-1!!-1!!-1!!5!!false!!false"
    tt = str(time.time() * 1000)
    o = re.sub(r'data\d{4}\d+magic', 'data' + tt + 'magic', o)
    t_1233 = re.sub(r'\d{8}\d+', tt, t_1233)
    a = {
        "lang": 'zh-cn',
        "type": 'fullpage',
        "tt": cal_tt(n, c, s),
        "light": "SPAN_0",
        "s": hash_(bytes_to_string(help_(r))),
        "h": hash_(bytes_to_string(help_(o))),
        "hh": hash_(o),
        "hi": hash_(t_1233),
        "ep": cal_ep(fp, lp, gt, challenge),
        "captcha_token": 'bboy',
        "passtime": random.randint(100, 300)
    }
    a['rp'] = hash_(gt + challenge + str(a['passtime']))
    return a


def cal_tt(t, e, n):
    if not t or not n:
        return e
    i = 0
    o = t
    s = e[0]
    a = e[2]
    u = e[4]
    r = n[i:i + 2]
    while r:
        i += 2
        c = int(r, 16)
        _ = chr(c)
        l = (s * c * c + a * c + u) % len(t)
        o = o[:l] + _ + o[l:]
        r = n[i:i + 2]
    return o


def hash_(e):
    md5 = hashlib.md5()
    md5.update(bytes(e, 'utf8'))
    return md5.hexdigest()


def cal_ep(fp, lp, gt, challenge):
    AC = [
        -119.75575256347656,
        -119.63088989257812,
        -119.25106811523438,
        -118.62662506103516,
        -117.77042388916016,
        -116.68677520751953,
        -115.37254333496094,
        -113.86859893798828,
        -112.13563537597656,
        -110.18766784667969,
        -108.01028442382812,
        -105.57905578613281,
        -102.86422729492188,
        -99.82667541503906,
        -96.42578125,
        -92.65921783447266,
        -88.80050659179688,
        -88.23417663574219,
        -63.43762969970703,
        -38.98215866088867,
        -30.18212127685547,
        -30.771005630493164,
        -41.033077239990234,
        -69.45748138427734,
        -87.49734497070312,
        -89.3124771118164,
        -93.22586059570312,
        -96.97767639160156,
        -100.37113189697266,
        -103.42404174804688,
        -106.18102264404297,
        -108.68859100341797,
    ]

    a = int(time.time() * 1000)
    f = a + random.randint(2, 8)
    b = a + random.randint(50, 80)
    l = a + random.randint(3, 9)
    m = l + random.randint(30, 50)
    n = m + random.randint(1, 5)
    o = n + random.randint(10, 50)
    p = o + random.randint(70, 90)
    r = p + random.randint(10, 100)
    s = r + random.randint(1, 2)
    tm = {
        'a': a,
        'b': b,
        'c': b,
        'd': 0,
        'e': 0,
        'f': f,
        'g': f,
        'h': f,
        'i': f,
        'j': f,
        'k': 0,
        'l': l,
        'm': m,
        'n': n,
        'o': o,
        'p': p,
        'q': p,
        'r': int(time.time() * 1000),
        's': s,
        't': s,
        'u': s
    }
    e = {"ts": int(time.time() * 1000), 'v': '8.7.9'}
    e['ip'] = "192.168.1.104,218.249.50.58"
    e['f'] = hash_(gt + challenge)
    e['de'] = False
    e['te'] = False
    e['me'] = True
    e['ven'] = "Intel Open Source Technology Center"
    e['ren'] = "Mesa DRI Intel(R) UHD Graphics 620 (Kabylake GT2) "
    e['ac'] = hash_(''.join([str(i) for i in AC]))
    e['pu'] = False
    e['ph'] = False
    e['ni'] = False
    e['se'] = False
    e['fp'] = fp
    e['lp'] = lp
    e['em'] = {
        'cp': 0,
        'ek': "11",
        'nt': 0,
        'ph': 0,
        'sc': 0,
        'si': 0,
        'wd': 0,
    }
    e['tm'] = tm
    e['by'] = 0
    return e


def cal_n_help1(e):
    t = ''
    n = 0
    while not t and e[n]:
        t = e[n][4]
        n += 1
    if not t:
        return e
    r = ''
    o = ["mouse", "touch", "pointer", "MSPointer"]
    for i in o:
        if not t.find(i):
            r = i
    s = e[:]
    size = len(s)
    a = ["move", "down", "up"]
    for c in range(size - 1, -1, -1):
        u = s[c]
        _ = u[0]
        if _ in a:
            if len(u) >= 5 and u[4].find(r):
                s.pop(c)
    return s


def cal_n_help2(e):
    t = 32767
    if t < e:
        e = t
    elif e < -t:
        e = -t
    return int(round(e))


def cal_n_help3(e):
    t = n = i = 0
    r = []
    a = s = None
    c = cal_n_help1(e)
    u = len(c)
    o = ["down", "move", "up", "scroll"]
    o_ = ['blur', 'focus', 'unload']
    _ = 0 if u < 300 else u - 300
    for idx in range(_, u):
        l = c[idx]
        h = l[0]
        if h in o:
            a = l if not a else a
            s = l
            i = l[3] - i if i else i
            r.append([h, [l[1] - t, l[2] - n], cal_n_help2(i)])
            t = l[1]
            n = l[2]
            i = l[3]
        elif h in o_:
            i = l[1] - i if i else i
            r.append([h, cal_n_help2(i)])
            i = l[1]
    return a, s, r


def cal_n_fun_d(e):
    t = []
    n = len(e)
    r = 0
    while r < n:
        o = e[r]
        i = 0
        while True:
            if i >= 16:
                break
            a = r + i + 1
            if a >= n:
                break
            if e[a] != o:
                break
            i += 1
        r = r + 1 + i
        s = h[o]
        if i:
            t.append(8 | s)
            t.append(i - 1)
        else:
            t.append(s)
    c = bin(32768 | n).lstrip('0b').zfill(16)
    u = ''
    for _ in range(len(t)):
        u += bin(t[_]).lstrip('0b').zfill(4)
    return c + u


def cal_n_fun_p(e, flag):
    t = 32767
    n = []
    for i in e:
        if i > t:
            i = t
        elif i < -t:
            i = -t
        n.append(i)
    e = n
    n = len(e)
    r = 0
    o = []
    while r < n:
        i = 1
        a = e[r]
        s = abs(a)
        while True:
            if n <= r + i:
                break
            if e[r + i] != a:
                break
            if s >= 127 or i >= 127:
                break
            i += 1
        if i > 1:
            o.append((49152 if a < 0 else 32768) | i << 7 | s)
        else:
            o.append(a)
        r += i
    e = o
    r = []
    o = []
    for i in e:
        if i:
            t = math.ceil(math.log(abs(i) + 1) / math.log(16))
        else:
            t = 0
        if not t:
            t = 1
        r.append(bin(t - 1).lstrip('0b').zfill(2))
        o.append(bin(abs(i)).lstrip('0b').zfill(4 * t))
    i = "".join(r)
    a = "".join(o)
    if not flag:
        return bin(32768 | len(e)).lstrip('0b').zfill(16) + i + a + ''
    else:
        n = []
        tmp = []
        for idx in e:
            if idx and idx >> 15 != 1:
                tmp.append(idx)
        for idx in tmp:
            n.append('1' if idx < 0 else '0')
        n = ''.join(n)
        return bin(32768 | len(e)).lstrip('0b').zfill(16) + i + a + n
    return None


def cal_n(e):
    t = []
    n = []
    o = []
    r = []
    for i in range(len(e)):
        s = e[i]
        c = len(s)
        t.append(s[0])
        if c == 2:
            n.append(s[1])
        else:
            n.append(s[2])
        if c == 3:
            r.append(s[1][0])
            o.append(s[1][1])
    u = cal_n_fun_d(t) + cal_n_fun_p(n, False) \
        + cal_n_fun_p(r, True) + cal_n_fun_p(o, True)
    _ = len(u)
    if _ % 6:
        u += bin(0).lstrip('0b').zfill(6 - _ % 6)
    s = "()*,-./0123456789:?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz~"
    t = ''
    n = len(u) / 6
    r = 0
    while r < n:
        t += s[int(u[6 * r:6 * (r + 1)], 2)]
        r += 1
    return t

def help_(e):
    return [ord(n) for n in e]

def bytes_to_string(array):
    i = {
        'JDN': ".",
        'JEi': 7274496,
        'JFj': 9483264,
        'JGF': 19220,
        'JHv': 235,
        'JIP': 24
    }

    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()"

    def o(t):
        if t < 0 or t >= len(s):
            return '.'
        else:
            return s[t]

    def e(t, e):
        n = 0
        for r in range(i['JIP'], -1, -1):
            if 1 == (e >> r & 1):
                n = (n << 1) + (t >> r & 1)
        return n

    n = r = ''
    for a in range(0, len(array), 3):
        if a + 2 < len(array):
            u = (array[a] << 16) + (array[a + 1] << 8) + array[a + 2]
            n += o(e(u, i['JEi'])) + o(e(u, i['JFj'])) + o(e(u, i['JGF'])) + o(
                e(u, i['JHv']))
        else:
            c = len(array) % 3
            if c == 2:
                u = (array[a] << 16) + (array[a + 1] << 8)
                n += o(e(u, i['JEi'])) + o(e(u, i['JFj'])) + o(e(u, i['JGF']))
                r = i['JDN']
            elif 1 == c:
                u = array[a] << 16
                n += o(e(u, i['JEi'])) + o(e(u, i['JFj']))
                r = i['JDN'] + i['JDN']
    return n + r
