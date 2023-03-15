fib = 0
fib1 = 1
# fibonacci = fib + fib1
num = int(input("Defina um número limite para ver a sequência de fibonacci: "))
while fib <= num:
    print(fib, end=' ')
    fibonacciSequence = [fib]
    fibonacci = fib + fib1
    fib = fib1
    fib1 = fibonacci
if num in fibonacciSequence:
    print(f"\nO número {num} faz parte da sequencia de fibonacci.")
else:
    print(f"\nO número {num} não faz parte da sequencia de fibonacci.")
