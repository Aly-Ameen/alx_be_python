m = n = int(input('Enter the size of the pattern: '))
while m:
    for _ in range(n):
        print('*', end='')
    print()
    m -= 1
