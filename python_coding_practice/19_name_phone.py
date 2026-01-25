import re

name_phone = """
park 010-9999-9998
kim 010-9988-7766
lee 010-8789-5456
"""

def replace_hash(match):
    return "####"


p = re.compile(r"(\w+\s\d+[-]\d+[-])\d+")
print(p.sub(r"\1####", name_phone))