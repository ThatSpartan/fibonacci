def Clean(number):
    try:
        _int = int(number)
        return _int
    except ValueError:
        return 0

def Fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fibonacci(n-1) + Fibonacci(n-2)

def Ask():
    _input = input('Input length > ')
    _int = Clean(_input)

    print(Fibonacci(_int))

if __name__ == '__main__':
    while True:
        Ask()