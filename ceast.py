print("enter your key(number)")
key = int(input())
print("enter your very improtant data")
string = input()
print("your encrypted data is ",end="")
for i in range(len(string)) :
    if string[i] != " ":
        b=chr((ord(string[i])-96+key)%26+96)
        if b =="`":print("z",end="")
        else :print(b,end="")
    else: print(" ",end="")