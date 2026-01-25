# Python Programming Practice
## 파이썬 코딩 20제

1. 문자열 바꾸기

`a:b:c:d` 문자열을 split()과 join()함수를 사용해 다음과 같이 고치시오. `a#b#c#d`

```python
my_str = "a:b:c:d"

my_str = my_str.split(":")
my_str = "#".join(my_str)

print(my_str)
```

<br>

2. 딕셔너리 값 추출하기
   
다음은 딕셔너리 a에서 "C"라는 key에 해당하는 value를 출력하는 프로그램이다.

```python
a = {"A": 90, "B": 80}
a["C"] # KeyError
```

a 딕셔너리에는 "C"라는 key가 없으므로 위와 같은 오류가 발생한다. "C"에 해당하는 key값이 없을 경우, 오류 대신 70을 얻을 수 있도록 수정하시오.

```python
a = {"A": 90, "B": 80}
a.get("C", 70)
```

<br>

3. 리스트의 더하기와 extend 함수

다음과 같은 리스트 a가 있다.
`a = [1, 2, 3]` 리스트 a에 `[4, 5]`를 `+`를 사용해 더한 결과는 다음과 같다.

```python
a = [1, 2, 3]
a = a + [4, 5]
print(a)
```

```
[1, 2, 3, 4, 5]
```

리스트 a에 `[4, 5]`를 `extend`를 사용해 더한 결과는 다음과 같다.

```python
a = [1, 2, 3]
a.extend([4, 5])
print(a)
```

```
[1, 2, 3, 4, 5]
```

`+`를 사용하여 더한 것과 `extend`한 것의 차이점이 있으면 설명하시오.

- 연산자 `+`를 사용하면 연산결과를 변수에 저장해야 사용할 수 있다. `extend()`함수를 사용하면 원본 리스트가 변경되어 별도로 저장하지 않아도 된다.


<br>

4. 리스트 총합 구하기

다음 학급의 학생 점수를 나타낸 리스트에서 50점 이상 점수의 총합을 구하세요.

`scores = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]`

```python
scores = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

total = 0
for score in scores:
    if score >= 50:
        total += score

print(total)
```

<br>

5. 피보나치 함수

첫 번쨰 항의 값이 0이고, 두 번째 항의 값이 1일 때, 이후에 이어지는 항은 이전의 두 항을 더한 값으로 이루어지는 수열을 '피보나치 수열'이라고 한다. 입력을 정수 n으로 받았을 때, n항 이하까지의 피보나치 수열을 출력하는 함수를 작성하시오.

```python

def fibonacci(n):
    fibonacci = [0, 1]

    if n == 1: 
        print(fibonacci[:1])
    elif n == 2:
        print(fibonacci[:2])
    else:
        for i in range(2, n):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        print(fibonacci)
```

<br>

6. 숫자의 총합 구하기

사용자에게 다음과 같은 숫자를 입력받아 입력받은 숫자의 총합을 구하는 프로그램을 작성하시오. (단, 숫자는 ","로 구분하여 입력한다.)

`65,45,2,3,45,8`

```python

input_str = input("숫자를 ,로 구분하여 입력하세요.")
num_list = input_str.split(",")

total = 0
for num in num_list:
    total += int(num)

print(f"총합은 {total}입니다.")

```

<br>

7. 한 줄 구구단

사용자에게 2~9의 숫자중 하나를 입력받아 해당 숫자의 구구단을 한 줄로 출력하는 프로그램을 작성하시오.

```python
def input_num():
    while(True):
        num = int(input("2~9의 숫자중 하나를 입력하세요."))
        if num > 1 and num < 10: return num
        else: print("범위에 맞는 숫자를 입력하세요.")

def print_multiple(num):
    for i in range(1, 10):
        print(num * i, end=" ")

number = input_num()
print_multiple(number)
```

<br>

8. 파일을 읽어 역순으로 저장하기

다음과 같은 내용의 파일 `abc.txt`가 있다.

```
AAA
BBB
CCC
DDD
EEE
```

이 파일의 내용을 다음과 같이 역순으로 바꾸어 저장하시오.

```
EEE
DDD
CCC
BBB
AAA
```

