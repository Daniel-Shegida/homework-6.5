

print("enter your key(word)")
key = input()
print("enter your very improtant data")
string = input()
key = key*(len(string)//len(key)+1)
print("your encrypted data is ", end="")
for i in range(len(string)):
    if string[i] != " ":
        b = chr((ord(string[i])-96+(ord(key[i])-97)) % 26 + 96)
        if b == "`":
            print("z", end="")
        else:
            print(b, end="")
    else:
        print(" ", end="")
