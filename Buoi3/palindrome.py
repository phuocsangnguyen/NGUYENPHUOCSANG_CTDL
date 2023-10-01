def palindrome(s):
    n=len(s)
    st=""
    for i in range(n):
        st=st+s[n-i-1]
    return st==s


a_input=input("nhap mot chuoi:")
if palindrome(a_input):
    print(" palindrome")
else:
    print("not palindrome ")