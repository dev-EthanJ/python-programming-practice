
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

