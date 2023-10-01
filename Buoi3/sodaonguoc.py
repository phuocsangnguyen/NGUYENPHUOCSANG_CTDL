def daonguoc(a):
    b=0
    while a>0:
        c=a%10
        b=b*10+c
        a=a//10
    return b
a_input=int(input(" nhập 1 số: "))
print(f"số đảo ngược là {daonguoc(a_input)}")