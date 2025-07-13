def rooter(n, precision=0.0001):
    if n < 0:
        print("Negative numbers not accepted.")
    
    if n == 0:
        return 0.0

    x = n/2

    while True:
        y = (x + n / x)/2
        if abs(y - x) < precision:
            return y

        x = y


for i in range(0, 10):
    print(rooter(i))

