# Do it! 점프 투 파이썬
## Chapter 03. 제어문
### 연습문제

1. 조건문의 참과 거짓

- 다음 코드의 결과값은 무엇일까?

```python
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
```

```
shirt
```
<br>

2. 3의 배수의 합 구하기

- while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보자.

```python
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print(result)
```

<br>

3. 별 표시하기

```python
i = 0
while True:
    i += 1
    if i > 5: break
    print('*' * i)
```

```
*
**
***
****
*****
```
<br>

4. 1부터 100까지 출력하기

- for문을 사용해 1부터 100까지의 숫자를 출력해보자.

```python
for i in range(1, 101):
    print(i)
```

<br>

5. 평균 점수 구하기

- A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.

- `[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]`

- for문을 사용하여 A 학급의 평균 점수를 구해보자.

```python
scores = [70, 60, 55, 75, 95, 90, 80, 85, 100]
total = 0
for score in scores:
    total += score
average = total / len(scores)
print(average)
```

<br>

6. 리스트 컴프리헨션 사용하기

- 다음 소스 코드를 List comprehension을 사용하여 표현해보자.

```python
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n * 2)
print(result)
```

```python
numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)
```
