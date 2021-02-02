#！/user/bin/env python
#-*-coding: utf-8-*-
#@Time           : 2020/11/13 9:57
#@Author         : GodSpeed
#@File           : sm4_tool.py.py
#@Software       : PyCharm

#pip install -i https://pypi.tuna.tsinghua.edu.cn/simple gmssl

from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
import binascii
from heapq import heappush, heappop
from collections import OrderedDict
import base64

# str_url = base64.b64encode(bytes_url)  # 被编码的参数必须是二进制数据
# str_url = base64.b64decode(url).decode("utf-8")


class SM4:
    """
    国密sm4加解密
    """

    def __init__(self):
        self.crypt_sm4 = CryptSM4()

    def str_to_hexStr(self, hex_str):
        """
        字符串转hex
        :param hex_str: 字符串
        :return: hex
        """
        hex_data = hex_str.encode('utf-8')
        str_bin = binascii.unhexlify(hex_data)
        return str_bin.decode('utf-8')

    def encrypt(self, encrypt_key, value):
        """
        国密sm4加密
        :param encrypt_key: sm4加密key
        :param value: 待加密的字符串
        :return: sm4加密后的hex值
        """
        crypt_sm4 = self.crypt_sm4
        crypt_sm4.set_key(encrypt_key.encode(), SM4_ENCRYPT)
        date_str = str(value)
        encrypt_value = crypt_sm4.crypt_ecb(date_str.encode())  # bytes类型
        #return encrypt_value.hex()
        return base64.b64encode(encrypt_value)

    def decrypt(self, decrypt_key, encrypt_value):
        """
        国密sm4解密
        :param decrypt_key:sm4加密key
        :param encrypt_value: 待解密的hex值
        :return: 原字符串
        """
        crypt_sm4 = self.crypt_sm4
        crypt_sm4.set_key(decrypt_key.encode(), SM4_DECRYPT)
        #decrypt_value = crypt_sm4.crypt_ecb(bytes.fromhex(encrypt_value))  # bytes类型
        decrypt_value = crypt_sm4.crypt_ecb(base64.b64decode(encrypt_value))
        return self.str_to_hexStr(decrypt_value.hex())

if __name__ == '__main__':
    #str_data = {"ffffffwsdwefewd": "fefefewfwrv", "qazqaz": "vfbfrbgtrnujy"}
    # ADHFMUudFU1DHKHB
    key = "B56EC8BCB56AFCCD"
    #str_data = "abcd"
    SM4 = SM4()
    #print("待加密内容：", str_data)
    # encoding = SM4.encrypt(key, str_data)
    encoding ='9G87fTXkFugCuoOt4WHQj1+VnOHDqFkCE/hxo88phiwwKkFgy2RqX+zvvxCGi8bjK4SDRFGWo36uAleZ0orxmk1DN59e0j3Zsua0CQM8ds8vn4X6yLTTxVrolsUof+lrEookc2fd5rretKVi+FwvJvRIuoNeaHHc9p5kbxE0cWoHEYwUJ9Rult+vL502zKkdBfvkVnTL3S7OBl6htS/abiLkwQFLA7DQj/Spr+iEp14bzaz6ZBCv4aVsjRbglxVN+YWtjVLQQWC8azvocsCk4b+oF3EE0Ex9Bzs+T0w9VfvWj7KtSIGro0Hlq+6uzLb47H01e9LU8/Ixbd1HOqDDqrfnJAGWxuLqNqfOekDecTvT8Nu6Z11hg7X8otoUh0MpFmgS/ocRuDohPUVNZ/qWElzAc4laMK596soiNpu2i76PXk/CZZCBV+CnaA6X6xwQgaSGuyEkIcZntz0W+bUeZkVEwWGlXaEnQLtFdBK53awsngCHNaQiyaAWiSexRjX41iwok9HN8YvpQo0MUDHRtI7+NkNKuXoo+2yZ7fUJ1WbcaBEMduru5jpd1PC30XdEYPJ/g0ezeu3xbtr9s9SCA1m0sFctYeLQtkr24shP4v9e477BZkLJbM62BjmCeLBK0aVqVUcw7+GjPuNzUtMCwg+5oHPTCl8Kgm+uIQiB8Yw4dGBmdraxj0pLw2qZXT7iIHaUmr3YbEkXiXQ6DvHraKrZy97OX4lFNu2fnwKx08GHDYhHldnibdMfoYTqpfHUqm0UwBo8JhZUht0tOVaijIpIGxnCcHVl+NI9aiFB3bA8JpJ/JIk1UyuHy3P3pNizYECueAs8BxwHFvZtctlxkg693NggZligVhs1zJn8SXY='
    # print("国密sm4加密后的结果：", encoding)
    print("国密sm4解密后的结果：", SM4.decrypt(key, encoding))
