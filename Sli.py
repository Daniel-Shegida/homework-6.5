l = ['15' ,'14' ,'13' ,'12' ,'11' ,'10' ,'09' ,'08' ,'07' ,'06' ,'05' ,'04' ,'03' ,'02' ,'01' ,"  "]
active = 15
winner = 0
command = "p"

def paint():
    for i in range(14):
        print("_", end = "")
    print("_")
    for i in range(4):
        print("|",l[0 + 4 * i], l[1 + 4 * i],l[2 + 4 * i],l[3 + 4*  i],"|")
    print(" ", end="")
    for i in range(13):
        print("T", end = "")
    return

def clean():
    for i in range(4):
        print(" ")
    return
print("hints of controlling void  :w to go up s to go down a to go left and  d to go right")
print("enter your first command and start a game")
while winner != 1 :
    if l == ["  ",'01',"02","03","04","05","06",'07','08','09','10','11','12','13','14','15']:
        winner = 1
        print("congratulation u win this time")
    else :
        paint()
        print(" ")
        command = input()
        if command == "w":
            if active - 4 >= 0:
                a = l[active]
                l[active] = l[active - 4]
                l[active - 4] = a
                active = active - 4
            else:
                print("wrong command read the rules")
            clean()
        elif command == "s":
            if active + 4 <= 15:
                a = l[active]
                l[active] = l[active + 4]
                l[active + 4] = a
                active = active + 4
            else:
                print("wrong command read the rules")
            clean()
        elif command == "d":
            if active + 1 <= 15:
                a = l[active]
                l[active] = l[active + 1]
                l[active + 1] = a
                active = active + 1
            else:
                print("wrong command read the rules")
            clean()
        elif command == "a":
            if active - 1 >= 0:
                a = l[active]
                l[active] = l[active - 1]
                l[active - 1] = a
                active = active - 1
            else:
                print("wrong command read the rules")
            clean()
        else :
            print("a wrong command")
            clean()
