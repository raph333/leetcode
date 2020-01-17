
def countSwaps(a):
    num_swaps = 0

    for i in range(len(a)):
        for j in range(len(a) - i - 1):

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                num_swaps += 1

    print(f'Array is sorted in {num_swaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