```python
lines = []
with open("abc.txt", "r") as f:
    for line in f:
        if line[-1] != '\n':
            line += '\n'
        lines.append(line)
    print(lines)

with open("abc.txt", "w") as f:
    for index in range(len(lines) - 1, -1, -1):
        f.write(lines[index])
```

<br>

09. 평균값 구하기

총 10줄로 이루어져 있고, 각 줄마다 점수(0~100)이 쓰여진 `sample.txt`가 있다. 해당 파일의 숫자 값을 모두 읽어 총합과 평균값을 구한 후 평균값을 `result.txt`에 쓰는 프로그램을 작성하시오.

```python
scores = []
with open("sample.txt", "r") as f:
    for line in f:
        scores.append(int(line))

total = 0
average = 0

for score in scores:
    total += score

average = total / len(scores)

with open("result.txt", "w") as f:
    f.write(str(average))
```

<br>

10. 계산기 만들기

다음과 같이 동작하는 클래스 `Calculator`를 작성하시오.

```
>>> cal1 = Calculator([1, 2, 3, 4, 5])
>>> cal1.sum()
15
>>> cal1.avg()
3.0
>>> cal2 = Calculator([6, 7, 8, 9, 10])
>>> cal2.sum()
40
>>> cal2.avg()
8.0
```

```python
class Calculator:
    def __init__(self, data):
        self.data = data
        self.sum_data = None
        self.avg_data = None

    def sum(self):
        if self.sum_data is None:
            sum_total = 0
            for i in self.data:
                sum_total += i
            self.sum_data = sum_total
        return self.sum_data 
    
    def avg(self):
        if self.sum_data is None:
            self.sum()
        self.avg_data = self.sum_data / len(self.data)
        return self.avg_data 
```

<br>

11. 모듈을 사용하는 방법

다른 디렉터리에 `mymod.py` 파이썬 모듈이 있다고 가정해 보자. 명령 프롬프트 창에서 파이썬 셸을 열어 이 모듈을 import해서 사용할 수 있는 방법을 모두 기술하시오. (즉, import mymod를 수행할 때 오류가 없어야 한다.)

1. `sys.path.append` 사용하기. 파이썬 셸에서 `sys`모듈을 불러온 후 `sys.path`를 조회하여 라이브러리 디렉터리 목록을 확인한다. 그리고 `sys.path.append("path to mymod.py")` 명령어를 통해 `sys.path`에 `mymod.py`의 경로를 업데이트하여 이후 `import mymod`로 실행할 수 있다.  

2. `PYTHONPATH` 환경 변수 사용하기. 터미널에서 `set PYTHONPATH=path to mymod.py` 명령어를 입력한다. `PYTHONPATH`환경 변수에 `mymod`파일의 디렉토리를 설정하여 별도의 추가 작업 없이 `import mymod`를 진행할 수 있다.

<br>

12. 오류와 예외처리

다음 코드의 실행 결과를 예측하고 그 이유에 대해 설명하시오.

```python
result = 0

try:
    [1, 2, 3][3]
    "a" + 1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)
```

- try문 내부의 세 문장은 각각 IndexError, TypeError, ZeroDivisionError에 해당한다. 다만 try 실행 도중 한번이라도 예외 에러가 발생하면 예외처리 문구를 진행한 후 try문을 빠져나온다. 그래서 가장 첫번째 문장을 실행하며 IndexError가 발생하여 result==3이 된다. 이때, finally절은 예외발생여부에 상관 없이 항상 실행되므로, 최종 result == 7이 되어, `7`이 print된다.

<br>

13. DashInsert 함수

`DashInsert`함수는 숫자로 구성된 문자열을 입력받은 뒤, 문자열 안에서 홀수가 연속되면 두 수 사이에 `-`를 추가하고, 짝수가 연속되면 `*`을 추가하는 기능을 가지고 있다. `DashInsert`함수를 완성하시오.

```python

def DashInsert(data):
    flag_data = []
    for char in data:
        if int(char) % 2 == 0:
            flag_data.append(0)
        else:
            flag_data.append(1)

    new_data = ""
    for i in range(0, len(flag_data)):
        if i == 0: 
            new_data = str(data[0])
            continue
        if flag_data[i] == flag_data[i - 1]:
            if flag_data[i] == 0:
                new_data = new_data + "*" + str(data[i])
            if flag_data[i] == 1:
                new_data = new_data + "-" + str(data[i])
        else:
            new_data += data[i]

    return str(new_data)
```

