def add_digits(num):
    while num>10:
        s=0

        while num>0:
            s += num%10
            num //=10
        num = s

    return num


if __name__ == "__main__":
    num = int(input().strip())
    print(add_digits(num))