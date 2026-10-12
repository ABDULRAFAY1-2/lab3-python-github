#defining functions
def add(a,b):
    print(a+b)
def subtract(a,b):
    print(a-b)
def multiply(a,b):
    print(a*b)
def divide(a,b):
    if b==0:
        print("CANNOT BE DIVIDED BY ZERO")
    else:
        print("RESULT:", a/b)
def even_odd(a,b):
    print(a%b)
def percentage(a,b):
    if b==0:
        print("cannot find the percentage")
    else:
        print((a/b)*100)
#using loops
while True:
    print(1, "ADDITION")
    print(2, "SUBTRACTION")
    print(3, "MULTIPLICATION")
    print(4, "DIVISION")
    print(5, "CHECK EVEN OR ODD")
    print(6, "FIND PERCENTAGE")
    print(7, "EXIT")
#choice
    choice= input("ENTER YOUR CHOICE: ")
    if choice == "1":
        num_1=float(input("ENTER YOUR FIRST NUMBER: "))
        num_2=float(input("ENTER YOUR SECOND NUMBER: "))
        add(num_1,num_2)
    elif choice=="2":
        num_1=float(input("ENTER YOUR FIRST NUMBER: "))
        num_2=float(input("ENTER YOUR SECOND NUMBER: "))
        subtract(num_1,num_2)
    elif choice=="3":
        num_1=float(input("ENTER YOUR FIRST NUMBER: "))
        num_2=float(input("ENTER YOUR SECOND NUMBER: "))
        multiply(num_1,num_2)
    elif choice=="4":
        num_1=float(input("ENTER YOUR FIRST NUMBER: "))
        num_2=float(input("ENTER YOUR SECOND NUMBER: "))
        divide(num_1,num_2)
    elif choice=="5":
        num_1=int(input("ENTER YOUR NUMBER: "))
        if(num_1%2==0):
            print("THE NUMBER IS EVEN")
        else:
            print("THE NUMBER IS ODD")
    elif choice=="6":
        num_1=float(input("ENTER YOUR FIRST NUMBER: "))
        num_2=float(input("ENTER YOUR SECOND NUMBER: "))
        percentage(num_1,num_2)
    elif choice=="7":
        print("EXITED CALCULATOR")
        break
    else:
        print("invalid choice")
