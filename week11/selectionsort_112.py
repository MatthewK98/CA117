import random
def selectionsort(a):
    for done in range(len(a) - 1):
        min_value = a[done]
        min_index = done
        for i in range(done + 1, len(a)):
            if a[i] < min_value:
                min_value = a[i]
                min_index = i

        a[min_index], a[done] = a[done], a[min_index]


def main():
    A = random.sample(range(-99, 100), 10)

    print('Unsorted: {}'.format(A))
    selectionsort(A)
    print('Sorted: {}'.format(A))

if __name__ == '__main__':
    main()
