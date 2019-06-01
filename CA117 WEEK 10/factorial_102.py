def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    print(sumup(0))
    print(sumup(1))
    print(sumup(12))

if __name__ == "__main__":
    main()