<br>

14. 문자열 압축하기
문자열을 입력받아 같은 문자가 연속적으로 반복되는 경우, 그 반복 횟수를 표시해 문자열을 압축하여 표시하시오.

```
>>> aaabbcccccca
a3b2c6a1
```


```python

def CompressStr(data):
    before_char = ""
    count = 1
    new_str = ""
    data = data + "\n"
    for i in range(0, len(data)):
        if i == 0: 
            before_char = data[0]
            continue
        if before_char == data[i]:
            count += 1    
        else: # before_char != data[i]
            new_str = new_str + before_char + str(count)
            count = 1
        before_char = data[i]

    return new_str

print(CompressStr("aaabbcccccca"))

```

<br>

15. Duplicate Numbers 함수

0~9의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9의 모든 숫자를 각각 한 번씩만 사용한 것인지 확인하는 함수를 작성하시오.

```
>>> 0123456789 01234 01234567890 6789012345 012322456789
True False False True False
```

```python

def DuplicateNumbers(data):
    count_list = []
    for i in range(10):
        count_list.append(0)

    for number in data:
        count_list[int(number)] += 1

    flag = True
    for count in count_list:
        if count != 1:
            flag = False

    return flag

```

<br>

16. 모스부호 해독

문자열 형식으로 입력받은 모스 부호 .(dot)과 -(dash)를 해독하여 영어 문장으로 출력하는 프로그램을 작성하시오.

`mos_str = ".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"`

```python
morse_code = {
    # Alphabets
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    # Numbers
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}
dict_items = morse_code.items()
morse_list = list(map(lambda a: list(a), dict_items))


def CodeToChar(code):
    for item in morse_list:
        if item[1] == code:
            return str(item[0]) 
    return "ERROR"

def DecodingMorse(morse):
    result = ""
    word = ""
    for index in range(0, len(morse)):
        if morse[index] != " ":
            word += morse[index]
        else: # char == " "
            if morse[index - 1] != " ":
                # 코드를 문자로 변환하여 문자열에 추가
                result += CodeToChar(word)
                word = ""
                # print(result)
            if morse[index - 1] == " ":
                result += " "
                # print(result)

        if index == len(morse) - 1:
            # 코드를 문자로 변환하여 문자열에 추가
            result += CodeToChar(word)

    return result

morse_str = ".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"
print(DecodingMorse(morse_str))
```

<br>

17. 정규식 - 기초 메타 문자

다음 중 정규식 `a[.]{3,}b`와 매치되는 문자열은 무엇일까?

- `acccb`
- `a....b`
- `aaab`
- `a.cccb`

- 정답은 `a....b`이다. `[.]`메타문자에 의해 .이 반드시 있어야 하며, `{3,}`메타문자에 의해 3번부터 반복 가능하다.


<br>

18. 정규식 - 문자열 검색

다음 코드의 결괏값은 무엇일까?

```python
import re
p = re.compile("[a-z]+")
m = p.search("5 python")
print(m.start() + m.end())
```

- `m.start()`가 2이고, `m.end()`가 7이므로, 정답은 `9`가 print된다.

<br>

19. 정규식 - 그루핑

다음과 같은 문자열에서 휴대폰 번호 뒷자리인 숫자 4개를 ####로 바꾸는 프로그램을 정규식을 사용하여 작성하시오.

```
"""
park 010-9999-9998
kim 010-9988-7766
lee 010-8789-5456
"""
```

```python
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
```

<br>

20. 정규식 - 전방 탐색

다음은 이메일 주소를 나타내는 정규식이다. 이 정규식은 `park@naver.com,, kim@daum.net, lee@myhome.co.kr`등과 매치된다. 긍정형 전방 탐색 기법을 사용하여 `.com, .net`인 이메일 주소만 남기는 정규식을 작성하시오.

```python
# .com, .net아닌 이메일주소 제외시키는 정규식
import re

text = """
park@naver.com
lee@myhome.co.kr
kim@daum.net
jang@develop.ai
"""

p = re.compile(r".*[@].*[.](?=net$|com$).*$", re.M)
m = p.findall(text)

print(m)
```
