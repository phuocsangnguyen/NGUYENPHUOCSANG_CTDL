def anogram(c, d):
    if len(c) != len(d):
        return False

    char_count = {}
    for char in c:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in d:
        if char in char_count and char_count[char] > 0:
            char_count[char] -= 1
        else:
            return False

    for count in char_count.values():
        if count != 0:
            return False

    return True

a=input("nhap a ")
b=input("nhap b ")
if anogram(a,b):
    print(" anagram")
else:
    print("not anagram")
