# .com, .net아닌 이메일주소 제외시키는 정규식
import re

text = """
park@naver.com
lee@myhome.co.kr
kim@daum.net
jang@develop.ai
"""

p = re.compile(r".*[@].*[.](?=net$|com$)", re.M)
m = p.findall(text)

print(m)