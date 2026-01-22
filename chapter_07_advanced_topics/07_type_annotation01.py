# type annotation

num: int = 1

def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2))
# type이 달라도 오류가 발생하지는 않는다
print(add(1.2, 3.4))

# mypy 패키지를 이용해서 타입체크 가능