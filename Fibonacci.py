fib = [0, 1]
index = int(input("What fib do you want? "))

if index < 3:
    print("Yeay: ", fib[index - 1])
else:
    for i in range(2, index):
        print(fib)
        fib.append(fib[i-1] + fib[i-2])

    print(fib)
    print("Yeay ", fib[index - 1])



def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(2))