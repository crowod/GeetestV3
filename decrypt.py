import binascii, json, os
import time
import random
import hashlib
import rsa

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

class Encrypyed():
    def __init__(self):
        self.modulus = "00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81"
        self.pub_key = '10001'

    def encrypted_request(self, initData, c, aa, passtime):
        # md5 加密
        hash = hashlib.md5()
        hash.update(bytes(initData['gt'], encoding='utf-8'))
        hash.update(bytes(initData['challenge'][0:32], encoding='utf-8'))
        hash.update(bytes(str(passtime), encoding='utf-8'))
        text = {
            "lang": "zh-cn",
            "userresponse": self.cal_userresonse(c,
                                                 initData['challenge']),
            "passtime": passtime,
            "imgload": random.randint(100, 800),
            "aa": aa,
            "ep": self.get_ep(initData['gt'], initData['challenge']),
            'rp': hash.hexdigest()
        }
        text = json.dumps(text, separators=(',', ':'))
        sec_key = self.create_secret_key(8)
        # rsa 不对称性对 aes的密钥进行加密
        enc_sec_key = self.rsa_encrpt(sec_key, self.pub_key, self.modulus)

        # aes 对称加密  进行轨迹加密
        iv = b"0000000000000000"
        enc_text = self.aes_encrypt(text, sec_key.decode('utf-8'), iv)
        array = []
        for byte in enc_text:
            array.append(byte)

        enc_text = self.bytes_to_string(array)
        # print(enc_text)
        w = enc_text + enc_sec_key,
            # 'callback': 'geetest_' + str(int(time.time() * 1000)),
        return w

    def aes_encrypt(self, text, secKey, iv, style='pkcs7'):
        """
        :param text: 文本
        :param secKey: 密钥
        :param iv: 初始iv  bytes
        :param style: 返回函数类型
        :return:
        """
        encryptor = AES.new(secKey.encode('utf-8'), AES.MODE_CBC, iv)
        pad_pkcs7 = pad(text.encode('utf-8'), AES.block_size, style=style)
        ciphertext = encryptor.encrypt(pad_pkcs7)
        return ciphertext

    def rsa_encrpt(self, text, pubKey, modulus):
        '''
        对text 进行rsa加密   # reverseText^pubKey%modulus
        '''
        PublicKey = rsa.PublicKey(int(modulus, 16), int(pubKey,
                                                        16))  # rsa库公钥形式
        rs = rsa.encrypt(text, PublicKey)
        return rs.hex()

    def create_secret_key(self, size):
        # 作用是返回的二进制数据的十六进制表示。每一个字节的数据转换成相应的2位十六进制表示
        return binascii.hexlify(os.urandom(size))

    def bytes_to_string(self, array):
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
                n += o(e(u, i['JEi'])) + o(e(u, i['JFj'])) + o(e(
                    u, i['JGF'])) + o(e(u, i['JHv']))
            else:
                c = len(array) % 3
                if c == 2:
                    u = (array[a] << 16) + (array[a + 1] << 8)
                    n += o(e(u, i['JEi'])) + o(e(u, i['JFj'])) + o(
                        e(u, i['JGF']))
                    r = i['JDN']
                elif 1 == c:
                    u = array[a] << 16
                    n += o(e(u, i['JEi'])) + o(e(u, i['JFj']))
                    r = i['JDN'] + i['JDN']
        return n + r

    def cal_userresonse(self, value, challenge):
        n = challenge[32:]
        r = []
        for i in n:
            o = ord(i)
            r.append(o - 87 if 57 < o else o - 48)
        n = 36 * r[0] + r[1]
        a = int(round(value)) + n
        u = [[], [], [], [], []]
        c = {}
        _ = 0

        challenge = challenge[:32]
        l = len(challenge)
        for i in range(l):
            if challenge[i] in c:
                pass
            else:
                c[challenge[i]] = 1
                u[_].append(challenge[i])
                _ += 1
                _ = 0 if _ == 5 else _
        h = a
        d = 4
        p = ''
        g = [1, 2, 5, 10, 50]
        while h > 0:
            if h - g[d] >= 0:
                f = int(random.random() * len(u[d]))
                p += u[d][f]
                h -= g[d]
            else:
                u.pop(d)
                g.pop(d)
                d -= 1
        return p

    def get_ep(self, gt, challenge):
        md5 = hashlib.md5()
        md5.update(bytes(gt + challenge, encoding='utf-8'))
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
        return {
            "v": '7.6.0',
            "f": md5.hexdigest(),
            "me": True,
            "te": False,
            "tm": tm
        }

    def fun_t(self, t):
        i = []
        o = 0
        for s in range(len(t) - 1):
            e = int(round(t[s + 1][0] - t[s][0]))
            n = int(round(t[s + 1][1] - t[s][1]))
            r = int(round(t[s + 1][2] - t[s][2]))
            if e or n or r:
                if not e and not n:
                    o += r
                else:
                    i.append([e, n, r + o])
                    o = 0
        if o:
            i.append([e, n, o])

        return i

    def fun_e(self, t):
        e = [[1, 0], [2, 0], [1, -1], [1, 1], [0, 1], [0, -1], [3, 0], [2, -1],
             [2, 1]]
        s = "stuvwxyz~"
        for n in range(len(e)):
            if t[0] == e[n][0] and t[1] == e[n][1]:
                return s[n]
        return 0

    def fun_n(self, t):
        e = "()*,-./0123456789:?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqr"
        n = len(e)
        r = ""
        i = abs(t)
        o = int(i / n)

        if o >= n:
            o = n - 1
        if o:
            r = e[o]
        s = ''
        if t < 0:
            s += '!'
        if r:
            s += '$'
        return s + r + e[i % n]

    def fun_f(self, t):
        r = []
        i = []
        o = []

        track_list = self.fun_t(t)
        for t in track_list:
            e = self.fun_e(t)
            if e:
                i.append(e)
            else:
                r.append(self.fun_n(t[0]))
                i.append(self.fun_n(t[1]))
            o.append(self.fun_n(t[2]))
        return "".join(r) + '!!' + "".join(i) + '!!' + "".join(o)

    def cal_aa(self, t, e, n):
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