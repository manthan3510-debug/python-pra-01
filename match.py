# day = int(input("enter your day:"))

# match day:

#     case 1:
#         print("monday")

#     case 2:
#         print("tuesday")

#     case 3:
#         print("wed")
     
#     case 4:
#         print("thursday")

#     case _ :
#         print("invalid day")

# bank = int(input("enter your casse :"))

# match bank:

#     case 1:
#         print("withdrawal")
#     case 2:
#         print("transatiction")
#     case 3:
#         print("deposite money")
#     case 4:
#         print("exit ")
#     case _:
        # print("invalid ")

day = str(input("enter your day :"))

match day:
    case  "sat" | "sun":
        print("holiday")
    
    case _:
        print("working daays ")