def is_happy(n):
    og = set()
    while n!=1 and n not in og:
        og.add(n)
        total = 0
        while n>0:
            digit = n%10
            total += digit**2
            n = n//10
        n = total
    return n ==1

if __name__ == "__main__":
    n = int(input("Enter the Number: ").strip())
    print(is_happy(n))
