# a = int(input("enter your a number :"))
# b = int(input("enter your b numebr :"))
# c = int(input("enter your c number :"))

# if a>b and a>c:
#     print ("a is greater ")

# elif b>a and b>c:
#     print("b is greater")

# else:
#     print("c is greater")

# marks  = int(input("enter your marks: "))

# if marks>90:
#     print("grade a")

# elif marks>70:
#     print("grade b")

# elif marks>50:
#     print("grade c")

# elif marks>33:
#     print("grade d")

# elif marks < 33 and marks>0:
#     print("fail ")

# elif marks > 100 or marks < 0:
#     print("invaild marks:")


# else:
#     print(" invaild user :")

# cal using cal :

# a =  int (input("enter your number :"))
# op = input("enter your op -,+,/,* :")
# b = int(input("enter your number :"))

# if op == '+':
#     print("additinal value is ",a+b)
# elif op == '-':
#     print("subb value is ", a-b)
# elif op == '*':
#     print("enter value is",a*b)
# elif op == '/':
#     print("enter value is ",a/b)

# else:
#     print("innvaild syntax")

a = int(input("enter your a number  :"))
op =input("op is  +,-,/,* :")
b = int(input("enter your b number :"))

match op:
    case "+":
        print("additional number is this :",a+b)
    case "-":
        print("sub number is this :",a-b)
    case "*":
        print("multi number is this :", a*b)
    case "/":
        print("division number is this",a/b)
    case _:
        print("invaild number :")
    