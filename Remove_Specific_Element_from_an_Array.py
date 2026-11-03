def remove_element(num, val):
    k = 0
    for i in range(len(num)):
        if num[k] !=val:
            num[k] = num[i]
            k+=1
    return k

if __name__ == "__main__":
    num = list(map(int, input().split()))
    val = int(input().strip())
    print(remove_element(num,val))