def Fibonacci(n):

    # Neu am thi bao loi
    if n < 0:
        print("Incorrect input")

    # Neu n = 0 thì trâ ve 0
    elif n == 0:
        return 0

    # Neu là 1 hoặc 2 thì tra ve 1
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


if __name__ == "__main__":
    print(Fibonacci(9))
