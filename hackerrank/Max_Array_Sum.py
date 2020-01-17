
def maxSubsetSum(arr):

    maxes = arr[:2]
    maxes.append(max(maxes[0], maxes[0] + arr[2]))
    print(f'maxes init: {maxes}')

    for i in range(3, len(arr)):

        old_max = max(maxes[i - 2], maxes[i - 3])
        new_max = max(old_max, old_max + arr[i])

        print(f'{i}: {arr[i]} - ', old_max, new_max)

        maxes.append(new_max)

    print('\n', maxes)
    return max(maxes)


if __name__ == '__main__':

    arr = list(map(int, '3 7 4 6 5'.split(' ')))
    print('arr: ', arr, '\n')
    res = maxSubsetSum(arr)
    print('\n', res)


