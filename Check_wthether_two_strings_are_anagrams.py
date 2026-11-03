def is_anagrams(s,t):
    if len(s) != len(t):
        return False

    if sorted(s) == sorted(t):
        return True
    else:
        return False


if __name__ == "__main__":
    s = input("Enter the word1: ").strip()
    t = input("Enter the Word2: ").strip()
    print(is_anagrams(s,t))