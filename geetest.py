import re
import random
import time
import json
import os

import requests
import traceback

import function
from decrypt import Encrypyed
from img_locate import ImgProcess
from geetrace import *


class Geetest:
    def __init__(self, gt, challenge):
        self.gt = gt
        self.challenge = challenge
        self.s = ''
        self.c = [12, 58, 98, 36, 43, 95, 62, 15, 12]
        self.encrypyed = Encrypyed()
        self.sec_key = self.encrypyed.create_secret_key(8)
        self.session = requests.Session()

    def get_php(self):
        # if self.__step1() and self.__step2() and self.__step3():
        if self.__step1() and self.__step2():
            headers = {
                'Referer':
                'https://www.geetest.com/demo/slide-custom.html',
                'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            }
            params = (
                ('is_next', 'true'),
                ('type', 'slide3'),
                ('gt', self.gt),
                ('challenge', self.challenge),
                ('lang', 'zh-cn'),
                ('https', 'true'),
                ('protocol', 'https://'),
                ('offline', 'false'),
                ('product', 'custom'),
                ('api_server', 'api.geetest.com'),
                ('isPC', 'true'),
                ('area', '#area'),
                ('bg_color', 'gray'),
                ('width', '278px'),
                ('callback', 'geetest_' + str(int(time.time()) * 1000)),
            )
            response = self.session.get('https://api.geetest.com/get.php',
                                        params=params)
            try:
                result = json.loads(
                    re.search(
                        r'\((\{.*?\})\)',
                        response.content.decode('unicode_escape')).group(1))
                self.s = result['s']
                self.c = result['c']
                self.challenge = result['challenge']
                self.fullbg = 'https://static.geetest.com/' + result['fullbg']
                self.bg = 'https://static.geetest.com/' + result['bg']
            except Exception:
                traceback.print_exc()

    def __step1(self):

        headers = {
            'Referer':
            'https://www.geetest.com/demo/slide-custom.html',
            'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        }

        self.session.headers = headers

        text = """{"gt":"019924a82c70bb123aae90d483087f94","challenge":"03b132d32982a6c8ddebf90ab7f29e42","offline":false,"new_captcha":true,"product":"custom","width":"300px","next_width":"278px","area":"#area","bg_color":"gray","https":true,"protocol":"https://","click":"/static/js/click.2.8.1.js","slide":"/static/js/slide.7.6.0.js","pencil":"/static/js/pencil.1.0.3.js","fullpage":"/static/js/fullpage.8.7.9.js","beeline":"/static/js/beeline.1.0.1.js","aspect_radio":{"beeline":50,"click":128,"slide":103,"voice":128,"pencil":128},"static_servers":["static.geetest.com/","dn-staticdown.qbox.me/"],"type":"fullpage","maze":"/static/js/maze.1.0.1.js","geetest":"/static/js/geetest.6.0.9.js","voice":"/static/js/voice.1.2.0.js","cc":8,"ww":true,"i":"6322!!7608!!CSS1Compat!!1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!2!!3!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!1!!-1!!-1!!-1!!10!!44!!0!!0!!737!!784!!1687!!888!!zh-CN!!zh-CN,zh!!-1!!1.5!!24!!Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36!!1!!1!!1706!!960!!1707!!960!!1!!1!!1!!-1!!Linux x86_64!!0!!-8!!0a93728bbc5be4241e024b729f6c5e5d!!3f4cf59bdc7d0da206835d0e495e258a!!internal-pdf-viewer,mhjfbmdgcfjbbpaeojofohoefgiehjai!!0!!-1!!0!!8!!Arial,BitstreamVeraSansMono,Courier,CourierNew,Helvetica,Monaco,Times,TimesNewRoman,Wingdings,Wingdings2,Wingdings3!!1563788965804!!-1,-1,2,1,2,0,15,0,49,1,4,4,10,70,71,73,74,74,74,-1!!-1!!-1!!12!!-1!!-1!!-1!!5!!false!!false"}"""
        text = json.loads(text)
        text['gt'] = self.gt
        text['challenge'] = self.challenge
        w = self.cal_w(text)

        params = (
            ('gt', self.gt),
            ('challenge', self.challenge),
            ('lang', 'zh-cn'),
            ('pt', '0'),
            ('w', w),
            ('callback', 'geetest_' + str(int(time.time() * 1000))),
        )

        response = self.session.get('https://api.geetest.com/get.php',
                                    params=params)
        try:
            result = json.loads(
                re.search(r'\((\{.*?\})\)',
                          response.content.decode('unicode_escape')).group(1))
            self.c = result['data']['c']
            self.s = result['data']['s']
            return True
        except Exception:
            traceback.print_exc()
            return False

    def __step2(self):

        headers = {
            'Referer':
            'https://www.geetest.com/demo/slide-custom.html',
            'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        }
        self.session.headers = headers
        w = self.cal_w(function.cal_a(self.c, self.s, self.gt, self.challenge),
                       flag=1)
        params = (
            ('gt', self.gt),
            ('challenge', self.challenge),
            ('lang', 'zh-cn'),
            ('pt', '0'),
            ('w', w),
            ('callback', 'geetest_' + str(int(time.time() * 1000))),
        )
        try:
            response = self.session.get('https://api.geetest.com/ajax.php',
                                        params=params)
            result = json.loads(
                re.search(r'\((\{.*?\})\)',
                          response.content.decode('unicode_escape')).group(1))
            if 'data' in result:
                return True
        except Exception:
            traceback.print_exc()
            return False

    def cal_w(self, text, flag=0):
        enc_sec_key = ''
        if not flag:
            # rsa 不对称性对 aes的密钥进行加密
            enc_sec_key = self.encrypyed.rsa_encrpt(self.sec_key,
                                                    self.encrypyed.pub_key,
                                                    self.encrypyed.modulus)
        text = json.dumps(text, separators=(',', ':'))

        # aes 对称加密  进行轨迹加密
        iv = b"0000000000000000"
        enc_text = self.encrypyed.aes_encrypt(text,
                                              self.sec_key.decode('utf-8'), iv)
        array = []
        for byte in enc_text:
            array.append(byte)

        enc_text = self.encrypyed.bytes_to_string(array)
        return enc_text + enc_sec_key

    def crack(self):
        self.get_php()
        if not os.path.exists('Image'):
            os.mkdir('Image')

        headers = {
            'authority': 'static.geetest.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'if-none-match': '"8AF6F73553C6560DFD16F88CC8B6384A"',
            'if-modified-since': 'Thu, 22 Nov 2018 02:49:57 GMT',
        }
        self.session.headers = headers
        with open("Image/fullbg.jpg", "wb") as f:
            content = self.session.get(self.fullbg, timeout=0.5).content
            f.write(content)
        with open("Image/bg.jpg", "wb") as f:
            content = self.session.get(self.bg, timeout=0.5).content
            f.write(content)

        img_process = ImgProcess()
        img1 = img_process.get_merge_image('Image/fullbg.jpg')
        img2 = img_process.get_merge_image('Image/bg.jpg')
        distance = int(img_process.get_gap(img1, img2) - 7)
        trace = get_trace(distance)
        r1 = 230.65741262170448
        s = 1.0000401423527645
        c = int((trace[-1][0] + r1) / s - r1)
        initData = {'gt': self.gt, 'challenge': self.challenge}
        passtime = trace[-1][-1]
        aa = self.encrypyed.cal_aa(self.encrypyed.fun_f(trace), self.c, self.s)
        w = self.encrypyed.encrypted_request(initData, c, aa, passtime)
        headers = {
            'Referer':
            'https://www.geetest.com/demo/slide-custom.html',
            'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        }
        self.session.headers = headers
        params = (
            ('gt', self.gt),
            ('challenge', self.challenge),
            ('lang', 'zh-cn'),
            ('pt', '0'),
            ('w', w),
            ('callback', 'geetest_' + str(int(time.time() * 1000))),
        )
        response = self.session.get('https://api.geetest.com/ajax.php',
                                    params=params)
        try:
            result = json.loads(
                re.search(r'\((\{.*?\})\)',
                          response.content.decode('unicode_escape')).group(1))
            if 'validate' not in result:
                return None
            return result['validate']
        except Exception:
            traceback.print_exc()


if __name__ == "__main__":
    pass
    # Bilibili 测试

    #     cookies = {
    #         '$buvid3': 'D0F91575-9711-4DC6-945D-DFD886AA537749002infoc',
    #         'LIVE_BUVID': 'AUTO7215531554553297',
    #         'sid': 'cgv8n65s',
    #         'stardustvideo': '1',
    #         'CURRENT_FNVAL': '16',
    #         'UM_distinctid':
    #         '169c65cf49d281-0e535f0b9944e3-1a201708-18fd80-169c65cf49e738',
    #         'fts': '1554816673',
    #         'rpdid': '|(JY~JY)lJm~0J\'ullY|km~J|',
    #         'CURRENT_QUALITY': '32',
    #         '_uuid': '18193D65-6A6F-3C60-A39E-C5122D7E224164098infoc',
    #         'bp_t_offset_7073896': '278276587580201855',
    #         'JSESSIONID': '2E62623AC26241F9F92EC8E255538B2F',
    #     }

    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    #         'User-Agent':
    #         'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    #         'Accept': 'application/json, text/plain, */*',
    #         'Referer': 'https://passport.bilibili.com/login',
    #         'Connection': 'keep-alive',
    #     }

    #     params = (('plat', '11'), )

    #     response = requests.get(
    #         'https://passport.bilibili.com/web/captcha/combine',
    #         headers=headers,
    #         params=params,
    #         cookies=cookies)
    #     result = response.json()['data']['result']
    #     geetest = Geetest(result['gt'], result['challenge'])
    #     key = result['key']
    #     validate = geetest.crack()
    #     cookies = {
    #         '$buvid3': 'D0F91575-9711-4DC6-945D-DFD886AA537749002infoc',
    #         'LIVE_BUVID': 'AUTO7215531554553297',
    #         'sid': 'cgv8n65s',
    #         'stardustvideo': '1',
    #         'CURRENT_FNVAL': '16',
    #         'UM_distinctid':
    #         '169c65cf49d281-0e535f0b9944e3-1a201708-18fd80-169c65cf49e738',
    #         'fts': '1554816673',
    #         'rpdid': '|(JY~JY)lJm~0J\'ullY|km~J|',
    #         'CURRENT_QUALITY': '32',
    #         '_uuid': '18193D65-6A6F-3C60-A39E-C5122D7E224164098infoc',
    #         'bp_t_offset_7073896': '278276587580201855',
    #         'JSESSIONID': '2E62623AC26241F9F92EC8E255538B2F',
    #     }

    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    #         'User-Agent':
    #         'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    #         'Accept': '*/*',
    #         'Referer': 'https://passport.bilibili.com/login',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Connection': 'keep-alive',
    #     }

    #     params = (
    #         ('act', 'getkey'),
    #         ('r', random.random()),
    #     )

    #     response = requests.get('https://passport.bilibili.com/login',
    #                             headers=headers,
    #                             params=params,
    #                             cookies=cookies)

    #     result = response.json()
    #     import base64
    #     from Crypto.PublicKey import RSA
    #     from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
    #     password = ''
    #     message = result['hash'] + password
    #     rsakey = RSA.importKey(result['key'])
    #     cipher = Cipher_pkcs1_v1_5.new(rsakey)
    #     cipher_text = base64.b64encode(
    #         cipher.encrypt(message.encode(encoding="utf-8")))

    #     cookies = {
    #         '$buvid3': 'D0F91575-9711-4DC6-945D-DFD886AA537749002infoc',
    #         'LIVE_BUVID': 'AUTO7215531554553297',
    #         'sid': 'cgv8n65s',
    #         'stardustvideo': '1',
    #         'CURRENT_FNVAL': '16',
    #         'UM_distinctid':
    #         '169c65cf49d281-0e535f0b9944e3-1a201708-18fd80-169c65cf49e738',
    #         'fts': '1554816673',
    #         'rpdid': '|(JY~JY)lJm~0J\'ullY|km~J|',
    #         'CURRENT_QUALITY': '32',
    #         '_uuid': '18193D65-6A6F-3C60-A39E-C5122D7E224164098infoc',
    #         'bp_t_offset_7073896': '278276587580201855',
    #         'JSESSIONID': '2E62623AC26241F9F92EC8E255538B2F',
    #     }

    #     headers = {
    #     'Origin': 'https://passport.bilibili.com',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    #     'User-Agent':
    #     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    #     'Content-Type': 'application/x-www-form-urlencoded',
    #     'Accept': 'application/json, text/plain, */*',
    #     'Referer': 'https://passport.bilibili.com/login',
    #     'Connection': 'keep-alive',
    # }

    #     data = {
    #     'captchaType': '11',
    #     'username': '1325904294@qq.com',
    #     'password':
    #      cipher_text,
    #     'keep': 'true',
    #     'key': key,
    #     'goUrl': 'https://www.bilibili.com/',
    #     'challenge': geetest.challenge,
    #     'validate': validate,
    #     'seccode': validate + '|jordan'
    # }

    #     response = requests.post('https://passport.bilibili.com/web/login/v2',
    #                             headers=headers,
    #                             cookies=cookies,
    #                             data=data)
    #     print(response.json())

    # Slide Cutom 测试
    # for _ in range(10):
    #     headers = {
    #         'accept-encoding': 'gzip, deflate, br',
    #         'accept-language': 'zh-CN,zh;q=0.9',
    #         'user-agent':
    #         'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    #         'accept': 'application/json, text/javascript, */*; q=0.01',
    #         'referer': 'https://www.geetest.com/demo/slide-custom.html',
    #         'authority': 'www.geetest.com',
    #         'x-requested-with': 'XMLHttpRequest',
    #     }
    #     params = (('t', str(int(time.time() * 1000))), )
    #     response = requests.get(
    #         'https://www.geetest.com/demo/gt/register-slide', params=params, headers=headers)
    #     result = response.json()
    #     gt = result['gt']
    #     challenge = result['challenge']
    #     geetest = Geetest(gt, challenge)
    #     print(f'validate: {geetest.crack()}')
    #     time.sleep(5)
